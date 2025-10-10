# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindOrdersByCarrier(Tool):
    """Finds all outbound orders assigned to a specific carrier, filtering by status."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        carrier_name = kwargs.get('carrier_name')
        status = kwargs.get('status')
        if not carrier_name:
            return json.dumps({"error": "carrier_name is a required argument."}, indent=2)
        orders = data.get('outbound_orders', [])
        results = [o for o in orders if o.get('carrier_name') == carrier_name and (not status or o.get('status') == status)]
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "find_orders_by_carrier", "description": "Finds all outbound orders assigned to a specific carrier, optionally filtering by status.", "parameters": {"type": "object", "properties": {"carrier_name": {"type": "string"}, "status": {"type": "string"}}, "required": ["carrier_name"]}}}
