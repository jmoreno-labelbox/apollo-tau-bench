RULES = [
    "All operations must be deterministic using 2025-01-01 and 2025-01-01T09:00:00Z.",
    "Only update existing candidates, inventory assets, and asset requests; creation of these entities is not allowed.",
    "Creation is allowed for emails, email_labels, onboarding_files, attachments, access_checks, mcp_tool_calls, terminal_log.",
    "IDs must follow stable formats; new IDs may be introduced only for emails, email_labels, attachments, onboarding_files, access_checks, mcp_tool_calls, terminal_log.",
    "Sequential IDs must use max(existing)+1 with zero-padding width based on existing rows (default width 4).",
    "Onboarding paths must be /onboarding/<candidate_slug> where candidate_slug lowercases and replaces non-alphanumerics with underscores.",
    "Onboarding file writes must be idempotent by file_path.",
    "Emails may be inserted with deterministic message_id values provided in the instruction.",
    "Applying labels must de-duplicate label_ids for an email.",
    "Asset assign sets status='Assigned' and release sets status='Available'. No-op outputs are allowed when identifiers are unknown.",
    "Asset requests are updated by request_id; unknown requests produce deterministic no-op outputs.",
    "insert_access_check sets checked_ts=NOW_TS when missing.",
    "Checklist updates set updated_ts=NOW_TS; unknown items yield deterministic no-op outputs.",
    "insert_terminal_log and record_mcp_tool_call allocate deterministic sequential IDs.",
    "Tool outputs must never include the substring \"error\"."
]