from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class SummarizeWorkloadRebalance(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], hours_transferred: int = 0, from_employee: str = None, to_employee: str = None) -> str:
        if not all([hours_transferred, from_employee, to_employee]):
            payload = {
                "error": "hours_transferred, from_employee, and to_employee are required"
            }
            out = json.dumps(payload)
            return out
        payload = {
            "workload_balanced": True,
            "rebalanced": True,
            "hours_transferred": hours_transferred,
            "from_employee": from_employee,
            "to_employee": to_employee,
            "status": "completed",
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SummarizeWorkloadRebalance",
                "description": "Generate a summary of workload rebalancing operations",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "hours_transferred": {
                            "type": "number",
                            "description": "Number of hours transferred",
                        },
                        "from_employee": {
                            "type": "string",
                            "description": "Employee ID who had hours reduced",
                        },
                        "to_employee": {
                            "type": "string",
                            "description": "Employee ID who received additional hours",
                        },
                    },
                    "required": ["hours_transferred", "from_employee", "to_employee"],
                },
            },
        }
