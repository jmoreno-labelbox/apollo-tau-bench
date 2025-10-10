# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class list_leave_records(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id: str) -> str:
        leave_records = data.get("leave_records", [])
        hits = [lr for lr in leave_records if lr.get("employee_id") == employee_id]
        return json.dumps({"count": len(hits), "results": hits}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_leave_records",
                "description": "Return all leave records for a given employee_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "Unique ID of the employee whose leave records are requested",
                        }
                    },
                    "required": ["employee_id"],
                    "additionalProperties": False,
                },
            },
        }
