from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CreateHubspotTicketTool(Tool):
    """Initiate a new HubSpot ticket associated with RBAC or SIEM context."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        subject: str = None,
        description: str = None,
        requester_id: str = None,
        assignee_id: str = None,
        category: str = None,
        priority: str = "MEDIUM",
        created_at: str = None
    ) -> str:
        pass
        tickets = data.get("hubspot_tickets", {}).values()

        # Predictable ticket ID
        new_id = f"TI-{len(tickets) + 1:03d}"
        fixed_time = "2025-08-11 12:00:00+00:00"

        tickets.append(
            {
                "ticket_id": new_id,
                "created_at": fixed_time,
                "updated_at": fixed_time,
                "subject": subject,
                "description": description,
                "status": "OPEN",
                "priority": priority,
                "assignee_id": assignee_id,
                "requester_id": requester_id,
                "category": category,
                "closed_at": None,
            }
        )
        payload = {"success": f"Ticket {new_id} created"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateHubspotTicket",
                "description": "Create a HubSpot ticket and associate it with RBAC or SIEM events.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subject": {"type": "string"},
                        "description": {"type": "string"},
                        "requester_id": {"type": "string"},
                        "assignee_id": {"type": "string"},
                        "category": {"type": "string"},
                        "priority": {"type": "string"},
                    },
                    "required": [
                        "subject",
                        "description",
                        "requester_id",
                        "assignee_id",
                        "category",
                    ],
                },
            },
        }
