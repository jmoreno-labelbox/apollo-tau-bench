# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class create_employee_from_offer_letter(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        offer_doc_id = kwargs.get("offer_doc_id")
        employee_id = kwargs.get("employee_id")
        if not offer_doc_id or not employee_id:
            return json.dumps(
                {"error": "offer_doc_id and employee_id are required"}, indent=2
            )
        if find_employee(list(data.get("employees", {}).values()), employee_id):
            return json.dumps(
                {"error": f"employee_id {employee_id} already exists"}, indent=2
            )

        new_employee = {
            "employee_id": employee_id,
            "first_name": "New",
            "last_name": "Hire",
            "status": "Active",
            "notes": f"Created from offer doc {offer_doc_id}",
        }
        list(data.get("employees", {}).values()).append(new_employee)
        return json.dumps(
            {
                "success": f"Employee {employee_id} created from offer letter {offer_doc_id}"
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_employee_from_offer_letter",
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
