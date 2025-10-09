from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetHubspotTicketsByRequester(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], requester_id: str = None) -> str:
        matching_tickets = [
            ticket
            for ticket in data.get("hubspot_tickets", [])
            if ticket.get("requester_id") == requester_id
        ]
        payload = {"tickets": matching_tickets}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetHubspotTicketsByRequester",
                "description": "Retrieves a list of HubSpot tickets based on the requester's user ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "requester_id": {
                            "type": "string",
                            "description": "The user_id of the person who requested the tickets.",
                        }
                    },
                    "required": ["requester_id"],
                },
            },
        }
