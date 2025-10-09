from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class AddEmployee(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        name: str,
        role: str,
        store_id: str,
        email: str,
        phone_number: str
    ) -> str:
        employees = data.get("employees", {}).values()

        if any(e.get("email") == email for e in employees.values()):
            payload = {"error": f"Employee with email {email} already exists."}
            out = json.dumps(payload)
            return out

        employee_id = f"EMP-{len(employees) + 1001:04d}"

        new_employee = {
            "employee_id": employee_id,
            "name": name,
            "role": role,
            "store_id": store_id,
            "email": email,
            "phone_number": phone_number,
            "hire_date": datetime.now().strftime("%Y-%m-%d"),
            "status": "active",
        }

        data["employees"][employee_id] = new_employee
        data["employees"] = employees
        payload = new_employee
        out = json.dumps(payload, indent=2)
        return out
        pass
        employees = data.get("employees", {}).values()

        if any(e.get("email") == email for e in employees.values()):
            payload = {"error": f"Employee with email {email} already exists."}
            out = json.dumps(payload)
            return out

        employee_id = f"EMP-{len(employees) + 1001:04d}"

        new_employee = {
            "employee_id": employee_id,
            "name": name,
            "role": role,
            "store_id": store_id,
            "email": email,
            "phone_number": phone_number,
            "hire_date": datetime.now().strftime("%Y-%m-%d"),
            "status": "active",
        }

        data["employees"][employee_id] = new_employee
        data["employees"] = employees
        payload = new_employee
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddEmployee",
                "description": "Add a new employee to the system.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Full name of the employee.",
                        },
                        "role": {
                            "type": "string",
                            "description": "Job role of the employee.",
                        },
                        "store_id": {
                            "type": "string",
                            "description": "Store ID where the employee works.",
                        },
                        "email": {
                            "type": "string",
                            "description": "Email address of the employee.",
                        },
                        "phone_number": {
                            "type": "string",
                            "description": "Phone number of the employee.",
                        },
                    },
                    "required": ["name", "role", "store_id", "email", "phone_number"],
                },
            },
        }
