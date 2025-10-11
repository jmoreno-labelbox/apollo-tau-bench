# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCustomerSupportTicketsTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id, status) -> str:
        status_filter = status

        support_tickets = list(data.get('support_tickets', {}).values())
        customer_tickets = []

        for ticket in support_tickets:
            if ticket['customer_id'] == customer_id:
                if not status_filter or ticket['status'] == status_filter:
                    subject = ticket.get('subject', ticket.get('category', 'N/A'))

                    customer_tickets.append({
                        'ticket_id': ticket['ticket_id'],
                        'subject': subject,
                        'priority': ticket['priority'],
                        'status': ticket['status'],
                        'created_date': ticket.get('created_date', 'N/A'),
                        'assigned_agent': ticket.get('assigned_agent', 'Unassigned')
                    })

        return json.dumps(customer_tickets, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_customer_support_tickets",
                "description": "Get support tickets for a customer",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Customer identifier"},
                        "status": {"type": "string", "description": "Filter by status", "enum": ["Open", "Resolved", "In Progress"]}
                    },
                    "required": ["customer_id"]
                }
            }
        }
