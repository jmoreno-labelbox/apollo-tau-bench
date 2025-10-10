# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ChangeSupportTicketStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get("customer_id")
        ticket_id   = kwargs.get("ticket_id")
        new_status  = kwargs.get("new_status", "").strip()
        if not all([customer_id, ticket_id, new_status]):
            return json.dumps({"error": "customer_id, ticket_id and new_status are required."}, indent=2)

        tickets = list(data.get("support_tickets", {}).values())
        for ticket in tickets:
            if (ticket.get("ticket_id") == ticket_id and
                ticket.get("customer_id") == customer_id):
                ticket["status"] = new_status
                return json.dumps(ticket, indent=2)

        return json.dumps({"error": "Support ticket not found for this customer."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "change_support_ticket_status",
                "description": "Updates the status of a support ticket given its ID and customer ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "ID of the customer who owns the ticket"
                        },
                        "ticket_id": {
                            "type": "string",
                            "description": "Identifier of the support ticket to update"
                        },
                        "new_status": {
                            "type": "string",
                            "description": "New status value (e.g., 'Resolved' or 'Open')"
                        }
                    },
                    "required": ["customer_id", "ticket_id", "new_status"]
                }
            }
        }
