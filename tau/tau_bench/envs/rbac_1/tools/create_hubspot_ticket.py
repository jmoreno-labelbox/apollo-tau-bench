from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CreateHubspotTicket(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], subject: str = None, description: str = None, requester_id: int = None, category: str = None, assignee_id: int = None) -> str:
        tickets = data.get("hubspot_tickets", {}).values()
        new_id_num = max((int(t["ticket_id"][3:]) for t in tickets.values()), default=0) + 1
        new_ticket_id = f"TI-{new_id_num:03d}"
        new_ticket = {
            "ticket_id": new_ticket_id,
            "subject": subject,
            "description": description,
            "requester_id": requester_id,
            "category": category,
            "assignee_id": assignee_id,
            "status": "OPEN",
        }
        data["tickets"][ticket_id] = new_ticket
        data["hubspot_tickets"] = tickets
        payload = new_ticket
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateHubspotTicket",
                "description": "Creates a new ticket in HubSpot.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subject": {"type": "string"},
                        "description": {"type": "string"},
                        "requester_id": {"type": "string"},
                        "category": {"type": "string"},
                        "assignee_id": {"type": "string"},
                    },
                    "required": ["subject", "description", "requester_id", "category"],
                },
            },
        }
