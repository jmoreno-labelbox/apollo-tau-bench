# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateNewCase(Tool):
    """Create a new case and append it to the cases DB."""

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        contact_id: Any,
        account_id: Any,
        subject: Any,
        priority: Any,
        order_id: Any = None,
    ) -> str:
        contact_id = _idstr(contact_id)
        account_id = _idstr(account_id)
        order_id = _idstr(order_id)
        subject = subject
        priority = priority
        if not contact_id or not account_id or not subject or not priority:
            return json.dumps(
                {"error": "Missing required fields: contact_id, account_id, subject, priority"},
                indent=2,
            )
        cases = data.get("cases", [])
        case_id = get_next_case_id(data)
        new_case = {
            "case_id": case_id,
            "contact_id": contact_id,
            "account_id": account_id,
            "order_id": order_id,
            "subject": subject,
            "status": "New",
            "priority": priority,
        }
        cases.append(new_case)
        return json.dumps(new_case, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_new_case",
                "description": "Create a new case and append it to the cases DB. Default status is 'New'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "contact_id": {
                            "type": "string",
                            "description": "Contact ID related to the case.",
                        },
                        "account_id": {
                            "type": "string",
                            "description": "Account ID related to the case.",
                        },
                        "order_id": {
                            "type": ["string", "null"],
                            "description": "Order ID related to the case, if any.",
                        },
                        "subject": {"type": "string", "description": "Subject line for the case."},
                        "priority": {
                            "type": "string",
                            "description": "Priority level (e.g., Low, Medium, High).",
                        },
                    },
                    "required": ["contact_id", "account_id", "subject", "priority"],
                },
            },
        }
