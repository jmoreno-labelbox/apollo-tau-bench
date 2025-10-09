from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetHubspotTicketsByAssignee(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], assignee_id: str = None) -> str:
        matching_tickets = [
            ticket
            for ticket in data.get("hubspot_tickets", {}).values()
            if ticket.get("assignee_id") == assignee_id
        ]
        payload = {"tickets": matching_tickets}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetHubspotTicketsByAssignee",
                "description": "Retrieves a list of HubSpot tickets based on the assignee's user ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "assignee_id": {
                            "type": "string",
                            "description": "The user_id of the person to whom the tickets are assigned.",
                        }
                    },
                    "required": ["assignee_id"],
                },
            },
        }
