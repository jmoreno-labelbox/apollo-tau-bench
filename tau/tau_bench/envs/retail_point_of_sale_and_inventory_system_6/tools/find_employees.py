from tau_bench.envs.tool import Tool
import json
from collections import OrderedDict, defaultdict
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class find_employees(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        employee_id: str = None,
        phone_number: str = None,
        membership_level: str = None,
        birthdate: str = None,
        opt_in_marketing: bool = None,
        status: str = None,
        role: str = None,
        store_id: str = None,
        name: str = None,
        email: str = None,
        address: str = None,
    ) -> str:
        employees = data.get("employees", {}).values()

        # If a customer id is provided, it will take precedence over all other criteria

        # These columns will match precisely with the provided value
        exact_match_cols = [
            "phone_number",
            "membership_level",
            "birthdate",
            "opt_in_marketing",
            "status",
            "role",
            "store_id",
        ]
        exact_match_values = {
            "phone_number": phone_number,
            "membership_level": membership_level,
            "birthdate": birthdate,
            "opt_in_marketing": opt_in_marketing,
            "status": status,
            "role": role,
            "store_id": store_id,
        }

        # These columns will match as long as the database field includes the provided value
        approximate_match_cols = ["name", "email", "address"]
        approximate_match_values = {
            "name": name,
            "email": email,
            "address": address,
        }

        matches = []
        for employee in employees.values():
            # customer_id is prioritized
            if (employee_id is not None) and (employee["employee_id"] == employee_id):
                payload = employee
                out = json.dumps(payload, indent=2)
                return out

            # Add to the return list if all provided criteria align
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
        payload = matches
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindEmployees",
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
