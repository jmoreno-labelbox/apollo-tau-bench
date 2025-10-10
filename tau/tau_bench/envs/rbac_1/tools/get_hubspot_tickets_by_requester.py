# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetHubspotTicketsByRequester(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        requester_id = kwargs.get("requester_id")

        matching_tickets = [
                ticket for ticket in data.get('hubspot_tickets', [])
                if ticket.get('requester_id') == requester_id
        ]

        return json.dumps({"tickets": matching_tickets})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_hubspot_tickets_by_requester",
                        "description": "Retrieves a list of HubSpot tickets based on the requester's user ID.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "requester_id": {
                                                "type": "string",
                                                "description": "The user_id of the person who requested the tickets."
                                        }
                                },
                                "required": ["requester_id"]
                        }
                }
        }
