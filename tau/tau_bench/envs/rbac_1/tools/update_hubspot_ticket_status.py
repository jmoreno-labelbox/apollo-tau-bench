from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateHubspotTicketStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], ticket_id: str = None, status: str = None,
    note: Any = None,
    closed_at: Any = None,
    description: Any = None
    ) -> str:
        for ticket in data.get("hubspot_tickets", []):
            if ticket.get("ticket_id") == ticket_id:
                ticket["status"] = status
                ticket["closed_at"] = NOW.strftime(DT_STR_FORMAT)
                payload = ticket
                out = json.dumps(payload)
                return out
        payload = {"error": "Ticket not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateHubspotTicketStatus",
                "description": "Updates the status of a HubSpot ticket (e.g., OPEN, CLOSED).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ticket_id": {"type": "string"},
                        "status": {"type": "string"},
                        "note": {
                            "type": "string",
                            "description": "An optional note to add when updating the status.",
                        },
                    },
                    "required": ["ticket_id", "status"],
                },
            },
        }
