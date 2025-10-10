# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CloseHubspotTicketBasicTool(Tool):
    """
    close_hubspot_ticket_basic
    Assign a ticket to actor, set priority to LOW, set status to CLOSED, and return audit log id.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        ticket_id = kwargs.get("ticket_id")
        actor_id = kwargs.get("actor_id")
        if not ticket_id or not actor_id:
            return json.dumps(
                {"error": "ticket_id and actor_id are required"}, indent=2
            )

        updated = json.loads(
            UpdateHubspotTicketTool.invoke(
                data,
                ticket_id=ticket_id,
                assignee_id=actor_id,
                priority="LOW",
                status="CLOSED",
                actor_id=actor_id,
                note="auto-close",
            )
        )

        out = {
            "ticket_id": ticket_id,
            "status": updated.get("status"),
            "assignee_id": updated.get("assignee_id"),
            "priority": updated.get("priority"),
            "audit_log_id": f"LOG-{ticket_id}-update",
        }
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "close_hubspot_ticket_basic",
                "description": "Assign and close a HubSpot ticket with audit.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ticket_id": {"type": "string"},
                        "actor_id": {"type": "string"},
                    },
                    "required": ["ticket_id", "actor_id"],
                },
            },
        }
