# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateHubspotTicketStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        ticket_id = kwargs.get("ticket_id")
        new_status = kwargs.get("status")
        for ticket in data.get('hubspot_tickets', []):
            if ticket.get('ticket_id') == ticket_id:
                ticket['status'] = new_status
                ticket['closed_at'] = NOW.strftime(DT_STR_FORMAT)
                return json.dumps(ticket)
        return json.dumps({"error": "Ticket not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "update_hubspot_ticket_status",
                        "description": "Updates the status of a HubSpot ticket (e.g., OPEN, CLOSED).",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "ticket_id": {"type": "string"},
                                        "status": {"type": "string"},
                                        "note": {"type": "string", "description": "An optional note to add when updating the status."}
                                },
                                "required": ["ticket_id", "status"]
                        }
                }
        }
