---
name: google-workspace
description: Read and manage Gmail, Google Drive, Calendar, Docs, Sheets, Slides, Forms, Tasks, Contacts and Chat through the mcp-server-googleoffice MCP server. Use when a task needs data from, or changes to, a user's Google Workspace account.
---

# Google Workspace (mcp-server-googleoffice)

- Start with read-only tools (`search_*`, `list_*`, `get_*`, `read_sheet_values`, `get_doc_as_markdown`).
- Tools that send mail (`send_gmail_message`, Chat `send_message`), share files
  (`manage_drive_access`, `set_drive_file_permissions`) or run code
  (`run_script_function`) are destructive. Confirm with the user before you call them.
- If a call fails with an authentication error, call `start_google_auth` and give the user the link.
- In read-only deployments (`WORKSPACE_MCP_READ_ONLY=true`), mutating tools are not registered.
- The detailed upstream skill is in `skills/managing-google-workspace/SKILL.md`.
