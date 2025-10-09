from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class FindHubspotTicketByDescription(Tool):
    """Identifies a HubSpot ticket by looking for a keyword in its description field."""

    @staticmethod
    def invoke(data: dict[str, Any], keyword: str = None) -> str:
        try:
            tickets = data.get("hubspot_tickets", [])
        except (KeyError, json.JSONDecodeError):
            tickets = []

        for ticket in tickets:
            description = ticket.get("description", "")
            if description is None:
                description = ""

            if keyword in description:
                payload = ticket
                out = json.dumps(payload)
                return out
        payload = {
            "error": f"No HubSpot ticket found with keyword '{keyword}' in its description."
        }
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindHubspotTicketByDescription",
                "description": "Finds a HubSpot ticket by searching for a specific keyword within its description text.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "keyword": {
                            "type": "string",
                            "description": "The keyword or string to search for in the ticket descriptions (e.g., an alert ID like 'ALRT-001').",
                        }
                    },
                    "required": ["keyword"],
                },
            },
        }
