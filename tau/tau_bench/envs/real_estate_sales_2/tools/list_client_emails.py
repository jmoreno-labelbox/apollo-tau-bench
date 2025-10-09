from tau_bench.envs.tool import Tool
import json
from itertools import islice
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ListClientEmails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], client_id: str = None) -> str:
        rows = [e for e in (data.get("emails") or []) if e.get("client_id") == client_id]
        payload = {"client_id": client_id, "emails": rows}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListClientEmails",
                "description": "List all emails for a client.",
                "parameters": {
                    "type": "object",
                    "properties": {"client_id": {"type": "integer"}},
                    "required": ["client_id"],
                },
            },
        }
