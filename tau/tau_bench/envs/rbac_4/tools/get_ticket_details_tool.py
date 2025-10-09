from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetTicketDetailsTool(Tool):
    """Get a HubSpot ticket using ticket_id (read-only, predictable)."""

    @staticmethod
    def invoke(data: dict[str, Any], ticket_id: str = None) -> str:
        tickets = data.get("hubspot_tickets", {}).values()
        if not isinstance(tickets, list):
            payload = {"error": "hubspot_tickets must be a list"}
            out = json.dumps(payload, indent=2)
            return out

        if not isinstance(ticket_id, str) or not ticket_id.strip():
            payload = {"error": "ticket_id must be a non-empty string"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        for t in tickets.values():
            if t.get("ticket_id") == ticket_id:
                payload = t
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"ticket_id {ticket_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetTicketDetails",
                "description": "Retrieve details of a HubSpot ticket by ticket_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"ticket_id": {"type": "string"}},
                    "required": ["ticket_id"],
                },
            },
        }
