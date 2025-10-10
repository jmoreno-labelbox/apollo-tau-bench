# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class update_employee(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        employees = list(data.get("employees", {}).values())

        # These parameters are mandatory for updates
        row_id = kwargs.get("employee_id")
        timestamp = kwargs.get("timestamp")

        if (row_id is None) or (timestamp is None):
            return json.dumps({"error": "employee_id and timestamp must be sent"})

        # These are the parameters being sent for update
        updatable_cols = [
            "name",
            "phone_number",
            "email",
            "hire_date",
            "status",
            "role",
        ]
        updating_values = {k: kwargs.get(k) for k in updatable_cols}

        for employee in employees:
            if employee["employee_id"] == row_id:
                for col, value in updating_values.items():
                    # Update any sent values
                    if value is not None:
                        employee[col] = value

                employee["updated_at"] = timestamp

                return json.dumps(employee, indent=2)

        return json.dumps({"error": "no matching records found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_employee",
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
