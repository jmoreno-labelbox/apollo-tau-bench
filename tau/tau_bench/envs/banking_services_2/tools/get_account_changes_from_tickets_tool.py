from tau_bench.envs.tool import Tool
from typing import Any, Dict
import json



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetAccountChangesFromTicketsTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None) -> str:
        support_tickets = data.get('support_tickets', [])
        changes = []

        for ticket in support_tickets:
            if ticket.get('account_id') != account_id:
                continue
            change_types = []
            subject = ticket.get('subject', '').lower()
            description = ticket.get('description', '').lower()
            category = ticket.get('category', '').lower()

            keywords = ["update", "change", "modify", "freeze", "close", "re-open", "unlock", "limit", "restriction", "address", "contact", "status", "name"]
            if any(kw in subject or kw in description or kw in category for kw in keywords):
                change_types.append("change_detected")

            changes.append({
                "ticket_id": ticket.get("ticket_id"),
                "subject": ticket.get("subject", ""),
                "description": ticket.get("description", ""),
                "category": ticket.get("category", ""),
                "status": ticket.get("status", ""),
                "created_date": ticket.get("created_date", ""),
                "change_types": change_types,
                "raw_ticket": ticket
            })

        return json.dumps(changes, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAccountChangesFromTickets",
                "description": "Extract tickets that indicate account changes (update, freeze, contact change, etc) for a specific account.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string", "description": "Account identifier"}
                    },
                    "required": ["account_id"]
                }
            }
        }
