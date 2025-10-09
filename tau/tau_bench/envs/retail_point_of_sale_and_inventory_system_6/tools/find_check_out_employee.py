from tau_bench.envs.tool import Tool
import json
from collections import OrderedDict, defaultdict
from typing import Any

class FindCheckOutEmployee(Tool):
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
    def invoke(data: dict[str, Any], store_id: str, ignore_ids: list[str] = None) -> str:
        employees = data.get("employees", [])

        if ignore_ids is None:
            ignore_ids = []
        elif isinstance(ignore_ids, str):
            ignore_ids = json.loads(ignore_ids)

        # Inefficient nested loop, but it should work well given the small number of roles
        for role in FindCheckOutEmployee.priority:
            for employee in employees:
                if (
                    (employee["store_id"] == store_id)
                    and (employee["role"] == role)
                    and (employee["employee_id"] not in ignore_ids)
                ):
                    payload = employee
                    out = json.dumps(payload, indent=2)
                    return out
        payload = {"error": "no suitable employee found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindCheckOutEmployee",
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
