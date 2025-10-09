from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class MutateConsultantContact(Tool):
    """Modify contact information for the consultant."""

    @staticmethod
    def invoke(data: dict[str, Any], consultant_id: str, address: str = None, phone: str = None, email: str = None, gst_number: str = None) -> str:
        updates = {
            k: v
            for k, v in {"address": address, "phone": phone, "email": email, "gst_number": gst_number}.items()
            if v is not None
        }
        row = next(
            (c for c in data.get("consultants", {}).values() if c.get("consultant_id") == consultant_id),
            None,
        )
        if not row:
            payload = {"error": f"consultant_id '{consultant_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out
        row.update(updates)
        row["updated_at"] = _now_iso()
        payload = {"consultant_id": consultant_id, "updated": updates}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "MutateConsultantContact",
                "description": "Update contact fields for a consultant.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "consultant_id": {"type": "string"},
                        "address": {"type": "string"},
                        "phone": {"type": "string"},
                        "email": {"type": "string"},
                        "gst_number": {"type": "string"},
                    },
                    "required": ["consultant_id"],
                },
            },
        }
