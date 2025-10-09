from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdatePublisherContact(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        publisher_id: str,
        address: str = None,
        contact_email: str = None,
        gst_number: str = None
    ) -> str:
        row = next(
            (p for p in data.get("publishers", []) if p.get("publisher_id") == publisher_id),
            None,
        )
        if not row:
            payload = {"error": f"Publisher '{publisher_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out
        updates = {
            "address": address,
            "contact_email": contact_email,
            "gst_number": gst_number
        }
        updates = {k: v for k, v in updates.items() if v is not None}
        row.update(updates)
        row["updated_at"] = _fixed_now_iso()
        payload = {"publisher_id": publisher_id, "updated": updates}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdatePublisherContact",
                "description": "Update a publisher’s contact fields.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "publisher_id": {"type": "string"},
                        "address": {"type": "string"},
                        "contact_email": {"type": "string"},
                        "gst_number": {"type": "string"},
                    },
                    "required": ["publisher_id"],
                },
            },
        }
