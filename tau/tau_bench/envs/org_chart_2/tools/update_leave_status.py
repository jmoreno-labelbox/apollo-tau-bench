# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class update_leave_status(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], leave_id: str, status: str) -> str:
        lv = data.get("leave_records", [])

        for leave_record in lv:
            if leave_record["leave_id"] == leave_id:
                leave_record["status"] = status
                data["leave_records"] = lv
                return json.dumps(
                    {"success": f"leave {leave_id} set to {status}"}, indent=2
                )

        return json.dumps({"error": f"leave_id {leave_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_leave_status",
                "description": "Change status of an existing leave record (e.g., Approved, Denied).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "leave_id": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "required": ["leave_id", "status"],
                    "additionalProperties": False,
                },
            },
        }
