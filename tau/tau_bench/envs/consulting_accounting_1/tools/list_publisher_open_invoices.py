from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ListPublisherOpenInvoices(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], publisher_id: str = None) -> str:
        if not publisher_id:
            payload = {"error": "publisher_id is required"}
            out = json.dumps(payload, indent=2)
            return out
        invoices = data.get("invoices", [])
        open_invs = [
            i
            for i in invoices
            if i.get("publisher_id") == publisher_id and not i.get("paid_at")
        ]
        payload = {
                "publisher_id": publisher_id,
                "invoice_ids": [i["invoice_id"] for i in open_invs],
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListPublisherOpenInvoices",
                "description": "Return unpaid invoice IDs for a publisher.",
                "parameters": {
                    "type": "object",
                    "properties": {"publisher_id": {"type": "string"}},
                    "required": ["publisher_id"],
                },
            },
        }
