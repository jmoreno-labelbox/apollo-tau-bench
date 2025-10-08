from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any
from datetime import datetime, timedelta

class GetHubspotTicketsByRequesterTool(Tool):
    """get_hubspot_tickets_by_requester: filter tickets based on requester."""

    @staticmethod
    def invoke(data: dict[str, Any], requester_id: str = None, role_id: Any = None) -> str:
        return ListHubspotTicketsTool.invoke(
            data, requester_id=requester_id
        )
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getHubspotTicketsByRequester",
                "description": "List HubSpot tickets for a requester.",
                "parameters": {
                    "type": "object",
                    "properties": {"requester_id": {"type": "string"}},
                    "required": ["requester_id"],
                },
            },
        }
