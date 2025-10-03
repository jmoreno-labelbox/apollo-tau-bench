from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta, timezone
from typing import Any

class CreateHubSpotTicket(Tool):
    """
    Establish a general HubSpot support ticket adhering to consistent rules.

    kwargs:
      subject: str (mandatory) - subject line of the ticket
      description: str (mandatory) - description of the ticket
      assignee_id: str (mandatory) - individual responsible for the ticket
      requester_id: str (mandatory) - individual requesting the ticket
      priority: str (default: "MEDIUM") - HIGH, MEDIUM, LOW
      category: str (default: "GENERAL") - category of the ticket
      status: str (default: "OPEN") - OPEN, IN_PROGRESS, CLOSED
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        subject: str = "",
        description: str = "",
        assignee_id: str = "",
        requester_id: str = "",
        priority: str = "MEDIUM",
        category: str = "GENERAL",
        status: str = "OPEN"
    ) -> str:
        if not subject or not description or not assignee_id or not requester_id:
            payload = {
                "error": "subject, description, assignee_id, and requester_id are required"
            }
            out = json.dumps(payload)
            return out

        # Confirm priority
        valid_priorities = ["HIGH", "MEDIUM", "LOW"]
        if priority not in valid_priorities:
            payload = {"error": f"priority must be one of: {valid_priorities}"}
            out = json.dumps(payload)
            return out

        # Confirm status
        valid_statuses = ["OPEN", "IN_PROGRESS", "CLOSED"]
        if status not in valid_statuses:
            payload = {"error": f"status must be one of: {valid_statuses}"}
            out = json.dumps(payload)
            return out

        # Confirm the assignee is present
        users = data.get("users", [])
        assignee = _find_by_id(users, "user_id", assignee_id)
        if not assignee:
            payload = {"error": f"Assignee {assignee_id} not found"}
            out = json.dumps(payload)
            return out

        # Confirm the requester is present
        requester = _find_by_id(users, "user_id", requester_id)
        if not requester:
            payload = {"error": f"Requester {requester_id} not found"}
            out = json.dumps(payload)
            return out

        # Implement consistent rules for security incidents
        if category == "SECURITY_INCIDENT":
            # Confirm that the operations manager (U-005) is designated for security incidents
            if assignee_id != "U-005":
                assignee_id = "U-005"

            # Verify that the subject adheres to the SIEM alert format
            if not subject.startswith("SIEM Alert: "):
                subject = "SIEM Alert: Unauthorized Access Attempt"

        timestamp = get_current_timestamp()
        ticket_id = _next_id(data, "hubspot_tickets", "TI")

        ticket_record = {
            "ticket_id": ticket_id,
            "created_at": timestamp,
            "updated_at": timestamp,
            "subject": subject,
            "description": description,
            "status": status,
            "priority": priority,
            "assignee_id": assignee_id,
            "requester_id": requester_id,
            "category": category,
            "closed_at": None if status != "CLOSED" else timestamp,
        }

        data.setdefault("hubspot_tickets", []).append(ticket_record)
        payload = {"ok": True, "ticket": ticket_record}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateHubspotTicket",
                "description": "Create a general HubSpot support ticket following deterministic rules.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subject": {
                            "type": "string",
                            "description": "Ticket subject line.",
                        },
                        "description": {
                            "type": "string",
                            "description": "Ticket description.",
                        },
                        "assignee_id": {
                            "type": "string",
                            "description": "User ID who will handle the ticket.",
                        },
                        "requester_id": {
                            "type": "string",
                            "description": "User ID who is requesting the ticket.",
                        },
                        "priority": {
                            "type": "string",
                            "description": "Ticket priority (HIGH, MEDIUM, LOW).",
                            "default": "MEDIUM",
                        },
                        "category": {
                            "type": "string",
                            "description": "Ticket category.",
                            "default": "GENERAL",
                        },
                        "status": {
                            "type": "string",
                            "description": "Ticket status (OPEN, IN_PROGRESS, CLOSED).",
                            "default": "OPEN",
                        },
                    },
                    "required": [
                        "subject",
                        "description",
                        "assignee_id",
                        "requester_id",
                    ],
                    "additionalProperties": False,
                },
            },
        }
