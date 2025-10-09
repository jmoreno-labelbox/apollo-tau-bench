from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CreatePublisher(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], publisher_id: str = None, name: str = None, address: str = None, contact_email: str = None, gst_number: str = None) -> str:
        publishers = data.get("publishers", [])
        row = {
            "publisher_id": publisher_id,
            "name": name,
            "address": address,
            "contact_email": contact_email,
            "gst_number": gst_number,
            "created_at": _fixed_now_iso(),
            "updated_at": _fixed_now_iso(),
        }
        publishers.append(row)
        payload = row
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreatePublisher",
                "description": "Create a publisher row.",
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
