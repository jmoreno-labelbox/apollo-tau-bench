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
    """Generate a new ticket in the HubSpot system for monitoring purposes."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        timestamp: str = None,
        subject: str = None,
        description: str = None,
        priority: str = None,
        assignee_id: str = None,
        requester_id: str = None,
        category: str = None
    ) -> str:
        try:
            hubspot_tickets = data.get("hubspot_tickets", {}).values()
        except:
            hubspot_tickets = []

        existing_ids = [
            int(item["ticket_id"].replace("TI-", ""))
            for item in hubspot_tickets.values() if item.get("ticket_id", "").startswith("TI-")
        ]
        next_id_num = max(existing_ids) + 1 if existing_ids else 1
        ticket_id = f"TI-{next_id_num:03d}"

        new_ticket = {
            "ticket_id": ticket_id,
            "created_at": timestamp,
            "updated_at": timestamp,
            "subject": subject,
            "description": description,
            "status": "OPEN",
            "priority": priority,
            "assignee_id": assignee_id,
            "requester_id": requester_id,
            "category": category,
            "closed_at": None,
        }

        hubspot_data["tickets"][ticket_id] = new_ticket
        data["hubspot_tickets"] = hubspot_tickets
        payload = {
            "message": "HubSpot ticket created successfully.",
            "ticket_details": new_ticket,
        }
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateHubspotTicket",
                "description": "Creates a new ticket in the HubSpot system to track an incident or request.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subject": {
                            "type": "string",
                            "description": "The title or subject line of the ticket.",
                        },
                        "description": {
                            "type": "string",
                            "description": "A detailed description of the issue or event.",
                        },
                        "priority": {
                            "type": "string",
                            "description": "The priority level of the ticket (e.g., HIGH, MEDIUM, LOW).",
                        },
                        "assignee_id": {
                            "type": "string",
                            "description": "The user ID of the person the ticket is assigned to.",
                        },
                        "requester_id": {
                            "type": "string",
                            "description": "The user ID of the person who initiated the event or request.",
                        },
                        "category": {
                            "type": "string",
                            "description": "The category of the ticket (e.g., SECURITY_INCIDENT, ACCESS_REQUEST).",
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "The current timestamp for the creation record.",
                        },
                    },
                    "required": [
                        "subject",
                        "description",
                        "priority",
                        "assignee_id",
                        "requester_id",
                        "category",
                        "timestamp",
                    ],
                },
            },
        }
