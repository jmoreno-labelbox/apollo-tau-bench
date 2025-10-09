from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateHubspotTicketAssignee(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], ticket_id: str = None, new_assignee_id: str = None) -> str:
        for ticket in data.get("hubspot_tickets", {}).values():
            if ticket.get("ticket_id") == ticket_id:
                ticket["assignee_id"] = new_assignee_id
                ticket["updated_at"] = NOW.strftime(DT_STR_FORMAT)
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
                "name": "UpdateHubspotTicketAssignee",
                "description": "Updates the assignee of an existing HubSpot ticket.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ticket_id": {
                            "type": "string",
                            "description": "The ID of the ticket to update.",
                        },
                        "new_assignee_id": {
                            "type": "string",
                            "description": "The user_id of the new assignee.",
                        },
                    },
                    "required": ["ticket_id", "new_assignee_id"],
                },
            },
        }
