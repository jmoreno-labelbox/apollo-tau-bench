from tau_bench.envs.tool import Tool
import json
from typing import Any

class update_leave_record(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], leave_id: str, updates: dict[str, Any]) -> str:
        records = data.get("leave_records", [])
        for rec in records:
            if rec["leave_id"] == leave_id:
                rec.update(updates)
                data["leave_records"] = records
                payload = {"success": f"leave {leave_id} updated"}
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"leave_id {leave_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateLeaveRecord",
                "description": "Patch one or more fields (end_date, status, notes …) on an existing leave record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "leave_id": {"type": "string"},
                        "updates": {"type": "object"},
                    },
                    "required": ["leave_id", "updates"],
                    "additionalProperties": False,
                },
            },
        }
