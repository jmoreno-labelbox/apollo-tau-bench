from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta, timezone
from typing import Any

class GetHubSpotTicket(Tool):
    """
    Retrieve HubSpot tickets using ticket_id or filter by SIEM alert ID (found in description),
    status, priority, category, assignee_id, or requester_id.

    kwargs:
      ticket_id: str (optional) - Specific ticket ID to retrieve
      alert_id: str (optional) - SIEM alert ID to match within the description (e.g., ALRT-012)
      status: str (optional) - OPEN, IN_PROGRESS, CLOSED
      priority: str (optional) - HIGH, MEDIUM, LOW
      category: str (optional) - SECURITY_INCIDENT, ACCESS_REQUEST, GENERAL, etc.
      assignee_id: str (optional)
      requester_id: str (optional)
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        ticket_id: str = None,
        alert_id: str = None,
        status: str = None,
        priority: str = None,
        category: str = None,
        assignee_id: str = None,
        requester_id: str = None
    ) -> str:
        tickets = data.get("hubspot_tickets", [])

        # If ticket_id is supplied, return the specific ticket
        if ticket_id:
            t = _find_by_id(tickets, "ticket_id", ticket_id)
            if not t:
                payload = {"error": f"ticket_id {ticket_id} not found"}
                out = json.dumps(payload)
                return out
            payload = {"ok": True, "ticket": t}
            out = json.dumps(payload)
            return out

        # If not, narrow down
        out: list[dict[str, Any]] = []
        for t in tickets:
            if status and t.get("status") != status:
                continue
            if priority and t.get("priority") != priority:
                continue
            if category and t.get("category") != category:
                continue
            if assignee_id and t.get("assignee_id") != assignee_id:
                continue
            if requester_id and t.get("requester_id") != requester_id:
                continue
            if alert_id:
                desc = str(t.get("description", ""))
                if alert_id not in desc:
                    continue
            out.append(t)
        payload = {"ok": True, "tickets": out}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetHubspotTicket",
                "description": "Retrieve HubSpot tickets by ticket_id or filter by SIEM alert ID (in description), status, priority, category, assignee_id, or requester_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ticket_id": {
                            "type": "string",
                            "description": "Specific ticket ID to retrieve (TI-###).",
                        },
                        "alert_id": {
                            "type": "string",
                            "description": "SIEM alert ID to match in description (e.g., ALRT-012).",
                        },
                        "status": {
                            "type": "string",
                            "description": "Filter by status (OPEN, IN_PROGRESS, CLOSED).",
                        },
                        "priority": {
                            "type": "string",
                            "description": "Filter by priority (HIGH, MEDIUM, LOW).",
                        },
                        "category": {
                            "type": "string",
                            "description": "Filter by category (e.g., SECURITY_INCIDENT, ACCESS_REQUEST, GENERAL).",
                        },
                        "assignee_id": {
                            "type": "string",
                            "description": "Filter by assignee user_id.",
                        },
                        "requester_id": {
                            "type": "string",
                            "description": "Filter by requester user_id.",
                        },
                    },
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }
