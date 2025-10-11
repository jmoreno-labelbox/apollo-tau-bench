# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateSupportTicket(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], category, customer_id, details, priority, target_entity, target_id) -> str:
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
                        "name": "create_support_ticket",
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
