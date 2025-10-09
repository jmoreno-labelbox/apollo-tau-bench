from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CaV2GetUnpaidInvoices(Tool):
    """Retrieve all outstanding invoices."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        invoices = data.get("invoices", {}).values()
        unpaid_invoices = [inv for inv in invoices.values() if not inv.get("paid_at")]
        payload = unpaid_invoices
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2GetUnpaidInvoices",
                "description": "Get all invoices that have not been paid yet.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }
