# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import get_current_timestamp
from . import generate_unique_id


class CreateSupportTicketTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get('customer_id')
        subject = kwargs.get('subject')
        description = kwargs.get('description')
        priority = kwargs.get('priority', 'Medium')

        support_tickets = list(data.get('support_tickets', {}).values())

        ticket_id = f"ticket_{generate_unique_id()}"
        new_ticket = {
            "ticket_id": ticket_id,
            "customer_id": customer_id,
            "subject": subject,
            "description": description,
            "priority": priority,
            "status": "Open",
            "created_date": get_current_timestamp(),
            "assigned_agent": None,
            "resolution": None
        }

        support_tickets.append(new_ticket)

        return json.dumps({
            "ticket_id": ticket_id,
            "status": "Created",
            "priority": priority,
            "created_date": new_ticket["created_date"]
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_support_ticket",
                "description": "Create a new customer support ticket",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Customer identifier"},
                        "subject": {"type": "string", "description": "Ticket subject"},
                        "description": {"type": "string", "description": "Detailed issue description"},
                        "priority": {"type": "string", "description": "Priority level", "enum": ["Low", "Medium", "High", "Urgent"]}
                    },
                    "required": ["customer_id", "subject", "description"]
                }
            }
        }
