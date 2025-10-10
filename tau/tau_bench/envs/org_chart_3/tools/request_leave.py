# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class request_leave(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], leave: Dict[str, Any]) -> str:
        if not leave:
            return json.dumps({"error": "leave record required"}, indent=2)
        lv = data.get("leave_records", [])
        lv.append(leave)
        data["leave_records"] = lv
        return json.dumps({"success": f'leave {leave["leave_id"]} requested'}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "request_leave",
                "description": "Insert a leave request; status should start as 'Pending'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "leave": {"type": "object"}
                    },
                    "required": ["leave"],
                    "additionalProperties": False
                }
            }
        }
