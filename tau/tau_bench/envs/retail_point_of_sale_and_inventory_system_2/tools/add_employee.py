# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddEmployee(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], name: str, role: str, store_id: str, email: str, phone_number: str) -> str:
        employees = list(data.get("employees", {}).values())

        if any(e.get("email") == email for e in employees):
            return json.dumps({"error": f"Employee with email {email} already exists."})

        employee_id = f"EMP-{len(employees) + 1001:04d}"

        new_employee = {
            "employee_id": employee_id,
            "name": name,
            "role": role,
            "store_id": store_id,
            "email": email,
            "phone_number": phone_number,
            "hire_date": datetime.now().strftime("%Y-%m-%d"),
            "status": "active"
        }

        employees.append(new_employee)
        data["employees"][employee_id] = new_employee

        return json.dumps(new_employee, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_employee",
                "description": "Add a new employee to the system.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string", "description": "Full name of the employee."},
                        "role": {"type": "string", "description": "Job role of the employee."},
                        "store_id": {"type": "string", "description": "Store ID where the employee works."},
                        "email": {"type": "string", "description": "Email address of the employee."},
                        "phone_number": {"type": "string", "description": "Phone number of the employee."}
                    },
                    "required": ["name", "role", "store_id", "email", "phone_number"]
                }
            }
        }
