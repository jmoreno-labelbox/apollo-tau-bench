# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetHubspotTicketsByRequesterTool(Tool):
    """get_hubspot_tickets_by_requester: filter tickets by requester."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return ListHubspotTicketsTool.invoke(
            data, requester_id=kwargs.get("requester_id")
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_hubspot_tickets_by_requester",
                "description": "List HubSpot tickets for a requester.",
                "parameters": {
                    "type": "object",
                    "properties": {"requester_id": {"type": "string"}},
                    "required": ["requester_id"],
                },
            },
        }
