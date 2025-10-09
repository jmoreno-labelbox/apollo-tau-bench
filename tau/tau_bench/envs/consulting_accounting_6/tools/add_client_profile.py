from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class AddClientProfile(Tool):
    """Add a new client/publisher entry."""

    @staticmethod
    def invoke(data: dict[str, Any], publisher_id: str = None, name: str = None, address: str = None, contact_email: str = None, gst_number: str = None) -> str:
        tbl = data.get("publishers", {}).values()
        row = {
            "publisher_id": publisher_id,
            "name": name,
            "address": address,
            "contact_email": contact_email,
            "gst_number": gst_number,
            "created_at": _now_iso(),
            "updated_at": _now_iso(),
        }
        data["publishers"][publisher_id] = row
        payload = row
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddClientProfile",
                "description": "Create a client/publisher row.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "publisher_id": {"type": "string"},
                        "name": {"type": "string"},
                        "address": {"type": "string"},
                        "contact_email": {"type": "string"},
                        "gst_number": {"type": "string"},
                    },
                    "required": ["publisher_id", "name"],
                },
            },
        }
