from tau_bench.envs.tool import Tool
from typing import Any, Dict
import json



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetSupportTicketsForAccountTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None, fields: list = None, start_date: str = None, end_date: str = None, customer_id: str = None) -> str:
        # Support both account_id and customer_id
        if not account_id and customer_id:
            # Find account for this customer
            accounts = data.get('accounts', {}).values()
            for acc in accounts.values():
                if acc.get('customer_id') == customer_id:
                    account_id = acc.get('account_id')
                    break
        support_tickets = data.get('support_tickets', {}).values()
        results = []

        for ticket in support_tickets.values():
            ticket_account_id = ticket.get('account_id', None)
            if ticket_account_id != account_id:
                continue
            if fields:
                subject = ticket.get('subject', '').lower()
                description = ticket.get('description', '').lower()
                category = ticket.get('category', '').lower()
                if not any(field.lower() in subject or field.lower() in description or field.lower() in category for field in fields.values()):
                    continue
            created_date = ticket.get('created_date', '')
            resolved_date = ticket.get('resolved_date', '')
            in_range = False
            if start_date and end_date:
                if (created_date and start_date <= created_date <= end_date) or (resolved_date and start_date <= resolved_date <= end_date):
                    in_range = True
            else:
                in_range = True

            if not in_range:
                continue

            results.append({
                "ticket_id": ticket.get("ticket_id"),
                "subject": ticket.get("subject", ""),
                "description": ticket.get("description", ""),
                "category": ticket.get("category", ""),
                "priority": ticket.get("priority", ""),
                "status": ticket.get("status", ""),
                "created_date": created_date,
                "resolved_date": resolved_date,
                "assigned_agent": ticket.get("assigned_agent", "")
            })

        return json.dumps(results, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSupportTicketsForAccount",
                "description": "Get support tickets for a specific account, filtered by keywords and date range.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string", "description": "Account identifier"},
                        "fields": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of keywords to filter tickets (e.g. payment issues, account inquiries)"
                        },
                        "start_date": {"type": "string", "description": "Start date (ISO format)"},
                        "end_date": {"type": "string", "description": "End date (ISO format)"}
                    },
                    "required": ["account_id"]
                }
            }
        }
