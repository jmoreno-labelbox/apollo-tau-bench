from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateTicketStatusTool(Tool):
    """Revise the status of a HubSpot ticket (write operation)."""

    @staticmethod
    def invoke(data: dict[str, Any], ticket_id: str = None, status: str = None, updated_at: str = None) -> str:
        tickets = data.get("hubspot_tickets", [])

        if not isinstance(ticket_id, str):
            payload = {"error": "ticket_id must be provided"}
            out = json.dumps(payload, indent=2)
            return out
        if not isinstance(status, str):
            payload = {"error": "status must be provided"}
            out = json.dumps(payload, indent=2)
            return out

        for t in tickets:
            if t.get("ticket_id") == ticket_id:
                t["status"] = status
                if updated_at:
                    t["updated_at"] = updated_at
                payload = {"success": f"Ticket {ticket_id} updated", "ticket": t}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": f"Ticket {ticket_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateTicketStatus",
                "description": "Update the status of a HubSpot ticket.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ticket_id": {
                            "type": "string",
                            "description": "Unique ID of the ticket",
                        },
                        "status": {
                            "type": "string",
                            "description": "New status of the ticket (e.g., OPEN, CLOSED, IN_PROGRESS)",
                        },
                        "updated_at": {
                            "type": "string",
                            "description": "Optional ISO8601 timestamp of the update",
                        },
                    },
                    "required": ["ticket_id", "status"],
                },
            },
        }
