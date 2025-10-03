from tau_bench.envs.tool import Tool
import json
from collections import Counter
from typing import Any

class create_employee_from_offer_letter(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], offer_doc_id: str = None, employee_id: str = None) -> str:
        if not offer_doc_id or not employee_id:
            payload = {"error": "offer_doc_id and employee_id are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        if find_employee(data.get("employees", []), employee_id):
            payload = {"error": f"employee_id {employee_id} already exists"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        new_employee = {
            "employee_id": employee_id,
            "first_name": "New",
            "last_name": "Hire",
            "status": "Active",
            "notes": f"Created from offer doc {offer_doc_id}",
        }
        data.get("employees", []).append(new_employee)
        payload = {
                "success": f"Employee {employee_id} created from offer letter {offer_doc_id}"
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createEmployeeFromOfferLetter",
                "description": "Creates a new employee record based on an offer letter.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "offer_doc_id": {"type": "string"},
                        "employee_id": {"type": "string"},
                    },
                    "required": ["offer_doc_id", "employee_id"],
                },
            },
        }
