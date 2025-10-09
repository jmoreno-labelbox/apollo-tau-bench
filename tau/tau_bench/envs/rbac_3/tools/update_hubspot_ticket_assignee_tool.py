from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any
from datetime import datetime, timedelta

class UpdateHubspotTicketAssigneeTool(Tool):
    """update_hubspot_ticket_assignee: assign assignee with audit."""

    @staticmethod
    def invoke(data: dict[str, Any], ticket_id: str = None, assignee_id: str = None, actor_id: str = None, note: Any = None) -> str:
        pass
        return UpdateHubspotTicketTool.invoke(
            data,
            ticket_id=ticket_id,
            assignee_id=assignee_id,
            actor_id=actor_id,
        )
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateHubspotTicketAssignee",
                "description": "Update a HubSpot ticket assignee (writes audit entry).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ticket_id": {"type": "string"},
                        "assignee_id": {"type": "string"},
                        "actor_id": {"type": "string"},
                    },
                    "required": ["ticket_id", "assignee_id"],
                },
            },
        }
