# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateTicketStatusTool(Tool):
    """Update the status of a HubSpot ticket (write operation)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        tickets = data.get("hubspot_tickets", [])
        ticket_id = kwargs.get("ticket_id")
        new_status = kwargs.get("status")
        updated_at = kwargs.get("updated_at")

        if not isinstance(ticket_id, str):
            return json.dumps({"error": "ticket_id must be provided"}, indent=2)
        if not isinstance(new_status, str):
            return json.dumps({"error": "status must be provided"}, indent=2)

        for t in tickets:
            if t.get("ticket_id") == ticket_id:
                t["status"] = new_status
                if updated_at:
                    t["updated_at"] = updated_at
                return json.dumps({"success": f"Ticket {ticket_id} updated", "ticket": t}, indent=2)

        return json.dumps({"error": f"Ticket {ticket_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_ticket_status",
                "description": "Update the status of a HubSpot ticket.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ticket_id": {"type": "string", "description": "Unique ID of the ticket"},
                        "status": {"type": "string", "description": "New status of the ticket (e.g., OPEN, CLOSED, IN_PROGRESS)"},
                        "updated_at": {"type": "string", "description": "Optional ISO8601 timestamp of the update"}
                    },
                    "required": ["ticket_id", "status"]
                }
            }
        }
