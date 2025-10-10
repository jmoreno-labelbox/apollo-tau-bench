# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetSupportTicketDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], ticket_id) -> str:
        ticket = next((t for t in list(data.get('support_tickets', {}).values()) if t['ticket_id'] == ticket_id), None)
        if ticket:
            return json.dumps(ticket)
        return json.dumps({"error": "Support ticket not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_support_ticket_details",
                        "description": "Retrieves the full details of a single support ticket.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "ticket_id": {"type": "string", "description": "The unique ID of the support ticket."}
                                },
                                "required": ["ticket_id"]
                        }
                }
        }
