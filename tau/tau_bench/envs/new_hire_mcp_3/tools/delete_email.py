from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class DeleteEmail(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], message_id: str = None, email_id: Any = None) -> str:
        emails = data.get("emails", [])
        data["emails"] = [e for e in emails if e.get("message_id") != message_id]
        payload = {"deleted_message_id": message_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DeleteEmail",
                "description": "Delete an email by message ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"message_id": {"type": "string"}},
                    "required": ["message_id"],
                },
            },
        }
