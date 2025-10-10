# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SubmitSupportTicketTool(Tool):
    """
    Tool to create a new customer support ticket.

    This tool takes information such as the customer ID, ticket category, priority level,
    communication channel, and a structured request description. It generates a new ticket ID
    and logs the support request for further processing.

    Methods:
        invoke(data: Dict[str, Any], **kwargs) -> str:
            Submits the ticket and returns the new ticket ID and status.

        get_info() -> Dict[str, Any]:
            Explains tool usage, required fields, and return format.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get("customer_id")
        category = kwargs.get("category")
        priority = kwargs.get("priority")
        channel = kwargs.get("channel")
        request_details = kwargs.get("request_details")
        ticket_id = kwargs.get("ticket_id", f"ticket_{generate_unique_id()}")
        if "ticket_id" in kwargs:
            ticket_id = kwargs["ticket_id"]
        else:
            ticket_id = f"ticket_{generate_unique_id()}"

        if not all([customer_id, category, priority, channel, request_details]):
            return json.dumps(
                {
                    "error": "Missing required parameters: customer_id, category, priority, channel, and request_details"
                },
                indent=2,
            )

        tickets = load_json("support_tickets.json")

        new_ticket = {
            "ticket_id": ticket_id,
            "customer_id": customer_id,
            "category": category,
            "priority": priority,
            "channel": channel,
            "request_details": request_details,
            "status": "Open",
            "created_at": get_current_timestamp(),
        }
        tickets.append(new_ticket)

        return json.dumps({"ticket_id": ticket_id, "status": "Open"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "submit_support_ticket",
                "description": "Create a new support ticket for a customer including structured request metadata.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Customer ID"},
                        "category": {
                            "type": "string",
                            "description": "Support issue category (e.g., Audit, Security)",
                        },
                        "priority": {
                            "type": "string",
                            "description": "Support priority (e.g., High, Medium, Low)",
                        },
                        "channel": {
                            "type": "string",
                            "description": "Channel used to submit the ticket (e.g., Web, Mobile App)",
                        },
                        "request_details": {
                            "type": "object",
                            "description": "Structured data describing the target of the support request",
                            "properties": {
                                "target_entity": {
                                    "type": "string",
                                    "description": "Entity being modified (e.g., Customer, Account)",
                                },
                                "target_id": {
                                    "type": "string",
                                    "description": "ID of the entity being affected",
                                },
                                "operation": {
                                    "type": "string",
                                    "description": "Operation requested (e.g., UPDATE, REVIEW, CLOSE)",
                                },
                                "parameters": {
                                    "type": "object",
                                    "description": "Additional parameters related to the request",
                                },
                            },
                            "required": [
                                "target_entity",
                                "target_id",
                                "operation",
                                "parameters",
                            ],
                        },
                    },
                    "required": [
                        "customer_id",
                        "category",
                        "priority",
                        "channel",
                        "request_details",
                    ],
                },
            },
        }
