# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _find_by_id(items: List[Dict[str, Any]], key: str, value: str) -> Optional[Dict[str, Any]]:
    for it in items or []:
        if it.get(key) == value:
            return it
    return None

class UpdateHubSpotTicket(Tool):
    """
    Update an existing HubSpot ticket's fields and timestamps.

    kwargs:
      ticket_id: str (required)
      status: str (optional) - OPEN, IN_PROGRESS, CLOSED
      assignee_id: str (optional)
      priority: str (optional) - HIGH, MEDIUM, LOW
      subject: str (optional)
      description: str (optional)
      updated_at: str ISO (optional; defaults to now)
    """
    @staticmethod
    def invoke(data: Dict[str, Any], assignee_id, description, priority, status, subject, updated_at, ticket_id = "") -> str:
        updated_at = updated_at or get_current_timestamp()

        if not ticket_id:
            return json.dumps({"error": "ticket_id is required"})

        tickets = data.get("hubspot_tickets", [])
        idx = None
        for i, t in enumerate(tickets):
            if t.get("ticket_id") == ticket_id:
                idx = i
                break

        if idx is None:
            return json.dumps({"error": f"ticket_id {ticket_id} not found"})

        # Verify enum values
        if status is not None and status not in ["OPEN", "IN_PROGRESS", "CLOSED"]:
            return json.dumps({"error": "status must be one of: ['OPEN','IN_PROGRESS','CLOSED']"})
        if priority is not None and priority not in ["HIGH", "MEDIUM", "LOW"]:
            return json.dumps({"error": "priority must be one of: ['HIGH','MEDIUM','LOW']"})

        # Verify the assignee.
        if assignee_id is not None:
            if not _find_by_id(list(data.get("users", {}).values()), "user_id", assignee_id):
                return json.dumps({"error": f"assignee_id {assignee_id} not found"})

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
            # Handle closed_at according to the status.
            if status == "CLOSED":
                updated["closed_at"] = updated_at
            else:
                updated["closed_at"] = None

        updated["updated_at"] = updated_at

        data["hubspot_tickets"][idx] = updated
        return json.dumps({"ok": True, "ticket": updated})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_hubspot_ticket",
                "description": "Update an existing HubSpot ticket's fields and timestamps.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ticket_id": {"type": "string", "description": "Ticket id (TI-###)."},
                        "status": {"type": "string", "description": "New status (OPEN, IN_PROGRESS, CLOSED)."},
                        "assignee_id": {"type": "string", "description": "New assignee user_id."},
                        "priority": {"type": "string", "description": "Priority (HIGH, MEDIUM, LOW)."},
                        "subject": {"type": "string", "description": "Updated subject."},
                        "description": {"type": "string", "description": "Updated description."},
                        "updated_at": {"type": "string", "description": "ISO timestamp for update (optional)."}
                    },
                    "required": ["ticket_id"],
                    "additionalProperties": False
                }
            }
        }