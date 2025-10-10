# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AutoClassifySupportTicketPriorityTool(Tool):
    """
    Tool that uses keyword-based logic to automatically classify a support ticket's priority.

    It analyzes the ticket description text for urgency signals (e.g., "urgent", "can't access",
    "error") and assigns a priority level (Low, Medium, High).

    Methods:
        invoke(data: Dict[str, Any], **kwargs) -> str:
            Classifies the priority of a support ticket.

        get_info() -> Dict[str, Any]:
            Returns metadata about required inputs (ticket_text) and output (priority classification).
    """

    @staticmethod
    def invoke(data: Dict[str, Any], customer_id, message, ticket_id) -> str:

        if not customer_id or not message or not ticket_id:
            return json.dumps(
                {"error": "customer_id, message, and ticket_id are required"},
                indent=2
            )

        tickets = list(data.get("support_tickets", {}).values())
        for t in tickets:
            if t["ticket_id"] == ticket_id:
                priority = (
                    "High"
                    if any(term in message.lower() for term in ["urgent", "immediately", "lost", "unauthorized"])
                    else "Normal"
                )
                t["priority"] = priority
                return json.dumps({
                    "ticket_id": ticket_id,
                    "priority": priority,
                    "status": "updated"
                }, indent=2)

        return json.dumps({"error": f"Ticket '{ticket_id}' not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "auto_classify_support_ticket_priority",
                "description": "Automatically classify the priority of a support ticket based on content.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Customer ID"},
                        "message": {
                            "type": "string",
                            "description": "Support message content",
                        },
                    },
                    "required": ["customer_id", "message"],
                },
            },
        }
