from tau_bench.envs.tool import Tool
import json
from collections import OrderedDict, defaultdict
from typing import Any

class update_employee(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        employee_id: str = None,
        timestamp: str = None,
        name: str = None,
        phone_number: str = None,
        email: str = None,
        hire_date: str = None,
        status: str = None,
        role: str = None
    ) -> str:
        employees = data.get("employees", [])

        # These parameters are essential for updates
        row_id = employee_id
        timestamp = timestamp

        if (row_id is None) or (timestamp is None):
            payload = {"error": "employee_id and timestamp must be sent"}
            out = json.dumps(payload)
            return out

        # These parameters are being submitted for the update
        updatable_cols = [
            "name",
            "phone_number",
            "email",
            "hire_date",
            "status",
            "role",
        ]
        updating_values = {
            "name": name,
            "phone_number": phone_number,
            "email": email,
            "hire_date": hire_date,
            "status": status,
            "role": role
        }

        for employee in employees:
            if employee["employee_id"] == row_id:
                for col, value in updating_values.items():
                    # Revise any provided values
                    if value is not None:
                        employee[col] = value

                employee["updated_at"] = timestamp
                payload = employee
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": "no matching records found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateEmployee",
                "description": "Creates a new employee record",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "timestamp": {
                            "type": "string",
                            "description": "The current timestamp. Used for database timestamp rows",
                        },
                        "customer_id": {
                            "type": "string",
                            "description": "REQUIRED. The id of the customer to update",
                        },
                        "name": {
                            "type": "string",
                            "description": "The customer's name",
                        },
                        "phone_number": {
                            "type": "string",
                            "description": "The customer's phone number",
                        },
                        "email": {
                            "type": "string",
                            "description": "The customer's email",
                        },
                        "birthdate": {
                            "type": "string",
                            "description": "The customer's birthdate. YYYY-MM-DD",
                        },
                    },
                },
            },
        }
