# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateHubspotTicketTool(Tool):
    """Create a new HubSpot ticket linked to RBAC or SIEM context."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        tickets = data.get("hubspot_tickets", [])

        subject = kwargs.get("subject")
        description = kwargs.get("description")
        requester_id = kwargs.get("requester_id")
        assignee_id = kwargs.get("assignee_id")
        category = kwargs.get("category")
        priority = kwargs.get("priority", "MEDIUM")

        # Deterministic ticket ID
        new_id = f"TI-{len(tickets) + 1:03d}"
        fixed_time = "2025-08-11 12:00:00+00:00"

        tickets.append({
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
            "closed_at": None
        })

        return json.dumps({"success": f"Ticket {new_id} created"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_hubspot_ticket",
                "description": "Create a HubSpot ticket and associate it with RBAC or SIEM events.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "subject": {"type": "string"},
                        "description": {"type": "string"},
                        "requester_id": {"type": "string"},
                        "assignee_id": {"type": "string"},
                        "category": {"type": "string"},
                        "priority": {"type": "string"}
                    },
                    "required": ["subject", "description", "requester_id", "assignee_id", "category"]
                }
            }
        }
