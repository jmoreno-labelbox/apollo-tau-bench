# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_new_leave_id(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], ) -> str:
        leaves = data.get("leaves", [])
        prefix = "LV"
        start_num = 10000

        if not leaves:
            return json.dumps(f"{prefix}{start_num}", indent=2)

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
        return json.dumps(f"{prefix}{next_id_num}", indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_new_leave_id",
                "description": "Return a leave ID that is not currently in use.",
                "parameters": {},
            },
        }
