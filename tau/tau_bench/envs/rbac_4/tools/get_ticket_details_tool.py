# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetTicketDetailsTool(Tool):
    """Retrieve a HubSpot ticket by ticket_id (read-only, deterministic)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        ticket_id = kwargs.get("ticket_id")
        tickets = data.get("hubspot_tickets", [])
        if not isinstance(tickets, list):
            return json.dumps({"error": "hubspot_tickets must be a list"}, indent=2)

        if not isinstance(ticket_id, str) or not ticket_id.strip():
            return json.dumps({"error": "ticket_id must be a non-empty string"}, indent=2)

        for t in tickets:
            if t.get("ticket_id") == ticket_id:
                return json.dumps(t, indent=2)

        return json.dumps({"error": f"ticket_id {ticket_id} not found"}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "get_ticket_details",
                "description": "Retrieve details of a HubSpot ticket by ticket_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ticket_id": {"type": "string"}
                    },
                    "required": ["ticket_id"]
                }
            }
        }
