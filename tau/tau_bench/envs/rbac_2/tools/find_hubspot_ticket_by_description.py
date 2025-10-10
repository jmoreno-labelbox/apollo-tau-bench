# © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindHubspotTicketByDescription(Tool):
    """Finds a HubSpot ticket by searching for a keyword in its description field."""

    @staticmethod
    def invoke(data: Dict[str, Any], keyword) -> str:
        try:
            tickets = data.get('hubspot_tickets', [])
        except (KeyError, json.JSONDecodeError):
            tickets = []

        for ticket in tickets:
            description = ticket.get("description", "")
            if description is None:
                description = ""
            
            if keyword in description:
                return json.dumps(ticket)

        return json.dumps({"error": f"No HubSpot ticket found with keyword '{keyword}' in its description."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_hubspot_ticket_by_description",
                "description": "Finds a HubSpot ticket by searching for a specific keyword within its description text.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "keyword": {
                            "type": "string",
                            "description": "The keyword or string to search for in the ticket descriptions (e.g., an alert ID like 'ALRT-001')."
                        }
                    },
                    "required": ["keyword"]
                }
            }
        }
