from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetInvoiceDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], invoice_id: str = None) -> str:
        if not invoice_id:
            payload = {"error": "invoice_id is required"}
            out = json.dumps(payload, indent=2)
            return out
        invoices = data.get("invoices", [])
        inv = next((i for i in invoices if i.get("invoice_id") == invoice_id), None)
        payload = inv or {"error": f"Invoice {invoice_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetInvoiceDetails",
                "description": "Retrieve all data for a specific invoice.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoice_id": {
                            "type": "string",
                            "description": "The ID of the invoice.",
                        }
                    },
                    "required": ["invoice_id"],
                },
            },
        }
