# Copyright belongs to Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetHubspotTicketById(Tool):
    """ Get the full details of a specific HubSpot ticket using its ID. """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        ticket_id = kwargs.get("ticket_id")
        try:
            hubspot_tickets = data.get('hubspot_tickets', [])
        except:
            hubspot_tickets = []

        for ticket in hubspot_tickets:
            if ticket.get("ticket_id") == ticket_id:
                return json.dumps(ticket)

        return json.dumps({"error": f"HubSpot ticket with ID '{ticket_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_hubspot_ticket_by_id",
                "description": "Retrieves the full details of a specific HubSpot ticket using its unique ID (e.g., 'TI-053').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ticket_id": {
                            "type": "string",
                            "description": "The unique ID of the HubSpot ticket to retrieve."
                        }
                    },
                    "required": ["ticket_id"]
                }
            }
        }
