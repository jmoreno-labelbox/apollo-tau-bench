from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any
from datetime import datetime, timedelta

class CloseHubspotTicketBasicTool(Tool):
    """
    close_hubspot_ticket_basic
    Assign a ticket to the actor, set priority to LOW, set status to CLOSED, and return the audit log id.
    """

    @staticmethod
    def invoke(data: dict[str, Any], ticket_id: str = None, actor_id: str = None) -> str:
        if not ticket_id or not actor_id:
            payload = {"error": "ticket_id and actor_id are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out

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
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "closeHubspotTicketBasic",
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
