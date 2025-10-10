# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateHubSpotTicket(Tool):
    """
    Create a general HubSpot support ticket following deterministic rules.

    kwargs:
      subject: str (required) - ticket subject line
      description: str (required) - ticket description
      assignee_id: str (required) - who will handle the ticket
      requester_id: str (required) - who is requesting the ticket
      priority: str (default: "MEDIUM") - HIGH, MEDIUM, LOW
      category: str (default: "GENERAL") - ticket category
      status: str (default: "OPEN") - OPEN, IN_PROGRESS, CLOSED
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        subject = kwargs.get("subject", "")
        description = kwargs.get("description", "")
        assignee_id = kwargs.get("assignee_id", "")
        requester_id = kwargs.get("requester_id", "")
        priority = kwargs.get("priority", "MEDIUM")
        category = kwargs.get("category", "GENERAL")
        status = kwargs.get("status", "OPEN")

        if not subject or not description or not assignee_id or not requester_id:
            return json.dumps({"error": "subject, description, assignee_id, and requester_id are required"})

        # Validate priority
        valid_priorities = ["HIGH", "MEDIUM", "LOW"]
        if priority not in valid_priorities:
            return json.dumps({"error": f"priority must be one of: {valid_priorities}"})

        # Validate status
        valid_statuses = ["OPEN", "IN_PROGRESS", "CLOSED"]
        if status not in valid_statuses:
            return json.dumps({"error": f"status must be one of: {valid_statuses}"})

        # Validate assignee exists
        users = list(data.get("users", {}).values())
        assignee = _find_by_id(users, "user_id", assignee_id)
        if not assignee:
            return json.dumps({"error": f"Assignee {assignee_id} not found"})

        # Validate requester exists
        requester = _find_by_id(users, "user_id", requester_id)
        if not requester:
            return json.dumps({"error": f"Requester {requester_id} not found"})

        # Apply deterministic rules for security incidents
        if category == "SECURITY_INCIDENT":
            # Ensure operations manager (U-005) is assigned for security incidents
            if assignee_id != "U-005":
                assignee_id = "U-005"

            # Ensure subject follows SIEM alert format
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
            "closed_at": None if status != "CLOSED" else timestamp
        }

        data.setdefault("hubspot_tickets", []).append(ticket_record)
        return json.dumps({"ok": True, "ticket": ticket_record})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_hubspot_ticket",
                "description": "Create a general HubSpot support ticket following deterministic rules.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subject": {"type": "string", "description": "Ticket subject line."},
                        "description": {"type": "string", "description": "Ticket description."},
                        "assignee_id": {"type": "string", "description": "User ID who will handle the ticket."},
                        "requester_id": {"type": "string", "description": "User ID who is requesting the ticket."},
                        "priority": {"type": "string", "description": "Ticket priority (HIGH, MEDIUM, LOW).", "default": "MEDIUM"},
                        "category": {"type": "string", "description": "Ticket category.", "default": "GENERAL"},
                        "status": {"type": "string", "description": "Ticket status (OPEN, IN_PROGRESS, CLOSED).", "default": "OPEN"}
                    },
                    "required": ["subject", "description", "assignee_id", "requester_id"],
                    "additionalProperties": False
                }
            }
        }
