from tau_bench.envs.tool import Tool
import json
import os
from datetime import datetime, timedelta
from typing import Any, Dict

class ReviewTicketHistoryTool(Tool):
    """
    Tool to review all support tickets submitted by a specific customer.

    This tool fetches open and resolved tickets associated with a given customer ID,
    showing status, category, channel of submission, and ticket details.

    Methods:
        invoke(data: Dict[str, Any], **kwargs) -> str:
            Returns a formatted history of tickets for the given customer.

        get_info() -> Dict[str, Any]:
            Provides interface schema and tool description for orchestration.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None) -> str:
        if not customer_id:
            return json.dumps({"error": "customer_id is required"})

        tickets = load_json("support_tickets.json")
        customer_tickets = [t for t in tickets if t["customer_id"] == customer_id]
        open_tickets = sum(1 for t in customer_tickets if t["status"] != "Resolved")
        summary = (
            f"Total tickets: {len(customer_tickets)}. Open tickets: {open_tickets}."
        )

        return json.dumps({"summary": summary, "open_tickets": open_tickets}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ReviewTicketHistory",
                "description": "Review historical support tickets and unresolved issues.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Customer ID"}
                    },
                    "required": ["customer_id"],
                },
            },
        }
