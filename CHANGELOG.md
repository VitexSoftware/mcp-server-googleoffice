# Changelog (VitexSoftware fork)

Upstream release notes: https://github.com/taylorwilsdon/google_workspace_mcp/releases

## 2.4.1-1 (2026-11-11)

- Initial Debian packaging as `mcp-server-googleoffice` with the mcprack companion
  `mcprack-mcp-server-googleoffice`. Upstream base: v2.4.1 (`b5d4323b`).
- Read-only mode also removes tools that are not annotated read-only.
- `--version` option added.
- `copy_drive_file` sends `copyComments` only when requested, so it works with older
  google-api-python-client. With trixie's 2.166, `copy_comments=true` still fails.
