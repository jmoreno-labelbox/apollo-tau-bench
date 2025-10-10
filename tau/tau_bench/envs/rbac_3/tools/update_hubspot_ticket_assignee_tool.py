# Sierra copyright.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateHubspotTicketAssigneeTool(Tool):
    """update_hubspot_ticket_assignee: set assignee with audit."""

    @staticmethod
    def invoke(data: Dict[str, Any], actor_id, assignee_id, ticket_id) -> str:
        return UpdateHubspotTicketTool.invoke(
            data,
            ticket_id=ticket_id,
            assignee_id=assignee_id,
            actor_id=actor_id,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_hubspot_ticket_assignee",
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
