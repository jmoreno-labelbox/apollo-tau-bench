from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateHubspotTicket(Tool):
    """Modifies an existing HubSpot ticket."""

    @staticmethod
    def invoke(data: dict[str, Any], ticket_id: str = None, timestamp: str = None, status: str = None, priority: str = None,
        closed_at: Any = None,
        description: Any = None,
    ) -> str:
        try:
            hubspot_tickets = data.get("hubspot_tickets", [])
        except:
            hubspot_tickets = []

        ticket_to_update = None
        for ticket in hubspot_tickets:
            if ticket.get("ticket_id") == ticket_id:
                if status is not None:
                    ticket["status"] = status
                if priority is not None:
                    ticket["priority"] = priority
                ticket["updated_at"] = timestamp
                ticket_to_update = ticket
                break

        if not ticket_to_update:
            payload = {"error": f"HubSpot ticket with ID '{ticket_id}' not found."}
            out = json.dumps(payload)
            return out

        data["hubspot_tickets"] = hubspot_tickets
        payload = {
            "message": "HubSpot ticket updated successfully.",
            "ticket_details": ticket_to_update,
        }
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateHubspotTicket",
                "description": "Updates an existing HubSpot ticket's status, description, or other fields.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ticket_id": {
                            "type": "string",
                            "description": "The ID of the ticket to update.",
                        },
                        "status": {
                            "type": "string",
                            "description": "The new status for the ticket (e.g., 'CLOSED').",
                        },
                        "description": {
                            "type": "string",
                            "description": "The updated, detailed description of the issue or event.",
                        },
                        "closed_at": {
                            "type": "string",
                            "description": "The timestamp when the ticket was closed.",
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "The current timestamp for the update record.",
                        },
                    },
                    "required": ["ticket_id", "timestamp"],
                },
            },
        }
