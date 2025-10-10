# Sierra copyright.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class find_employees(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id) -> str:
        employees = list(data.get("employees", {}).values())

        # These columns will correspond precisely to the provided value.
        exact_match_cols = [
            "phone_number",
            "membership_level",
            "birthdate",
            "opt_in_marketing",
            "status",
            "role",
            "store_id",
        ]
        exact_match_values = {k: kwargs.get(k) for k in exact_match_cols}

        # These columns will be aligned as long as the database field includes the provided value.
        approximate_match_cols = ["name", "email", "address"]
        approximate_match_values = {k: kwargs.get(k) for k in approximate_match_cols}

        matches = []
        for employee in employees:
            # customer_id is prioritized.
            if (employee_id is not None) and (employee["employee_id"] == employee_id):
                return json.dumps(employee, indent=2)

            # If all specified conditions are met, include it in the return list.
            elif all(
                [
                    exact_match_values[k] == employee[k]
                    for k in exact_match_values.keys()
                    if exact_match_values[k] is not None
                ]
            ) and all(
                [
                    approximate_match_values[k].lower() in employee[k].lower()
                    for k in approximate_match_values.keys()
                    if approximate_match_values[k] is not None
                ]
            ):
                matches.append(employee)

        return json.dumps(matches, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_employees",
                "description": "Finds employees matching the sent criteria. Returns an empty list if there are none",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The id of the employee to return. If found, the function will return only the employee matching the employee_id",
                        },
                        "phone_number": {
                            "type": "string",
                            "description": "phone number of the employee. Will do an exact match",
                        },
                        "status": {
                            "type": "string",
                            "description": "status of the employee. Will do an exact match",
                        },
                        "hire_date": {
                            "type": "string",
                            "description": "hire date of the employee. Will do an exact match",
                        },
                        "role": {
                            "type": "string",
                            "description": "job of the employee. Will do an exact match",
                        },
                        "store_id": {
                            "type": "string",
                            "description": "store id where the employee works. Will do an exact match",
                        },
                        "name": {
                            "type": "string",
                            "description": "name of the employee. Will do an approximate match",
                        },
                        "email": {
                            "type": "string",
                            "description": "email of the employee. Will do an approximate match",
                        },
                    },
                },
            },
        }
