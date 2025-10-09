from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any

class GetHubspotTicketById(Tool):
    """Retrieve complete details of a specific HubSpot ticket by its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], ticket_id: str = None) -> str:
        try:
            hubspot_tickets = data.get("hubspot_tickets", [])
        except:
            hubspot_tickets = []

        for ticket in hubspot_tickets:
            if ticket.get("ticket_id") == ticket_id:
                payload = ticket
                out = json.dumps(payload)
                return out
        payload = {"error": f"HubSpot ticket with ID '{ticket_id}' not found."}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetHubspotTicketById",
                "description": "Retrieves the full details of a specific HubSpot ticket using its unique ID (e.g., 'TI-053').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ticket_id": {
                            "type": "string",
                            "description": "The unique ID of the HubSpot ticket to retrieve.",
                        }
                    },
                    "required": ["ticket_id"],
                },
            },
        }
