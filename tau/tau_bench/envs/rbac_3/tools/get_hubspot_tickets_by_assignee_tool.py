# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetHubspotTicketsByAssigneeTool(Tool):
    """get_hubspot_tickets_by_assignee: filter tickets by assignee."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        # utilize list tool with subsequent filtering
        tickets = json.loads(ListHubspotTicketsTool.invoke(data))
        assignee_id = kwargs.get("assignee_id")
        return json.dumps(
            [t for t in tickets if t.get("assignee_id") == assignee_id], indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_hubspot_tickets_by_assignee",
                "description": "List HubSpot tickets for an assignee.",
                "parameters": {
                    "type": "object",
                    "properties": {"assignee_id": {"type": "string"}},
                    "required": ["assignee_id"],
                },
            },
        }
