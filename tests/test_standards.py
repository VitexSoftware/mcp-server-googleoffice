"""VitexSoftware MCP-SERVER-STANDARDS checks (section 7).

Runs against the source tree (pytest from the repo root) or the installed
tree (autopkgtest sets PYTHONPATH=/usr/share/mcp-server-googleoffice).
"""

import json
import os
import pathlib
import subprocess
import sys

import pytest

SERVICE_MODULES = [
    "gmail.gmail_tools",
    "gdrive.drive_tools",
    "gcalendar.calendar_tools",
    "gdocs.docs_tools",
    "gsheets.sheets_tools",
    "gchat.chat_tools",
    "gforms.forms_tools",
    "gslides.slides_tools",
    "gtasks.tasks_tools",
    "gcontacts.contacts_tools",
    "gsearch.search_tools",
    "gappsscript.apps_script_tools",
]

# Tools whose name suggests read-only but which write to local disk; they are
# annotated non-read-only on purpose (and dropped in read-only mode).
NAME_RULE_EXCEPTIONS = {"get_gmail_attachment_content"}

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent


def _hint(annotations, snake, camel):
    value = getattr(annotations, snake, None)
    if value is None:
        value = getattr(annotations, camel, None)
    return value


class _Ann:
    def __init__(self, hints):
        (self.read_only_hint, self.destructive_hint,
         self.idempotent_hint, self.open_world_hint) = hints


class _Tool:
    def __init__(self, row):
        self.name, self.title, self.description, hints = row
        self.annotations = _Ann(hints) if hints is not None else None


@pytest.fixture(scope="module")
def tools():
    # Collect in a subprocess: other tests mutate the shared server instance.
    return [_Tool(row) for row in _probe(read_only=False)]


def test_tools_registered(tools):
    assert len(tools) > 100


def test_every_tool_has_title_and_four_hints(tools):
    problems = []
    for tool in tools:
        if not tool.title or tool.title == tool.name:
            problems.append(f"{tool.name}: missing/raw title")
        if not tool.description:
            problems.append(f"{tool.name}: missing description")
        ann = tool.annotations
        if ann is None:
            problems.append(f"{tool.name}: no annotations")
            continue
        hints = {
            "read_only": _hint(ann, "read_only_hint", "readOnlyHint"),
            "destructive": _hint(ann, "destructive_hint", "destructiveHint"),
            "idempotent": _hint(ann, "idempotent_hint", "idempotentHint"),
            "open_world": _hint(ann, "open_world_hint", "openWorldHint"),
        }
        for key, value in hints.items():
            if value is None:
                problems.append(f"{tool.name}: {key} hint not set")
        if hints["read_only"] and hints["destructive"]:
            problems.append(f"{tool.name}: read_only and destructive")
    assert not problems, "\n".join(problems)


def test_name_consistency(tools):
    problems = []
    for tool in tools:
        ann = tool.annotations
        ro = _hint(ann, "read_only_hint", "readOnlyHint")
        destructive = _hint(ann, "destructive_hint", "destructiveHint")
        if tool.name in NAME_RULE_EXCEPTIONS:
            continue
        if tool.name.startswith(("get_", "list_", "search_")) and ro is not True:
            problems.append(f"{tool.name}: get/list/search must be read-only")
        if ("delete" in tool.name or "remove" in tool.name) and not destructive:
            problems.append(f"{tool.name}: delete/remove must be destructive")
    assert not problems, "\n".join(problems)


_PROBE = r"""
import asyncio, importlib, json, sys
from auth.scopes import set_read_only
read_only = sys.argv[2] == "1"
set_read_only(read_only)
for mod in json.loads(sys.argv[1]):
    importlib.import_module(mod)
from core.server import server
if read_only:
    from core.tool_registry import filter_server_tools
    filter_server_tools(server)

def hint(a, snake, camel):
    v = getattr(a, snake, None)
    return getattr(a, camel, None) if v is None else v

out = []
for t in asyncio.run(server.list_tools()):
    a = t.annotations
    hints = None if a is None else [
        hint(a, "read_only_hint", "readOnlyHint"),
        hint(a, "destructive_hint", "destructiveHint"),
        hint(a, "idempotent_hint", "idempotentHint"),
        hint(a, "open_world_hint", "openWorldHint"),
    ]
    out.append([t.name, t.title, bool(t.description), hints])
print(json.dumps(out))
"""


def _child_env(**extra):
    env = dict(os.environ)
    path = env.get("PYTHONPATH")
    env["PYTHONPATH"] = (
        path if path and "mcp-server-googleoffice" in path else str(REPO_ROOT)
    )
    env.update(extra)
    return env


def _probe(read_only):
    result = subprocess.run(
        [sys.executable, "-c", _PROBE, json.dumps(SERVICE_MODULES),
         "1" if read_only else "0"],
        capture_output=True,
        text=True,
        timeout=120,
        env=_child_env(),
        cwd=os.environ.get("AUTOPKGTEST_TMP", str(REPO_ROOT)),
    )
    assert result.returncode == 0, result.stderr[-2000:]
    return json.loads(result.stdout.strip().splitlines()[-1])


def test_read_only_mode_registers_only_read_only_tools():
    tools = _probe(read_only=True)
    assert tools, "read-only mode left no tools"
    offenders = [
        name
        for name, _title, _desc, hints in tools
        if (hints is None or hints[0] is not True) and name != "start_google_auth"
    ]
    assert not offenders, offenders


def _main_script():
    installed = pathlib.Path("/usr/share/mcp-server-googleoffice/main.py")
    if "mcp-server-googleoffice" in os.environ.get("PYTHONPATH", "") and installed.exists():
        return installed
    return REPO_ROOT / "main.py"


def test_secret_not_echoed_in_error_output():
    secret = "S3cr3t-should-never-be-printed-0123456789"
    result = subprocess.run(
        [sys.executable, str(_main_script())],
        capture_output=True,
        text=True,
        timeout=60,
        env=_child_env(
            GOOGLE_OAUTH_CLIENT_ID="test.apps.googleusercontent.com",
            GOOGLE_OAUTH_CLIENT_SECRET=secret,
            GOOGLE_PSE_API_KEY=secret,
            WORKSPACE_MCP_TOOLS="not-a-service",
        ),
        stdin=subprocess.DEVNULL,
    )
    assert result.returncode != 0
    assert secret not in result.stdout
    assert secret not in result.stderr


def test_version_flag():
    result = subprocess.run(
        [sys.executable, str(_main_script()), "--version"],
        capture_output=True,
        text=True,
        timeout=60,
        env=_child_env(),
    )
    assert result.returncode == 0
    assert result.stdout.strip()


def _server_json():
    for candidate in (
        REPO_ROOT / "debian" / "server.json",
        pathlib.Path("/usr/share/mcp-server-googleoffice/server.json"),
    ):
        if candidate.exists():
            return json.loads(candidate.read_text())
    pytest.skip("server.json not available")


def test_server_json_env_vars_documented_in_readme():
    readme = REPO_ROOT / "README.md"
    if not readme.exists():
        pytest.skip("README.md not available (installed-tree run)")
    text = readme.read_text()
    manifest = _server_json()
    names = [
        env["name"]
        for pkg in manifest["packages"]
        for env in pkg.get("environmentVariables", [])
    ]
    assert names
    missing = [n for n in names if f"| `{n}` |" not in text]
    assert not missing, missing
