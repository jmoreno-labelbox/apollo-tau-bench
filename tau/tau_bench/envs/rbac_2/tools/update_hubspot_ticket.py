# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateHubspotTicket(Tool):
    """ Updates an existing HubSpot ticket. """

    @staticmethod
    def invoke(data: Dict[str, Any], ticket_id, timestamp) -> str:
        try:
            hubspot_tickets = data.get('hubspot_tickets', [])
        except:
            hubspot_tickets = []

        ticket_to_update = None
        for ticket in hubspot_tickets:
            if ticket.get("ticket_id") == ticket_id:
                for key, value in kwargs.items():
                    if key in ticket:
                        ticket[key] = value
                ticket["updated_at"] = timestamp # Continuously refresh the timestamp.
                ticket_to_update = ticket
                break

        if not ticket_to_update:
            return json.dumps({"error": f"HubSpot ticket with ID '{ticket_id}' not found."})

        data['hubspot_tickets'] = hubspot_tickets
        return json.dumps({
            "message": "HubSpot ticket updated successfully.",
            "ticket_details": ticket_to_update
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_hubspot_ticket",
                "description": "Updates an existing HubSpot ticket's status, description, or other fields.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ticket_id": {"type": "string", "description": "The ID of the ticket to update."},
                        "status": {"type": "string", "description": "The new status for the ticket (e.g., 'CLOSED')."},
                        "description": {"type": "string", "description": "The updated, detailed description of the issue or event."},
                        "closed_at": {"type": "string", "description": "The timestamp when the ticket was closed."},
                        "timestamp": {"type": "string", "description": "The current timestamp for the update record."}
                    },
                    "required": ["ticket_id", "timestamp"]
                }
            }
        }
