<!-- mcp-name: io.github.taylorwilsdon/workspace-mcp -->

<div align="center">

# <span style="color:#cad8d9">Google Workspace MCP Server</span> <img src="https://github.com/user-attachments/assets/b89524e4-6e6e-49e6-ba77-00d6df0c6e5c" width="80" align="right" />

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![PyPI](https://img.shields.io/pypi/v/workspace-mcp.svg)](https://pypi.org/project/workspace-mcp/)
[![PyPI Downloads](https://static.pepy.tech/personalized-badge/workspace-mcp?period=total&units=NONE&left_color=GREY&right_color=BLUE&left_text=pypi+downloads)](https://pepy.tech/projects/workspace-mcp)
[![MCP Toplist](https://mcptoplist.com/badge/glama%2Ftaylorwilsdon%2Fgoogle_workspace_mcp.svg)](https://mcptoplist.com/server/glama%2Ftaylorwilsdon%2Fgoogle_workspace_mcp)
[![Website](https://img.shields.io/badge/Website-workspacemcp.com-green.svg)](https://workspacemcp.com/?utm_source=github.com&utm_medium=referral&utm_campaign=readme&utm_content=badge-website)

*Full natural language control over Google Calendar, Drive, Gmail, Docs, Sheets, Slides, Forms, Tasks, Contacts, and Chat through all MCP clients, AI assistants and developer tools.*
*Includes a full featured CLI & Code Mode for use with tools like Claude Code and Codex!*

**The fastest, most feature-complete Google Workspace MCP server** is in a class of it's own: it can do things that Google's own tooling and the built in integrations with Claude and ChatGPT can't come close to with multi-user support, rich fine-grained editing tools and the most extensive coverage of any Workspace AI integration in existence. 

By leveraging native OAuth 2.1, stateless deployment capability and external auth server & gateway passthrough auth support, it's also the only Workspace MCP you can host for your whole organization centrally & securely! Supports all free Google accounts & Google Workspace plans with expanded app options like Chat & Spaces.

</div>

<p align="center">
  <a href="https://workspacemcp.com/docs?utm_source=github.com&utm_medium=referral&utm_campaign=readme&utm_content=hero-docs">
    <img src="https://img.shields.io/badge/Read%20the%20Docs-0969DA?style=for-the-badge&logo=readthedocs&logoColor=white" alt="Read the Docs">
  </a><a href="https://workspacemcp.com/quick-start?utm_source=github.com&utm_medium=referral&utm_campaign=readme&utm_content=hero-quickstart">
    <img src="https://img.shields.io/badge/Quick%20Start-2EA44F?style=for-the-badge" alt="Quick Start Guide">
  </a>
</p>

<div align="center">
<a href="https://www.pulsemcp.com/servers/taylorwilsdon-google-workspace">
<img width="375" src="https://github.com/user-attachments/assets/0794ef1a-dc1c-447d-9661-9c704d7acc9d" align="center"/>
</a>
</div>

<div align="center">
<a href="https://workspacemcp.com/workspace-mcp-cloud?utm_source=github.com&utm_medium=referral&utm_campaign=readme&utm_content=hero-cloud"><img width="400" height="53" alt="workspace-cloud" src="https://github.com/user-attachments/assets/349a6bab-c83a-4254-be2e-4ac6a9e8b3e5" /></a>
</div>

---

**See it in action:**
<div align="center">
  <video width="400" src="https://github.com/user-attachments/assets/a342ebb4-1319-4060-a974-39d202329710"></video>
</div>

---


## Debian package `mcp-server-googleoffice` (VitexSoftware fork)

This repository is the VitexSoftware fork of
[taylorwilsdon/google_workspace_mcp](https://github.com/taylorwilsdon/google_workspace_mcp).
Upstream base: **v2.4.1** (+13 commits, `b5d4323b`), last synced 2026-11-11.

```sh
apt install mcp-server-googleoffice           # server, /usr/bin/mcp-server-googleoffice
apt install mcprack-mcp-server-googleoffice   # registers it in the local mcprack catalog
```

The server is installed under `/usr/share/mcp-server-googleoffice`. The
launcher `/usr/bin/mcp-server-googleoffice` speaks **stdio** by default and
supports `--help` and `--version`. The upstream name `workspace-mcp` is kept
as a compatibility symlink.

The mcprack companion registers the server with `WORKSPACE_MCP_READ_ONLY=true`
and `MCP_SINGLE_USER_MODE=1`. Admins add the OAuth client as secrets in mcprack.

**Read-only mode** (`WORKSPACE_MCP_READ_ONLY=true`): the server requests only
read-only Google scopes. In this fork it also drops every tool that is not
annotated `readOnlyHint=true`. The one exception is `start_google_auth`,
which is needed to obtain credentials.

### Environment variables

The canonical list is `debian/server.json`, installed as
`/usr/share/mcp-server-googleoffice/server.json`.

| Variable | Secret | Required | Default | Meaning |
|---|---|---|---|---|
| `GOOGLE_OAUTH_CLIENT_ID` | yes | yes | | OAuth 2.0 client ID (Google Cloud console → Credentials) |
| `GOOGLE_OAUTH_CLIENT_SECRET` | yes | yes | | OAuth 2.0 client secret |
| `USER_GOOGLE_EMAIL` | no | no | | Default Google account for tool calls |
| `WORKSPACE_MCP_CREDENTIALS_DIR` | no | no | | Stored OAuth token directory; use a per-user path |
| `GOOGLE_SERVICE_ACCOUNT_KEY_JSON` | yes | no | | Service-account key for domain-wide delegation |
| `GOOGLE_SERVICE_ACCOUNT_KEY_FILE` | no | no | | Path to a service-account key file |
| `DWD_ALLOWED_DOMAINS` | no | no | | Domains the service account may impersonate |
| `MCP_SINGLE_USER_MODE` | no | no | `1` | Use stored credentials without session mapping |
| `WORKSPACE_MCP_READ_ONLY` | no | no | `true` | Read-only scopes and tools only |
| `WORKSPACE_MCP_TRANSPORT` | no | no | `stdio` | `stdio` or `streamable-http` |
| `WORKSPACE_MCP_TOOLS` | no | no | | Comma-separated services to load |
| `WORKSPACE_MCP_TOOL_TIER` | no | no | | `core`, `extended` or `complete` |
| `WORKSPACE_MCP_PERMISSIONS` | no | no | | Granular per-service permissions |
| `WORKSPACE_MCP_DISABLED_TOOLS` | no | no | | Comma-separated tools to block |
| `WORKSPACE_ATTACHMENT_DIR` | no | no | | Where downloaded attachments are stored |
| `GOOGLE_PSE_API_KEY` | yes | no | | Programmable Search Engine API key |
| `GOOGLE_PSE_ENGINE_ID` | no | no | | Programmable Search Engine ID |
| `WORKSPACE_MCP_LOG_LEVEL` | no | no | `INFO` | Log level |

On the stdio path, OAuth needs a one-time interactive consent. Run
`start_google_auth` once, or pre-seed `WORKSPACE_MCP_CREDENTIALS_DIR` with a
token, or use a service account with domain-wide delegation.

### Tools and annotation classes

<details><summary>119 tools</summary>

| Service | Tool | Title | Class |
|---|---|---|---|
| core | `start_google_auth` | Start Google Auth | create |
| gappsscript | `generate_trigger_code` | Generate Trigger Code | read-only |
| gappsscript | `get_script_activity` | Get Script Activity | read-only |
| gappsscript | `get_script_project` | Get Script Project | read-only |
| gappsscript | `get_script_version` | Get Script Version | read-only |
| gappsscript | `list_script_deployments` | List Script Deployments | read-only |
| gappsscript | `manage_deployment` | Manage Deployment | mutate (destructive, non-idempotent) |
| gappsscript | `manage_script_content` | Manage Script Content | mutate (destructive, non-idempotent) |
| gappsscript | `manage_script_project` | Manage Script Project | mutate (destructive, non-idempotent) |
| gappsscript | `manage_script_trigger` | Manage Script Trigger | mutate (destructive, non-idempotent) |
| gappsscript | `manage_script_version` | Manage Script Version | create |
| gappsscript | `run_script_function` | Run Script Function | mutate (destructive, non-idempotent) |
| gcalendar | `get_events` | Get Events | read-only |
| gcalendar | `list_calendars` | List Calendars | read-only |
| gcalendar | `manage_calendar` | Manage Calendar | mutate (destructive, non-idempotent) |
| gcalendar | `manage_event` | Manage Event | mutate (destructive, non-idempotent) |
| gcalendar | `manage_focus_time` | Manage Focus Time | mutate (destructive, non-idempotent) |
| gcalendar | `manage_out_of_office` | Manage Out of Office | mutate (destructive, non-idempotent) |
| gcalendar | `query_freebusy` | Query Freebusy | read-only |
| gchat | `create_reaction` | Create Reaction | create |
| gchat | `download_chat_attachment` | Download Chat Attachment | create |
| gchat | `get_messages` | Get Messages | read-only |
| gchat | `list_spaces` | List Spaces | read-only |
| gchat | `search_messages` | Search Messages | read-only |
| gchat | `send_message` | Send Message | mutate (destructive, non-idempotent) |
| gcontacts | `get_contact` | Get Contact | read-only |
| gcontacts | `get_contact_group` | Get Contact Group | read-only |
| gcontacts | `list_contact_groups` | List Contact Groups | read-only |
| gcontacts | `list_contacts` | List Contacts | read-only |
| gcontacts | `manage_contact` | Manage Contact | mutate (destructive, non-idempotent) |
| gcontacts | `manage_contact_group` | Manage Contact Group | mutate (destructive, non-idempotent) |
| gcontacts | `manage_contacts_batch` | Manage Contacts Batch | mutate (destructive, non-idempotent) |
| gcontacts | `search_contacts` | Search Contacts | read-only |
| gdocs | `batch_update_doc` | Batch Update Doc | mutate (destructive, non-idempotent) |
| gdocs | `create_doc` | Create Doc | create |
| gdocs | `create_table_with_data` | Create Table with Data | create |
| gdocs | `debug_table_structure` | Debug Table Structure | read-only |
| gdocs | `export_doc_to_pdf` | Export Doc to PDF | create |
| gdocs | `find_and_replace_doc` | Find and Replace Doc | mutate (destructive, non-idempotent) |
| gdocs | `get_doc_as_markdown` | Get Doc as Markdown | read-only |
| gdocs | `get_doc_content` | Get Doc Content | read-only |
| gdocs | `insert_doc_elements` | Insert Doc Elements | create |
| gdocs | `insert_doc_image` | Insert Doc Image | create |
| gdocs | `inspect_doc_structure` | Inspect Doc Structure | read-only |
| gdocs | `list_docs_in_folder` | List Docs in Folder | read-only |
| gdocs | `list_document_comments` | List Document Comments | read-only |
| gdocs | `manage_doc_tab` | Manage Doc Tab | mutate (destructive, non-idempotent) |
| gdocs | `manage_document_comment` | Manage Document Comment | mutate (destructive, non-idempotent) |
| gdocs | `modify_doc_text` | Modify Doc Text | mutate (destructive, non-idempotent) |
| gdocs | `search_docs` | Search Docs | read-only |
| gdocs | `update_doc_headers_footers` | Update Doc Headers Footers | mutate (destructive, non-idempotent) |
| gdocs | `update_paragraph_style` | Update Paragraph Style | create |
| gdrive | `check_drive_file_public_access` | Check Drive File Public Access | read-only |
| gdrive | `copy_drive_file` | Copy Drive File | create |
| gdrive | `create_drive_file` | Create Drive File | create |
| gdrive | `create_drive_folder` | Create Drive Folder | create |
| gdrive | `get_drive_file_content` | Get Drive File Content | read-only |
| gdrive | `get_drive_file_download_url` | Get Drive File Download URL | read-only |
| gdrive | `get_drive_file_permissions` | Get Drive File Permissions | read-only |
| gdrive | `get_drive_shareable_link` | Get Drive Shareable Link | read-only |
| gdrive | `import_to_google_doc` | Import to Google Doc | create |
| gdrive | `import_to_google_sheets` | Import to Google Sheets | create |
| gdrive | `import_to_google_slides` | Import to Google Slides | create |
| gdrive | `list_drive_items` | List Drive Items | read-only |
| gdrive | `manage_drive_access` | Manage Drive Access | mutate (destructive, non-idempotent) |
| gdrive | `search_drive_files` | Search Drive Files | read-only |
| gdrive | `set_drive_file_permissions` | Set Drive File Permissions | mutate (destructive, non-idempotent) |
| gdrive | `update_drive_file` | Update Drive File | mutate (destructive, non-idempotent) |
| gforms | `batch_update_form` | Batch Update Form | mutate (destructive, non-idempotent) |
| gforms | `create_form` | Create Form | create |
| gforms | `get_form` | Get Form | read-only |
| gforms | `get_form_response` | Get Form Response | read-only |
| gforms | `list_form_responses` | List Form Responses | read-only |
| gforms | `set_publish_settings` | Set Publish Settings | create |
| gmail | `batch_modify_gmail_message_labels` | Batch Modify Gmail Message Labels | mutate (destructive, non-idempotent) |
| gmail | `draft_gmail_message` | Draft Gmail Message | create |
| gmail | `get_gmail_attachment_content` | Get Gmail Attachment Content | create |
| gmail | `get_gmail_message_content` | Get Gmail Message Content | read-only |
| gmail | `get_gmail_messages_content_batch` | Get Gmail Messages Content Batch | read-only |
| gmail | `get_gmail_thread_content` | Get Gmail Thread Content | read-only |
| gmail | `get_gmail_threads_content_batch` | Get Gmail Threads Content Batch | read-only |
| gmail | `list_gmail_filters` | List Gmail Filters | read-only |
| gmail | `list_gmail_labels` | List Gmail Labels | read-only |
| gmail | `manage_gmail_filter` | Manage Gmail Filter | mutate (destructive, non-idempotent) |
| gmail | `manage_gmail_label` | Manage Gmail Label | mutate (destructive, non-idempotent) |
| gmail | `modify_gmail_message_labels` | Modify Gmail Message Labels | mutate (destructive, non-idempotent) |
| gmail | `search_gmail_messages` | Search Gmail Messages | read-only |
| gmail | `send_gmail_message` | Send Gmail Message | mutate (destructive, non-idempotent) |
| gsearch | `get_search_engine_info` | Get Search Engine Info | read-only |
| gsearch | `search_custom` | Search Custom | read-only |
| gsheets | `append_table_rows` | Append Table Rows | create |
| gsheets | `create_sheet` | Create Sheet | create |
| gsheets | `create_spreadsheet` | Create Spreadsheet | create |
| gsheets | `format_sheet_range` | Format Sheet Range | mutate (destructive, non-idempotent) |
| gsheets | `get_spreadsheet_info` | Get Spreadsheet Info | read-only |
| gsheets | `list_sheet_tables` | List Sheet Tables | read-only |
| gsheets | `list_spreadsheet_comments` | List Spreadsheet Comments | read-only |
| gsheets | `list_spreadsheets` | List Spreadsheets | read-only |
| gsheets | `manage_conditional_formatting` | Manage Conditional Formatting | mutate (destructive, non-idempotent) |
| gsheets | `manage_named_range` | Manage Named Range | mutate (destructive, non-idempotent) |
| gsheets | `manage_sheet_tab` | Manage Sheet Tab | mutate (destructive, non-idempotent) |
| gsheets | `manage_spreadsheet_comment` | Manage Spreadsheet Comment | mutate (destructive, non-idempotent) |
| gsheets | `modify_sheet_values` | Modify Sheet Values | mutate (destructive, non-idempotent) |
| gsheets | `move_sheet_rows` | Move Sheet Rows | mutate (destructive, non-idempotent) |
| gsheets | `read_sheet_values` | Read Sheet Values | read-only |
| gsheets | `resize_sheet_dimensions` | Resize Sheet Dimensions | mutate (destructive, non-idempotent) |
| gslides | `batch_update_presentation` | Batch Update Presentation | mutate (destructive, non-idempotent) |
| gslides | `create_presentation` | Create Presentation | create |
| gslides | `get_page` | Get Page | read-only |
| gslides | `get_presentation` | Get Presentation | read-only |
| gslides | `list_presentation_comments` | List Presentation Comments | read-only |
| gslides | `manage_presentation_comment` | Manage Presentation Comment | mutate (destructive, non-idempotent) |
| gslides | `render_page_to_image` | Render Page to Image | read-only |
| gtasks | `get_task` | Get Task | read-only |
| gtasks | `get_task_list` | Get Task List | read-only |
| gtasks | `list_task_lists` | List Task Lists | read-only |
| gtasks | `list_tasks` | List Tasks | read-only |
| gtasks | `manage_task` | Manage Task | mutate (destructive, non-idempotent) |
| gtasks | `manage_task_list` | Manage Task List | mutate (destructive, non-idempotent) |

</details>

## What It Does

Workspace MCP connects AI assistants to all twelve major Google Workspace services - 120+ tools behind a single MCP server, with OAuth 2.1 multi-user auth, three progressive tool tiers, read-only mode, a full CLI, and stateless container deployment. It runs locally over stdio for legacy clients and remotely over streamable HTTP with full implementation of the latest MCP spec.

The README covers just enough to get you running, with extensive documentation on the website:

| Where to go | What you'll find |
|:---|:---|
| **[Quick&nbsp;Start](https://workspacemcp.com/quick-start?utm_source=github.com&utm_medium=referral&utm_campaign=readme&utm_content=nav-quickstart)** | Google Cloud setup, credentials, and client connection with screenshots |
| **[Full&nbsp;Documentation](https://workspacemcp.com/docs?utm_source=github.com&utm_medium=referral&utm_campaign=readme&utm_content=nav-docs)** | Every tool, parameter, and auth mode |
| **[Advanced&nbsp;Deployment](https://workspacemcp.com/docs/deployment?utm_source=github.com&utm_medium=referral&utm_campaign=readme&utm_content=nav-deployment)** | Reverse proxy & nginx config, origin validation, credential store backends (GCS/CMEK), [trusted-gateway identity](https://workspacemcp.com/docs/deployment/gateway-identity?utm_source=github.com&utm_medium=referral&utm_campaign=readme&utm_content=nav-gateway-identity), and the complete environment variable reference |
| **[Client&nbsp;Setup&nbsp;Guides](https://workspacemcp.com/guides?utm_source=github.com&utm_medium=referral&utm_campaign=readme&utm_content=nav-guides)** | Claude Desktop/web Connectors, ChatGPT Developer Mode, and more |
| **[FAQ&nbsp;&&nbsp;Troubleshooting](https://workspacemcp.com/welcome/faq?utm_source=github.com&utm_medium=referral&utm_campaign=readme&utm_content=nav-faq)** | Enabling Google APIs, OAuth errors, redirect URIs, Google Chat setup, client quirks |

## <span style="color:#adbcbc">Security & Compliance</span>

<table>
<tr>
<td valign="top" width="50%">

**For Security Teams**

By default, this server sends no data anywhere except Google's APIs, on behalf of the authenticated user, using your own OAuth client credentials. There is no usage reporting, analytics, license server, or SaaS dependency outside optional OTel support for your own usage.

- **Fully open source** — every line is auditable in this repo
- **Your OAuth client, your GCP project** — credentials never leave your environment & you control scopes
- **You control the network** — deploy behind your reverse proxy, in your VPC, on your own terms
- **Stateless mode** — zero disk writes for locked-down container environments
- **Sensitive path blocking** — local file reads default to the managed attachment directory, and `validate_file_path()` still blocks `.env*` files plus common home-directory credential stores such as `~/.ssh/` and `~/.aws/` even if `ALLOWED_FILE_DIRS` is broadened

Full dependency tree in `pyproject.toml`, pinned in `uv.lock`.

</td>
<td valign="top" width="50%">

**For Legal & Procurement**

This project is [MIT licensed](LICENSE) — 

- **Use commercially without restriction** — build products, sell services, deploy internally
- **Fork, embed, redistribute** — MIT requires only attribution
- **No CLA** — contributions remain under MIT
- **No built-in telemetry to disclose** — optional tracing is off unless you configure it
- **No network effects** — the server never contacts any endpoint you didn't configure
- **Standard dependency licenses** — MIT, Apache 2.0, and BSD throughout the dependency chain; no copyleft, no AGPL
</td>
</tr>
</table>

## Services

<table width="100%" align="center">
<tr>
<td align="center" width="25%">
<h3>📧</h3><a href="https://workspacemcp.com/gmail?utm_source=github.com&utm_medium=referral&utm_campaign=readme&utm_content=services-gmail"><b>Gmail</b></a><br>
<sub>15 tools - search, send, draft,<br>labels, filters, attachments</sub>
</td>
<td align="center" width="25%">
<h3>📁</h3><a href="https://workspacemcp.com/google-drive?utm_source=github.com&utm_medium=referral&utm_campaign=readme&utm_content=services-google-drive"><b>Drive</b></a><br>
<sub>16 tools - search, create, share,<br>import Office files</sub>
</td>
<td align="center" width="25%">
<h3>📅</h3><a href="https://workspacemcp.com/google-calendar?utm_source=github.com&utm_medium=referral&utm_campaign=readme&utm_content=services-google-calendar"><b>Calendar</b></a><br>
<sub>7 tools - events, sharing, free/busy,<br>Out of Office, Focus Time</sub>
</td>
<td align="center" width="25%">
<h3>📝</h3><a href="https://workspacemcp.com/google-docs?utm_source=github.com&utm_medium=referral&utm_campaign=readme&utm_content=services-google-docs"><b>Docs</b></a><br>
<sub>19 tools - edit, style, tables,<br>tabs, comments, export</sub>
</td>
</tr>
<tr>
<td align="center" width="25%">
<h3>📊</h3><a href="https://workspacemcp.com/google-sheets?utm_source=github.com&utm_medium=referral&utm_campaign=readme&utm_content=services-google-sheets"><b>Sheets</b></a><br>
<sub>14 tools - ranges, tables,<br>formatting, conditional rules</sub>
</td>
<td align="center" width="25%">
<h3>🖼️</h3><a href="https://workspacemcp.com/google-slides?utm_source=github.com&utm_medium=referral&utm_campaign=readme&utm_content=services-google-slides"><b>Slides</b></a><br>
<sub>7 tools - create, batch update,<br>slide images, comments</sub>
</td>
<td align="center" width="25%">
<h3>📋</h3><a href="https://workspacemcp.com/google-forms?utm_source=github.com&utm_medium=referral&utm_campaign=readme&utm_content=services-google-forms"><b>Forms</b></a><br>
<sub>6 tools - build forms, publish,<br>read responses</sub>
</td>
<td align="center" width="25%">
<h3>✅</h3><a href="https://workspacemcp.com/google-tasks?utm_source=github.com&utm_medium=referral&utm_campaign=readme&utm_content=services-google-tasks"><b>Tasks</b></a><br>
<sub>6 tools - tasks & lists<br>with hierarchy</sub>
</td>
</tr>
<tr>
<td align="center" width="25%">
<h3>👤</h3><a href="https://workspacemcp.com/google-contacts?utm_source=github.com&utm_medium=referral&utm_campaign=readme&utm_content=services-google-contacts"><b>Contacts</b></a><br>
<sub>8 tools - people, groups,<br>batch operations</sub>
</td>
<td align="center" width="25%">
<h3>💬</h3><a href="https://workspacemcp.com/google-chat?utm_source=github.com&utm_medium=referral&utm_campaign=readme&utm_content=services-google-chat"><b>Chat</b></a><br>
<sub>6 tools - spaces, messages,<br>search, reactions</sub>
</td>
<td align="center" width="25%">
<h3>🔍</h3><a href="https://workspacemcp.com/google-search?utm_source=github.com&utm_medium=referral&utm_campaign=readme&utm_content=services-google-search"><b>Custom Search</b></a><br>
<sub>2 tools - programmable<br>web search</sub>
</td>
<td align="center" width="25%">
<h3>⚡</h3><a href="https://workspacemcp.com/google-apps-script?utm_source=github.com&utm_medium=referral&utm_campaign=readme&utm_content=services-google-apps-script"><b>Apps Script</b></a><br>
<sub>15 tools - write, deploy,<br>run & debug scripts</sub>
</td>
</tr>
</table>

Each page lists every tool with its tier, parameters, required scopes, and example prompts. The [complete reference](https://workspacemcp.com/docs?utm_source=github.com&utm_medium=referral&utm_campaign=readme&utm_content=services-docs-all) covers all twelve in one place.

> 💬 **Google Chat** needs a one-time Chat app configuration and a Workspace account - see the [Chat setup FAQ](https://workspacemcp.com/welcome/faq?utm_source=github.com&utm_medium=referral&utm_campaign=readme&utm_content=services-chat-faq).

## Quick Start

> Set credentials → pick a launch command → connect your client. Full walkthrough with screenshots: **[workspacemcp.com/quick-start](https://workspacemcp.com/quick-start?utm_source=github.com&utm_medium=referral&utm_campaign=readme&utm_content=quickstart-hero)**

You'll need an OAuth client from [Google Cloud Console](https://console.cloud.google.com/) in a project with the Google APIs enabled for the services you plan to use. The docs have [one-click enable links for every API](https://workspacemcp.com/docs?utm_source=github.com&utm_medium=referral&utm_campaign=readme&utm_content=quickstart-enable-apis#authentication) plus a single `gcloud services enable` command that covers them all, and the [quick start guide](https://workspacemcp.com/quick-start?utm_source=github.com&utm_medium=referral&utm_campaign=readme&utm_content=quickstart-inline) walks through the whole setup in about five minutes.

> **Agentic OAuth clients:** this server only calls Google's REST APIs, so your OAuth client does not need Google's "Use this client for an AI-powered agent" setting. If your organization wants agent traffic labeled for admin controls, create a separate client with that setting enabled; it can't be changed on an existing client after November 12, 2026.

<table>
<tr>
<td valign="top" width="50%">

**Confidential Client**

```bash
# 1. Credentials
export GOOGLE_OAUTH_CLIENT_ID="..."
export GOOGLE_OAUTH_CLIENT_SECRET="..."

# 2. Launch - pick a tier
uvx workspace-mcp --tool-tier core       # essential tools
uvx workspace-mcp --tool-tier extended   # core + management ops
uvx workspace-mcp --tool-tier complete   # everything

# Or cherry-pick services
uvx workspace-mcp --tools gmail drive calendar
```

</td>
<td valign="top" width="50%">

**OAuth 2.1 (PKCE)**

```bash
# 1. Credentials - MCP clients connect with PKCE and no
#    secret, but Google still requires one server-side
export MCP_ENABLE_OAUTH21=true
export GOOGLE_OAUTH_CLIENT_ID="..."
export GOOGLE_OAUTH_CLIENT_SECRET="..."
#    Alternatively, point GOOGLE_CLIENT_SECRET_PATH at a client_secret.json
#    that contains the client id and secret (env vars take precedence).
export WORKSPACE_MCP_PORT=8000
export GOOGLE_OAUTH_REDIRECT_URI="http://localhost:${WORKSPACE_MCP_PORT}/oauth2callback"
export OAUTHLIB_INSECURE_TRANSPORT=1

# 2. Launch - OAuth 2.1 requires HTTP transport
uvx workspace-mcp --transport streamable-http --tool-tier core
```

</td>
</tr>
</table>

**Tool tiers** keep context windows lean: `core` is the essential set, `extended` adds management operations, `complete` loads everything. Combine with `--tools <service> ...`, `--read-only`, or per-service `--permissions`, and subtract individual tools with `--disabled-tools <name> ...` - details in the [server modes docs](https://workspacemcp.com/docs?utm_source=github.com&utm_medium=referral&utm_campaign=readme&utm_content=tiers-server-modes#server-modes).

**Per-request toolsets** let HTTP clients sharing one server see different tools, using the same headers as the GitHub MCP server. `X-MCP-Toolsets` takes comma-separated service names (the `--tools` names, e.g. `gmail,drive`) and `X-MCP-Tools` takes comma-separated tool names (e.g. `search_gmail_messages`); when both are sent the request gets the union. Names ignore case and whitespace, unknown names match nothing, and a blank or missing header leaves the tool list unchanged. Headers only narrow what the server already loaded: a tool removed by the tier, `--tools`, `--read-only`, `--permissions` or `--disabled-tools` stays unavailable, and calls to tools outside the request's selection fail as unknown tools.

## Connect Your Client

**Claude Desktop, web & mobile** - run the server in HTTP mode and add it as a **Connector** (Settings → Connectors → Add custom connector). This is the recommended path; the [Connector guide](https://workspacemcp.com/guides/claude-connectors?utm_source=github.com&utm_medium=referral&utm_campaign=readme&utm_content=clients-connectors) has step-by-step screenshots. Legacy stdio configuration remains available for clients without Connector support - see the [FAQ](https://workspacemcp.com/welcome/faq?utm_source=github.com&utm_medium=referral&utm_campaign=readme&utm_content=clients-connectors-faq).

**Claude Code**

```bash
# Start the server in HTTP mode, then:
claude mcp add --transport http workspace-mcp http://localhost:8000/mcp

# Optional: install the bundled skill for better Workspace tool routing
ln -s "$(pwd)/skills/managing-google-workspace" ~/.claude/skills/managing-google-workspace
```

**ChatGPT** - connect via Developer Mode with the [ChatGPT guide](https://workspacemcp.com/guides/chatgpt-developer-mode?utm_source=github.com&utm_medium=referral&utm_campaign=readme&utm_content=clients-chatgpt).

**VS Code, LM Studio, Open WebUI, and everything else** - any MCP client works over streamable HTTP (recommended) or stdio. Client-specific walkthroughs live in the [guides](https://workspacemcp.com/guides?utm_source=github.com&utm_medium=referral&utm_campaign=readme&utm_content=clients-guides) and [FAQ](https://workspacemcp.com/welcome/faq?utm_source=github.com&utm_medium=referral&utm_campaign=readme&utm_content=clients-guides-faq).

## CLI

`workspace-cli` lists and calls tools against a running server with encrypted, disk-backed OAuth token caching - authenticate once, script forever:

```bash
uv run workspace-cli list
uv run workspace-cli call search_gmail_messages query="is:unread" max_results=5
```

Install globally with `uv tool install .` from this repo. ⚠️ Don't use `uvx workspace-cli` - an abandoned PyPI package squats that name.

## Deployment & Advanced Configuration

Everything you need to run this in production lives in two places. The [documentation](https://workspacemcp.com/docs?utm_source=github.com&utm_medium=referral&utm_campaign=readme&utm_content=deploy-docs) covers auth modes and server configuration:

- **[OAuth 2.1 multi-user auth](https://workspacemcp.com/docs?utm_source=github.com&utm_medium=referral&utm_campaign=readme&utm_content=deploy-oauth21#authentication)** - bearer tokens, required for remote or shared HTTP endpoints
- **[Stateless container mode](https://workspacemcp.com/docs?utm_source=github.com&utm_medium=referral&utm_campaign=readme&utm_content=deploy-stateless#authentication)** - zero disk writes for locked-down deployments
- **[OAuth proxy storage backends](https://workspacemcp.com/docs?utm_source=github.com&utm_medium=referral&utm_campaign=readme&utm_content=deploy-proxy-storage#authentication)** - memory, disk, or Valkey/Redis for distributed setups
- **[External OAuth provider mode](https://workspacemcp.com/docs?utm_source=github.com&utm_medium=referral&utm_campaign=readme&utm_content=deploy-external-oauth#authentication)** - bring your own auth server, validate bearer tokens only
- **[Service accounts with domain-wide delegation](https://workspacemcp.com/docs?utm_source=github.com&utm_medium=referral&utm_campaign=readme&utm_content=deploy-service-accounts#authentication)** - per-request user impersonation with an optional domain allowlist
- **[Trusted-gateway identity](https://workspacemcp.com/docs/deployment/gateway-identity?utm_source=github.com&utm_medium=referral&utm_campaign=readme&utm_content=deploy-gateway-identity)** - proxy-verified per-user isolation with Pomerium, Cloudflare Access, oauth2-proxy, or any JWKS-verifiable gateway
- **[OpenTelemetry tracing](https://workspacemcp.com/docs?utm_source=github.com&utm_medium=referral&utm_campaign=readme&utm_content=deploy-otel#server-modes)** - optional, off unless you configure an OTLP endpoint
- **Docker** - `docker build -t workspace-mcp . && docker run -p 8000:8000 workspace-mcp`

The **[Advanced Deployment guide](https://workspacemcp.com/docs/deployment?utm_source=github.com&utm_medium=referral&utm_campaign=readme&utm_content=deploy-advanced)** covers self-hosting specifics: reverse proxy setup with `WORKSPACE_EXTERNAL_URL` (including the nginx `Origin: null` consent workaround, the `WORKSPACE_MCP_ALLOW_NULL_ORIGIN_CONSENT` escape hatch, and the `Referrer-Policy` pitfall), origin validation and VS Code webview allowlisting, credential store backends (local directory or GCS with CMEK enforcement), and the **[complete environment variable reference](https://workspacemcp.com/docs/deployment?utm_source=github.com&utm_medium=referral&utm_campaign=readme&utm_content=deploy-env-vars#environment-variables)**.

Production tuning is all environment variables; the names below link to their reference entries.

- **Google API requests:** [`WORKSPACE_MCP_GOOGLE_API_WORKERS`](https://workspacemcp.com/docs/deployment?utm_source=github.com&utm_medium=referral&utm_campaign=readme&utm_content=deploy-env-vars#WORKSPACE_MCP_GOOGLE_API_WORKERS), [`WORKSPACE_MCP_GOOGLE_API_TIMEOUT_SECONDS`](https://workspacemcp.com/docs/deployment?utm_source=github.com&utm_medium=referral&utm_campaign=readme&utm_content=deploy-env-vars#WORKSPACE_MCP_GOOGLE_API_TIMEOUT_SECONDS)
- **External OAuth token validation:** [`WORKSPACE_MCP_TOKEN_VALIDATION_WORKERS`](https://workspacemcp.com/docs/deployment?utm_source=github.com&utm_medium=referral&utm_campaign=readme&utm_content=deploy-env-vars#WORKSPACE_MCP_TOKEN_VALIDATION_WORKERS), [`WORKSPACE_MCP_TOKEN_VALIDATION_CACHE_TTL`](https://workspacemcp.com/docs/deployment?utm_source=github.com&utm_medium=referral&utm_campaign=readme&utm_content=deploy-env-vars#WORKSPACE_MCP_TOKEN_VALIDATION_CACHE_TTL)
- **Memory ceilings:** [`WORKSPACE_MCP_MAX_FILE_BYTES`](https://workspacemcp.com/docs/deployment?utm_source=github.com&utm_medium=referral&utm_campaign=readme&utm_content=deploy-env-vars#WORKSPACE_MCP_MAX_FILE_BYTES), [`WORKSPACE_MCP_STATELESS_INLINE_MAX_BYTES`](https://workspacemcp.com/docs/deployment?utm_source=github.com&utm_medium=referral&utm_campaign=readme&utm_content=deploy-env-vars#WORKSPACE_MCP_STATELESS_INLINE_MAX_BYTES), [`WORKSPACE_MCP_MAX_OFFICE_XML_BYTES`](https://workspacemcp.com/docs/deployment?utm_source=github.com&utm_medium=referral&utm_campaign=readme&utm_content=deploy-env-vars#WORKSPACE_MCP_MAX_OFFICE_XML_BYTES)
- **Text returned per call:** `get_drive_file_content` returns long content a page at a time by default, so a long file does not fill the model's context. `WORKSPACE_MCP_MAX_CONTENT_CHARS` sets the page size (default `40000`; `0` returns whole content by default). Each page ends with a note giving the `offset` to read on from. This is only the default: a client can always pass `full_content=true` to get the whole file in one call. Text being read page by page is kept in memory for ten minutes so later pages are not downloaded again, within `WORKSPACE_MCP_PAGED_CONTENT_CACHE_BYTES` per process (default `33554432`, 32 MiB; `0` keeps nothing).
- **Sessions and health probes:** [`WORKSPACE_MCP_SESSION_IDLE_TIMEOUT`](https://workspacemcp.com/docs/deployment?utm_source=github.com&utm_medium=referral&utm_campaign=readme&utm_content=deploy-env-vars#WORKSPACE_MCP_SESSION_IDLE_TIMEOUT), [`WORKSPACE_MCP_READINESS_TIMEOUT_SECONDS`](https://workspacemcp.com/docs/deployment?utm_source=github.com&utm_medium=referral&utm_campaign=readme&utm_content=deploy-env-vars#WORKSPACE_MCP_READINESS_TIMEOUT_SECONDS)
- **DNS-rebinding protection:** `WORKSPACE_MCP_ALLOWED_HOSTS`, a comma-separated list of hostnames without ports (for example `workspace-mcp,10.0.0.5`). When set, requests whose `Host` is not loopback, listed, or the host of `WORKSPACE_EXTERNAL_URL` or an allowed origin get `403`, so include every name clients and health probes use. Unset, any `Host` is accepted.
- **Hosted servers without access to the caller's disk:** [`WORKSPACE_MCP_DISABLE_LOCAL_FILES`](https://workspacemcp.com/docs/deployment?utm_source=github.com&utm_medium=referral&utm_campaign=readme&utm_content=deploy-env-vars#WORKSPACE_MCP_DISABLE_LOCAL_FILES)
  With local files disabled, `create_drive_file`, `update_drive_file` and the import tools offer `return_upload_url`: the caller PUTs the bytes to the returned URL. If the file sits in a cloud-mirrored folder (Drive for desktop), copy it to a local directory first, since mirrored paths can stall mid-upload.
- **OAuth 2.1 token refresh and lifetimes:** see [`.env.oauth21`](.env.oauth21)
- **OAuth 2.1 consent screen:** `WORKSPACE_MCP_OAUTH_PROXY_REQUIRE_CONSENT=remember` shows the OAuth proxy's consent screen once per browser for each MCP client instead of on every authorization; cross-site navigations are still prompted. The default, `always`, prompts every time. Any other value fails startup.
- **OAuth 2.1 Google account choice:** `WORKSPACE_MCP_OAUTH_PROXY_GOOGLE_PROMPT` sets the `prompt` the OAuth proxy sends to Google's authorization endpoint (default `consent`); external provider mode ignores it. `select_account consent` shows Google's account chooser, so a user signed in to Google with another account can pick the right one, and still returns a refresh token. The only other accepted value is `consent`; anything else fails startup.

For downloads, horizontally scaled or scale-to-zero HTTP deployments (Cloud Run, Kubernetes) can stage attachments in Google Cloud Storage instead of instance-local disk, whose `/attachments/{id}` URL may reach a different instance. Install the `gcs` extra and set `WORKSPACE_MCP_FILES_GCS_BUCKET` to a bucket name; objects are written under `WORKSPACE_MCP_FILES_GCS_PREFIX` (default `attachments`) and handed out as V4 signed URLs valid for one hour, which the client fetches straight from GCS. This also lets stateless mode return download URLs instead of inline files. stdio ignores the setting, since its client reads the local file path directly. The runtime service account needs object read and write access on the bucket — `roles/storage.objectUser`, or `roles/storage.objectCreator` plus `roles/storage.objectViewer` — and, without an exported private key, `roles/iam.serviceAccountTokenCreator` on itself so URLs can be signed through IAM. Read access is not optional: a signed URL carries the signer's authority, so without `storage.objects.get` the upload and the signing both succeed while the client's download fails with `403`. Objects are not deleted by the server, so add a bucket lifecycle rule that removes them after a few hours.

## Security Best Practices

By default this server sends no data anywhere except Google's APIs, using your own OAuth client credentials - no usage reporting, analytics, license server, or SaaS dependency. MIT licensed with no CLA, no dual licensing, and no copyleft in the dependency chain. The full security posture - scope minimization, sensitive-path blocking, stateless mode - is documented at [workspacemcp.com](https://workspacemcp.com/privacy?utm_source=github.com&utm_medium=referral&utm_campaign=readme&utm_content=security-privacy).

A few things worth internalizing before you connect an LLM to your email:

- **Prompt injection is real.** Emails, docs, and events can contain hidden instructions. Only connect trusted data to an LLM, and be deliberate about which write tools you enable.
- **Never commit** `.env`, `client_secret.json`, or `.credentials/` to source control.
- **Local file reads are sandboxed** to the managed attachment directory. Broaden with `ALLOWED_FILE_DIRS` only if you trust the client and its data sources; `.env*`, `~/.ssh/`, `~/.aws/`, and similar paths are always blocked.
- **Production** deployments should use HTTPS and OAuth 2.1.

## Development

```bash
uv sync --group dev    # install deps
uv run ruff check .    # lint
uv run pytest          # test
```

Single-file service modules live in `g<service>/`, tools are registered with `@server.tool` decorators, and tiers are defined in `core/tool_tiers.yaml`. PRs welcome.

## License

MIT - see [`LICENSE`](LICENSE). The license is 21 lines and says what it means.

_Workspace MCP is an independent open-source project and is not affiliated with, endorsed by, or sponsored by Google LLC. Google and Google Workspace are trademarks of Google LLC._

---

Validations:
[![MCP Badge](https://lobehub.com/badge/mcp/taylorwilsdon-google_workspace_mcp)](https://lobehub.com/mcp/taylorwilsdon-google_workspace_mcp)
