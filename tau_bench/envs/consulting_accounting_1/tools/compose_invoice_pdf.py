from tau_bench.envs.tool import Tool
import json
from typing import Any

class ComposeInvoicePdf(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], invoice_id: str = None, publisher_id: str = None) -> str:
        if not invoice_id or not publisher_id:
            payload = {"error": "invoice_id and publisher_id are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        path = f"/invoices/auto/{invoice_id}.pdf"
        payload = {"invoice_id": invoice_id, "publisher_id": publisher_id, "pdf_path": path}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ComposeInvoicePdf",
                "description": "Generate a PDF artifact path for the invoice.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoice_id": {"type": "string"},
                        "publisher_id": {"type": "string"},
                    },
                    "required": ["invoice_id", "publisher_id"],
                },
            },
        }
