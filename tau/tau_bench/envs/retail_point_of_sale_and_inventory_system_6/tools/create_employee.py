from tau_bench.envs.tool import Tool
import json
from collections import OrderedDict, defaultdict
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class create_employee(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        timestamp: str,
        name: str = None,
        phone_number: str = None,
        email: str = None,
        role: str = None,
        hire_date: str = None,
        store_id: str = None,
    ) -> str:
        employees = data.get("employees", {}).values()

        # A timestamp is required for database records

        # These values are required to be provided
        required_cols = [
            "name",
            "phone_number",
            "email",
            "role",
            "hire_date",
            "store_id",
        ]

        # Default values will apply if these are not provided
        optional_cols = []

        required_values = {
            "name": name,
            "phone_number": phone_number,
            "email": email,
            "role": role,
            "hire_date": hire_date,
            "store_id": store_id,
        }
        optional_values = {}

        # The function calculates these values
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

        # Raise an error if any required values are missing
        if any([required_values[k] is None for k in required_values.keys()]):
            payload = {
                "error": "required values not sent: "
                + ", ".join(
                    [k for k in required_values.values() if required_values[k] is None]
                )
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        # This represents the order of items in the database
        # While not crucial due to the unordered nature of dictionaries, having items in a consistent order can facilitate validation
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

        # Arrange the items
        row = required_values | optional_values | fill_in
        row_final = OrderedDict()
        for k in col_order:
            row_final[k] = row[k]

        # Insert into the database
        employees.append(json.dumps(row_final, indent=2))
        payload = row_final
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createEmployee",
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
