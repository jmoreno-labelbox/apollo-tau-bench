from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class create_leave_record(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], leave: dict[str, Any]) -> str:
        if not leave:
            payload = {"error": "leave record required"}
            out = json.dumps(payload, indent=2)
            return out
        lv = data.get("leave_records", {}).values()
        data["leave_records"][leave["leave_record_id"]] = leave
        data["leave_records"] = lv
        payload = {"success": f'leave {leave["leave_id"]} requested'}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateLeaveRecord",
                "description": "Insert a leave request; status should start as 'Pending'.",
                "parameters": {
                    "type": "object",
                    "properties": {"leave": {"type": "object"}},
                    "required": ["leave"],
                    "additionalProperties": False,
                },
            },
        }
