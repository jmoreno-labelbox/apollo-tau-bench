from tau_bench.envs.tool import Tool
import json
from datetime import date, datetime, time, timedelta, timezone
from typing import Any, Dict, List

class CreateSupportTicket(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, priority: str = None, category: str = None, details: str = None, target_entity: str = None, target_id: str = None) -> str:
        ticket_id = _get_next_support_ticket_id(data)
        new_ticket = {
                "ticket_id": ticket_id,
                "customer_id": customer_id,
                "status": "Open",
                "priority": priority,
                "category": category,
                "request_details": {
                        "details": details,
                        "target_entity": target_entity,
                        "target_id": target_id,
                }
        }
        data['support_tickets'].append(new_ticket)
        return json.dumps(new_ticket)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "CreateSupportTicket",
                        "description": "Creates a new support ticket for a customer issue.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "customer_id": {"type": "string"}, "category": {"type": "string"}, "priority": {"type": "string"},
                                        "details": {"type": "string"}, "target_entity": {"type": "string"}, "target_id": {"type": "string"}
                                },
                                "required": ["customer_id", "category", "priority", "details", "target_entity", "target_id"]
                        }
                }
        }
