# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetHubspotTicketsByAssignee(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], assignee_id) -> str:

        matching_tickets = [
                ticket for ticket in data.get('hubspot_tickets', [])
                if ticket.get('assignee_id') == assignee_id
        ]

        return json.dumps({"tickets": matching_tickets})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_hubspot_tickets_by_assignee",
                        "description": "Retrieves a list of HubSpot tickets based on the assignee's user ID.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "assignee_id": {
                                                "type": "string",
                                                "description": "The user_id of the person to whom the tickets are assigned."
                                        }
                                },
                                "required": ["assignee_id"]
                        }
                }
        }
