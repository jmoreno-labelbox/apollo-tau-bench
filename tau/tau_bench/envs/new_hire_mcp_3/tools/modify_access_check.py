from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ModifyAccessCheck(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], updates: dict[str, Any] = None, check_id: str = None) -> str:
        updates = updates or {}
        checks = data.get("access_checks", {}).values()
        for c in checks.values():
            if c.get("check_id") == check_id:
                c.update(updates)
                c["updated_at"] = _fixed_now_iso()
        payload = {"updated_check_id": check_id, "updates": updates}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAccessCheck",
                "description": "Update an access check status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "check_id": {"type": "string"},
                        "updates": {"type": "object"},
                    },
                    "required": ["check_id", "updates"],
                },
            },
        }
