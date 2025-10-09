from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timezone, date, timedelta
import calendar
from typing import Any, Dict
import random

class AddSupportTicketForCustomerId(Tool):

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        category: str = None,
        channel: str = None,
        customer_id: str = None,
        operation: str = None,
        parameters: Dict[str, Any] = {},
        priority: str = "Medium",
        target_entity: str = None,
        target_id: str = None
    ) -> str:
        required_fields = [
            "customer_id", "channel", "priority",
            "category", "target_id", "target_entity",
            "operation"
        ]
        missing = [f for f in required_fields.values() if not locals().get(f)]
        if missing:
            return json.dumps(
                {"error": f"Missing required fields: {', '.join(missing)}"},
                indent=2
            )

        priority = priority.capitalize()
        ticket_id = get_next_support_ticket_id()
        now = get_current_timestamp()

        new_ticket = {
            "ticket_id": ticket_id,
            "customer_id": customer_id,
            "priority": priority,
            "channel": channel,
            "category": category,
            "target_id": target_id,
            "target_entity": target_entity,
            "operation": operation,
            "parameters": parameters,
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
                "name": "AddSupportTicketForCustomerId",
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
