from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timezone, date, timedelta
import calendar
from typing import Any, Dict
import random



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ChangeSupportTicketStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, ticket_id: str = None, new_status: str = "") -> str:
        new_status = new_status.strip()
        if not all([customer_id, ticket_id, new_status]):
            return json.dumps({"error": "customer_id, ticket_id and new_status are required."}, indent=2)

        tickets = data.get("support_tickets", {}).values()
        for ticket in tickets.values():
            if (ticket.get("ticket_id") == ticket_id and
                ticket.get("customer_id") == customer_id):
                ticket["status"] = new_status
                return json.dumps(ticket, indent=2)

        return json.dumps({"error": "Support ticket not found for this customer."}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ChangeSupportTicketStatus",
                "description": "Updates the status of a support ticket given its ID and customer ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "ID of the customer who owns the ticket"
                        },
                        "ticket_id": {
                            "type": "string",
                            "description": "Identifier of the support ticket to update"
                        },
                        "new_status": {
                            "type": "string",
                            "description": "New status value (e.g., 'Resolved' or 'Open')"
                        }
                    },
                    "required": ["customer_id", "ticket_id", "new_status"]
                }
            }
        }
