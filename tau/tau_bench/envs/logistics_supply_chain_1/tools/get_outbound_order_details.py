# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetOutboundOrderDetails(Tool):
    """Retrieves the full details for a single outbound order by its ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], order_id) -> str:
        if not order_id:
            return json.dumps({"error": "order_id is required."}, indent=2)
        order = next((o for o in data.get('outbound_orders', []) if o.get('order_id') == order_id), None)
        if not order:
            return json.dumps({"error": f"Order '{order_id}' not found."}, indent=2)
        return json.dumps(order, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_outbound_order_details", "description": "Retrieves the full details for a single outbound order by its ID.", "parameters": {"type": "object", "properties": {"order_id": {"type": "string"}}, "required": ["order_id"]}}}
