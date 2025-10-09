from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ModifyAttachment(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], updates: dict[str, Any] = None, attachment_id: str = None) -> str:
        updates = updates or {}
        attach_id = attachment_id
        attachments = data.get("attachments", [])
        for a in attachments:
            if a.get("attachment_id") == attach_id:
                a.update(updates)
                a["updated_at"] = _fixed_now_iso()
        payload = {"updated_attachment_id": attach_id, "updates": updates}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateAttachment",
                "description": "Update an attachment metadata.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "attachment_id": {"type": "string"},
                        "updates": {"type": "object"},
                    },
                    "required": ["attachment_id", "updates"],
                },
            },
        }
