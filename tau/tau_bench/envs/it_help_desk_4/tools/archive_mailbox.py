# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ArchiveMailbox(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        employee_id = kwargs.get("employee_id")
        mailboxes = data.get("mailboxes", [])
        archives = data.setdefault("data_archives", [])
        mailbox = next((m for m in mailboxes if m.get("employee_id") == employee_id), None)
        if not mailbox:
            return json.dumps({"error": f"Mailbox for employee {employee_id} not found."}, indent=2)
        mailbox["status"] = "archived"
        archive_id = f"arch_{mailbox['mailbox_id'].split('_')[-1]}"
        new_archive = {"archive_id": archive_id, "employee_id": employee_id, "mailbox_id": mailbox["mailbox_id"], "archive_path": f"s3://corp-archives/mail/{employee_id}/{FIXED_NOW.split('T')[0]}", "retention_policy": mailbox["retention_policy"], "created_at": FIXED_NOW}
        archives.append(new_archive)
        return json.dumps(new_archive, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "archive_mailbox", "description": "Archives a user's mailbox and creates a data archive record.", "parameters": {"type": "object", "properties": {"employee_id": {"type": "string"}}, "required": ["employee_id"]}}}
