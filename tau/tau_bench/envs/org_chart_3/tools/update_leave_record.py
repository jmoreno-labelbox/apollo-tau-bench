# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class update_leave_record(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], leave_id: str, updates: Dict[str, Any]) -> str:
        records = data.get("leave_records", [])
        for rec in records:
            if rec["leave_id"] == leave_id:
                rec.update(updates)
                data["leave_records"] = records
                return json.dumps({"success": f"leave {leave_id} updated"}, indent=2)
        return json.dumps({"error": f"leave_id {leave_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_leave_record",
                "description": "Patch one or more fields (end_date, status, notes …) on an existing leave record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "leave_id": {"type": "string"},
                        "updates": {"type": "object"}
                    },
                    "required": ["leave_id", "updates"],
                    "additionalProperties": False
                }
            }
        }
