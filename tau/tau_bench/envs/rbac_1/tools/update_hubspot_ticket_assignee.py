# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateHubspotTicketAssignee(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], new_assignee_id, ticket_id) -> str:
        for ticket in data.get('hubspot_tickets', []):
            if ticket.get('ticket_id') == ticket_id:
                ticket['assignee_id'] = new_assignee_id
                ticket['updated_at'] = NOW.strftime(DT_STR_FORMAT)
                return json.dumps(ticket)
        return json.dumps({"error": "Ticket not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "update_hubspot_ticket_assignee",
                        "description": "Updates the assignee of an existing HubSpot ticket.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "ticket_id": {
                                            "type": "string",
                                            "description": "The ID of the ticket to update."
                                        },
                                        "new_assignee_id": {
                                            "type": "string",
                                            "description": "The user_id of the new assignee."
                                        }
                                },
                                "required": ["ticket_id", "new_assignee_id"]
                        }
                }
        }
