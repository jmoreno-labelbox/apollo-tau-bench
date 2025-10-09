from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any, Dict
from datetime import timedelta

class GetInvoiceDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], invoice_number: str) -> str:
        """
        Retrieves the full details for a given invoice_number.
        """
        invoice = next((inv for inv in data["invoices"].values() if inv["invoice_number"] == invoice_number), None)
        return json.dumps(invoice)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function", "function": {
                "name": "GetInvoiceDetails",
                "description": "Retrieve the full details for a given invoice by its invoice_number.",
                "parameters": {
                    "type": "object", "properties": {
                        "invoice_number": {"type": "string", "description": "The number of the invoice to retrieve"}
                    },
                    "required": ["invoice_number"],
                },
            },
        }
