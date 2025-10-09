from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateHubSpotTicket(Tool):
    """
    Modify the fields and timestamps of an existing HubSpot ticket.

    kwargs:
      ticket_id: str (mandatory)
      status: str (optional) - OPEN, IN_PROGRESS, CLOSED
      assignee_id: str (optional)
      priority: str (optional) - HIGH, MEDIUM, LOW
      subject: str (optional)
      description: str (optional)
      updated_at: str ISO (optional; defaults to now)
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        ticket_id: str = "",
        status: str = None,
        assignee_id: str = None,
        priority: str = None,
        subject: str = None,
        description: str = None,
        updated_at: str = None
    ) -> str:
        if updated_at is None:
            updated_at = get_current_timestamp()

        if not ticket_id:
            payload = {"error": "ticket_id is required"}
            out = json.dumps(payload)
            return out

        tickets = data.get("hubspot_tickets", {}).values()
        idx = None
        for i, t in enumerate(tickets.values()):
            if t.get("ticket_id") == ticket_id:
                idx = i
                break

        if idx is None:
            payload = {"error": f"ticket_id {ticket_id} not found"}
            out = json.dumps(payload)
            return out

        # Confirm enumerations
        if status is not None and status not in ["OPEN", "IN_PROGRESS", "CLOSED"]:
            payload = {"error": "status must be one of: ['OPEN','IN_PROGRESS','CLOSED']"}
            out = json.dumps(payload)
            return out
        if priority is not None and priority not in ["HIGH", "MEDIUM", "LOW"]:
            payload = {"error": "priority must be one of: ['HIGH','MEDIUM','LOW']"}
            out = json.dumps(payload)
            return out

        # Confirm the assignee
        if assignee_id is not None:
            if not _find_by_id(data.get("users", {}).values(), "user_id", assignee_id):
                payload = {"error": f"assignee_id {assignee_id} not found"}
                out = json.dumps(payload)
                return out

        updated = dict(tickets[idx])
        if subject is not None:
            updated["subject"] = subject
        if description is not None:
            updated["description"] = description
        if priority is not None:
            updated["priority"] = priority
        if assignee_id is not None:
            updated["assignee_id"] = assignee_id
        if status is not None:
            updated["status"] = status
            # Handle closed_at according to the status
            if status == "CLOSED":
                updated["closed_at"] = updated_at
            else:
                updated["closed_at"] = None

        updated["updated_at"] = updated_at

        data["hubspot_tickets"][idx] = updated
        payload = {"ok": True, "ticket": updated}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateHubspotTicket",
                "description": "Update an existing HubSpot ticket's fields and timestamps.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ticket_id": {
                            "type": "string",
                            "description": "Ticket id (TI-###).",
                        },
                        "status": {
                            "type": "string",
                            "description": "New status (OPEN, IN_PROGRESS, CLOSED).",
                        },
                        "assignee_id": {
                            "type": "string",
                            "description": "New assignee user_id.",
                        },
                        "priority": {
                            "type": "string",
                            "description": "Priority (HIGH, MEDIUM, LOW).",
                        },
                        "subject": {
                            "type": "string",
                            "description": "Updated subject.",
                        },
                        "description": {
                            "type": "string",
                            "description": "Updated description.",
                        },
                        "updated_at": {
                            "type": "string",
                            "description": "ISO timestamp for update (optional).",
                        },
                    },
                    "required": ["ticket_id"],
                    "additionalProperties": False,
                },
            },
        }
