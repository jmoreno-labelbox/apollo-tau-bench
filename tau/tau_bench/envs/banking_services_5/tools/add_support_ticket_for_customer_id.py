# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddSupportTicketForCustomerId(Tool):
    """Creates and adds a new support ticket for a customer."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        required_fields = [
            "customer_id", "channel", "priority",
            "category", "target_id", "target_entity",
            "operation"
        ]
        missing = [f for f in required_fields if not kwargs.get(f)]
        if missing:
            return json.dumps(
                {"error": f"Missing required fields: {', '.join(missing)}"},
                indent=2
            )

        priority = kwargs.get("priority", "Medium").capitalize()
        ticket_id = get_next_support_ticket_id()
        now = get_current_timestamp()

        new_ticket = {
            "ticket_id": ticket_id,
            "customer_id": kwargs["customer_id"],
            "priority": priority,
            "channel": kwargs["channel"],
            "category": kwargs["category"],
            "target_id": kwargs["target_id"],
            "target_entity": kwargs["target_entity"],
            "operation": kwargs["operation"],
            "parameters": kwargs.get("parameters", {}),
            "status": "Open",
            "created_at": now,
            "last_updated": now
        }

        data.setdefault("support_tickets", []).append(new_ticket)
        return json.dumps(new_ticket, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_support_ticket_for_customer_id",
                "description": "Adds a new support ticket for the given customer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "ID of the customer creating the support ticket"
                        },
                        "priority": {
                            "type": "string",
                            "description": "Priority of the ticket (e.g., Low, Medium, High); defaults to Medium"
                        },
                        "channel": {
                            "type": "string",
                            "description": "Channel via which the ticket was created (e.g., Phone, Email, Web Portal)"
                        },
                        "category": {
                            "type": "string",
                            "description": "Category of the support issue (e.g., Transaction, Loan, Account, Security)"
                        },
                        "target_id": {
                            "type": "string",
                            "description": "ID of the entity being affected (e.g., transaction ID, loan ID)"
                        },
                        "target_entity": {
                            "type": "string",
                            "description": "Type of entity affected (e.g., Transaction, Account, Loan)"
                        },
                        "operation": {
                            "type": "string",
                            "description": "Requested operation (e.g., Update, Cancel, Refund)"
                        },
                        "parameters": {
                            "type": "object",
                            "description": "Additional parameters for the operation (e.g., fields to update, new values)"
                        }
                    },
                    "required": [
                        "customer_id", "channel", "category", "priority",
                        "target_id", "target_entity", "operation"
                    ]
                }
            }
        }
