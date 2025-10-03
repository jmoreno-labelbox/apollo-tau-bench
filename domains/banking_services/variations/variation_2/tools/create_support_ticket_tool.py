from tau_bench.envs.tool import Tool
from typing import Any, Dict
import json

class CreateSupportTicketTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str, subject: str, description: str, priority: str = 'Medium') -> str:
        support_tickets = data.get('support_tickets', [])

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
                "name": "CreateSupportTicket",
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
