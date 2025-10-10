# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetEmployeeAllocations(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        employee_id = kwargs.get("employee_id")
        if not employee_id:
            return json.dumps({"error": "employee_id is required"})

        allocations = data.get("allocations", [])
        employee_allocations = [
            alloc
            for alloc in allocations
            if alloc.get("employee_id") == employee_id
            and alloc.get("status") == "active"
        ]

        return json.dumps(employee_allocations, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_employee_allocations",
                "description": "Get all active allocations for a specific employee",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The employee ID",
                        }
                    },
                    "required": ["employee_id"],
                },
            },
        }
