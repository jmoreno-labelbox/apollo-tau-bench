# Sierra copyright.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateHubspotTicket(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        tickets = data.get('hubspot_tickets', [])
        new_id_num = max((int(t['ticket_id'][3:]) for t in tickets), default=0) + 1
        new_ticket_id = f"TI-{new_id_num:03d}"
        new_ticket = {
                "ticket_id": new_ticket_id,
                "subject": kwargs.get("subject"),
                "description": kwargs.get("description"),
                "requester_id": kwargs.get("requester_id"),
                "category": kwargs.get("category"),
                "assignee_id": kwargs.get("assignee_id"),
                "status": "OPEN"
        }
        tickets.append(new_ticket)
        data['hubspot_tickets'] = tickets
        return json.dumps(new_ticket)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "create_hubspot_ticket",
                        "description": "Creates a new ticket in HubSpot.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "subject": {"type": "string"},
                                        "description": {"type": "string"},
                                        "requester_id": {"type": "string"},
                                        "category": {"type": "string"},
                                        "assignee_id": {"type": "string"}
                                },
                                "required": ["subject", "description", "requester_id", "category"]
                        }
                }
        }
