from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ArchiveMailbox(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str) -> str:
        mailboxes = data.get("mailboxes", {}).values()
        archives = data.setdefault("data_archives", [])
        mailbox = next(
            (m for m in mailboxes.values() if m.get("employee_id") == employee_id), None
        )
        if not mailbox:
            payload = {"error": f"Mailbox for employee {employee_id} not found."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        mailbox["status"] = "archived"
        archive_id = f"arch_{mailbox['mailbox_id'].split('_')[-1]}"
        new_archive = {
            "archive_id": archive_id,
            "employee_id": employee_id,
            "mailbox_id": mailbox["mailbox_id"],
            "archive_path": f"s3://corp-archives/mail/{employee_id}/{FIXED_NOW.split('T')[0]}",
            "retention_policy": mailbox["retention_policy"],
            "created_at": FIXED_NOW,
        }
        data["archives"][archive_id] = new_archive
        payload = new_archive
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ArchiveMailbox",
                "description": "Archives a user's mailbox and creates a data archive record.",
                "parameters": {
                    "type": "object",
                    "properties": {"employee_id": {"type": "string"}},
                    "required": ["employee_id"],
                },
            },
        }
