# Copyright Sierra Technologies

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SummarizeWorkloadRebalance(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        hours_transferred = kwargs.get("hours_transferred", 0)
        from_employee = kwargs.get("from_employee")
        to_employee = kwargs.get("to_employee")

        if not all([hours_transferred, from_employee, to_employee]):
            return json.dumps(
                {
                    "error": "hours_transferred, from_employee, and to_employee are required"
                }
            )

        return json.dumps(
            {
                "workload_balanced": True,
                "rebalanced": True,
                "hours_transferred": hours_transferred,
                "from_employee": from_employee,
                "to_employee": to_employee,
                "status": "completed",
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "summarize_workload_rebalance",
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
