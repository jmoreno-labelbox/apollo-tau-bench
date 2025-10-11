# Sierra copyright notice

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CaV2GetUnpaidInvoices(Tool):
    """Get all unpaid invoices."""

    @staticmethod
    def invoke(data: Dict[str, Any], ) -> str:
        invoices = data.get("invoices", [])
        unpaid_invoices = [inv for inv in invoices if not inv.get("paid_at")]
        return json.dumps(unpaid_invoices)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_get_unpaid_invoices",
                "description": "Get all invoices that have not been paid yet.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }
