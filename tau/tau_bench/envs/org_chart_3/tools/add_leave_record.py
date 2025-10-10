# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class add_leave_record(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], leave: Dict[str, Any]) -> str:
        leave_records = data.setdefault("leave_records", [])
        leave_records.append(leave)
        return json.dumps(leave, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_leave_record",
                "description": "Insert a new leave record into leave_records for the specified employee.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "leave": {
                            "type": "object",
                            "description": "Complete leave record object including leave_id, employee_id, leave_type, start_date, end_date, status, and notes."
                        }
                    },
                    "required": ["leave"],
                    "additionalProperties": False
                }
            }
        }
