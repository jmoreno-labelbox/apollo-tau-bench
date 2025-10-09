from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any
from datetime import datetime, timedelta

class GetHubspotTicketsByAssigneeTool(Tool):
    """get_hubspot_tickets_by_assignee: filter tickets based on assignee."""

    @staticmethod
    def invoke(data: dict[str, Any], assignee_id: str = None) -> str:
        pass
        #utilize the list tool again with a post-filter
        tickets = json.loads(ListHubspotTicketsTool.invoke(data))
        payload = [t for t in tickets.values() if t.get("assignee_id") == assignee_id]
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getHubspotTicketsByAssignee",
                "description": "List HubSpot tickets for an assignee.",
                "parameters": {
                    "type": "object",
                    "properties": {"assignee_id": {"type": "string"}},
                    "required": ["assignee_id"],
                },
            },
        }
