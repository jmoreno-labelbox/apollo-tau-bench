from tau_bench.envs.tool import Tool
import json
from typing import Any

class add_leave_record(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], leave_record: dict) -> str:
        records = data.setdefault("leave_records", [])
        records.append(leave_record)
        payload = {"success": True, "leave_id": leave_record.get("leave_id")}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddLeaveRecord",
                "description": "Add a new leave record. The leave_record object must contain all required fields.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "leave_record": {
                            "type": "object",
                            "description": "Leave record to add",
                        }
                    },
                    "required": ["leave_record"],
                    "additionalProperties": False,
                },
            },
        }
