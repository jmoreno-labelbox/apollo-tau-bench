# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateHubspotTicketStatusTool(Tool):
    """update_hubspot_ticket_status: set status with audit."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return UpdateHubspotTicketTool.invoke(
            data,
            ticket_id=kwargs.get("ticket_id"),
            status=kwargs.get("status"),
            actor_id=kwargs.get("actor_id"),
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_hubspot_ticket_status",
                "description": "Update a HubSpot ticket status (writes audit entry).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ticket_id": {"type": "string"},
                        "status": {"type": "string"},
                        "actor_id": {"type": "string"},
                    },
                    "required": ["ticket_id", "status"],
                },
            },
        }
