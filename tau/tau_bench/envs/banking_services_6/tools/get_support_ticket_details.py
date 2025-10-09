from tau_bench.envs.tool import Tool
import json
from datetime import date, datetime, time, timedelta, timezone
from typing import Any, Dict, List

class GetSupportTicketDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], ticket_id: str = None) -> str:
        ticket = next((t for t in data.get('support_tickets', []) if t['ticket_id'] == ticket_id), None)
        if ticket:
            return json.dumps(ticket)
        return json.dumps({"error": "Support ticket not found."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "GetSupportTicketDetails",
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
