# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class find_check_out_employee(Tool):
    priority = [
        "Cashier",
        "Customer Service Rep",
        "Sales Associate",
        "Floor Supervisor",
        "Assistant Manager",
        "Store Manager",
        "Inventory Specialist",
        "Department Manager",
    ]

    @staticmethod
    def invoke(data: Dict[str, Any], store_id, ignore_ids = []) -> str:
        employees = list(data.get("employees", {}).values())
        if isinstance(ignore_ids, str):
            ignore_ids = json.loads(ignore_ids)

        # Suboptimal nested loop, but acceptable given the small number of roles.
        for role in find_check_out_employee.priority:
            for employee in employees:
                if (
                    (employee["store_id"] == store_id)
                    and (employee["role"] == role)
                    and (employee["employee_id"] not in ignore_ids)
                ):
                    return json.dumps(employee, indent=2)

        return json.dumps({"error": "no suitable employee found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_check_out_employee",
                "description": "Gets an employee to process a transaction at a store",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "store_id": {
                            "type": "string",
                            "description": "The store_id to check",
                        },
                        "ignore_ids": {
                            "type": "string",
                            "descrption": "These employee ids will be ignored when searching. Useful if someone is not available",
                        },
                    },
                },
            },
        }
