from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ModifyEmailLabel(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], 
        updates: dict[str, Any] = None, 
        label_id: str = None,
        email_id: str = None
    ) -> str:
        updates = updates or {}
        labels = data.get("email_labels", [])
        for l in labels:
            if l.get("label_id") == label_id:
                l.update(updates)
                l["updated_at"] = _fixed_now_iso()
        payload = {"updated_label_id": label_id, "updates": updates}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateEmailLabel",
                "description": "Update an email label.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "label_id": {"type": "string"},
                        "updates": {"type": "object"},
                    },
                    "required": ["label_id", "updates"],
                },
            },
        }
