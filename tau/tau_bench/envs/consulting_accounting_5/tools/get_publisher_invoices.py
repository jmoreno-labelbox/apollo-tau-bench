from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any, Dict
from datetime import timedelta

class GetPublisherInvoices(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], publisher_id: str) -> str:
        """
        Returns all invoice_ids for a given publisher_id.
        """
        invoices = [inv for inv in data["invoices"] if inv["publisher_id"] == publisher_id]
        return json.dumps([inv["invoice_id"] for inv in invoices])
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPublisherInvoices",
                "description": "Retrieve all invoice_ids for a given publisher_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "publisher_id": {"type": "string", "description": "Publisher ID to filter invoices by"}
                    },
                    "required": ["publisher_id"],
                },
            },
        }
