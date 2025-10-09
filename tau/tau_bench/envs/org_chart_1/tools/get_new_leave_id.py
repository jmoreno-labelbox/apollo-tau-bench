from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class get_new_leave_id(Tool):
    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        leaves = data.get("leaves", {}).values()
        prefix = "LV"
        start_num = 10000

        if not leaves:
            payload = f"{prefix}{start_num}"
            out = json.dumps(payload, indent=2)
            return out

        max_id_num = 0
        for leave in leaves:
            leave_id = leave.get("leave_id", "")
            if leave_id.startswith(prefix):
                try:
                    num = int(leave_id[len(prefix) :])
                    if num > max_id_num:
                        max_id_num = num
                except (ValueError, TypeError):
                    continue

        next_id_num = max(start_num, max_id_num) + 1
        payload = f"{prefix}{next_id_num}"
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetNewLeaveId",
                "description": "Return a leave ID that is not currently in use.",
                "parameters": {},
            },
        }
