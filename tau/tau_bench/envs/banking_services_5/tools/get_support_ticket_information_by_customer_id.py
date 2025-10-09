from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timezone, date, timedelta
import calendar
from typing import Any, Dict
import random

class GetSupportTicketInformationByCustomerId(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = "") -> str:
        customer_id = customer_id.strip()

        if not customer_id:
            return json.dumps({"error": "customer_id is required."}, indent=2)

        support_tickets = data.get("support_tickets", [])
        matched_tickets = [
            ticket for ticket in support_tickets
            if ticket.get("customer_id") == customer_id
        ]

        if not matched_tickets:
            return json.dumps({"message": "No support tickets found for this customer."}, indent=2)

        return json.dumps({"tickets": matched_tickets}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getSupportTicketInformationByCustomerId",
                "description": "Fetches all support tickets associated with the given customer ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "Unique ID of the customer whose support tickets are to be fetched"
                        }
                    },
                    "required": ["customer_id"]
                }
            }
        }
