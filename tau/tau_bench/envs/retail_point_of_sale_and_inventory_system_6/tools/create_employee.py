# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class create_employee(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], timestamp) -> str:
        employees = list(data.get("employees", {}).values())

        # These values are required to be transmitted.
        required_cols = [
            "name",
            "phone_number",
            "email",
            "role",
            "hire_date",
            "store_id",
        ]

        # Default values are provided if none are specified.
        optional_cols = []

        required_values = {k: kwargs.get(k) for k in required_cols}
        optional_values = {}
        optional_values.update({k: kwargs[k] for k in optional_cols if k in kwargs})

        # The function computes these values.
        fill_in = {
            "employee_id": "EMP-1{employee_id:03}".format(
                employee_id=max(
                    [int(x["employee_id"].split("-")[1][1:]) for x in employees]
                )
                + 1
            ),
            "created_at": timestamp,
            "updated_at": timestamp,
            "status": "active",
        }

        # Generate an error if any essential values are absent.
        if any([required_values[k] is None for k in required_values.keys()]):
            return json.dumps(
                {
                    "error": "required values not sent: "
                    + ", ".join(
                        [k for k in required_values if required_values[k] is None]
                    )
                },
                indent=2,
            )

        # This is the sequence of items stored in the database.
        # Although dictionaries lack order, maintaining a consistent item sequence can simplify validation.
        col_order = [
            "employee_id",
            "name",
            "role",
            "phone_number",
            "email",
            "store_id",
            "hire_date",
            "status",
        ]

        # Sort the items.
        row = required_values | optional_values | fill_in
        row_final = OrderedDict()
        for k in col_order:
            row_final[k] = row[k]

        # Insert into the database.
        employees.append(json.dumps(row_final, indent=2))

        # Retrieve the complete row for reference.
        return json.dumps(row_final, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_employee",
                "description": "Creates a new employee record",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "timestamp": {
                            "type": "string",
                            "description": "The current timestamp. Used for database timestamp rows",
                        },
                        "name": {
                            "type": "string",
                            "description": "The employee's name",
                        },
                        "role": {"type": "string", "description": "The employee's job"},
                        "phone_number": {
                            "type": "string",
                            "description": "The employee's phone number",
                        },
                        "email": {
                            "type": "string",
                            "description": "The employee's email",
                        },
                        "store_id": {
                            "type": "string",
                            "description": "The store_id where the employee works",
                        },
                        "hire_date": {
                            "type": "string",
                            "description": "The employee's hiredate. YYYY-MM-DD",
                        },
                    },
                },
            },
        }
