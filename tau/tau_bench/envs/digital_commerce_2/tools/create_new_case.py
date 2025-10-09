from tau_bench.envs.tool import Tool
import json
from typing import Any
from decimal import ROUND_HALF_UP, Decimal



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CreateNewCase(Tool):

    @staticmethod
    def invoke(
        data: dict[str, Any],
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

        #1) Confirm
        if not contact_id or not account_id or not subject or not priority:
            payload = {
                    "error": "Missing required fields: contact_id, account_id, subject, priority"
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        cases = data.get("cases", {}).values()
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
        data["cases"][case_id] = new_case
        payload = new_case
        out = json.dumps(payload, indent=2)
        return out
         

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateNewCase",
                "description": "Create a new case and append it to the cases DB.",
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
                        "subject": {
                            "type": "string",
                            "description": "Subject line for the case.",
                        },
                        "priority": {
                            "type": "string",
                            "description": "Priority level (e.g., Low, Medium, High).",
                        },
                    },
                    "required": ["contact_id", "account_id", "subject", "priority"],
                },
            },
        }
