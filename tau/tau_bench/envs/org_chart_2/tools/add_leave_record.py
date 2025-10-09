from tau_bench.envs.tool import Tool
import json
from typing import Any

class add_leave_record(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], leave: dict[str, Any]) -> str:
        leave_records = data.setdefault("leave_records", [])
        leave_records.append(leave)
        payload = leave
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "addLeaveRecord",
                "description": "Insert a new leave record into leave_records for the specified employee.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "leave": {
                            "type": "object",
                            "description": "Complete leave record object including leave_id, employee_id, leave_type, start_date, end_date, status, and notes.",
                        }
                    },
                    "required": ["leave"],
                    "additionalProperties": False,
                },
            },
        }
