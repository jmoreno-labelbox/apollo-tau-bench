# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ReassignOrderCarrier(Tool):
    """Changes the assigned carrier for a specific outbound order."""
    @staticmethod
    def invoke(data: Dict[str, Any], new_carrier_scac, order_id) -> str:
        if not all([order_id, new_carrier_scac]):
            return json.dumps({"error": "order_id and new_carrier_scac are required."}, indent=2)
        order = next((o for o in data.get('outbound_orders', []) if o.get('order_id') == order_id), None)
        if not order:
            return json.dumps({"error": f"Order '{order_id}' not found."}, indent=2)
        new_carrier = next((c for c in data.get('carriers', []) if c.get('scac') == new_carrier_scac), None)
        if not new_carrier:
            return json.dumps({"error": f"New carrier with SCAC '{new_carrier_scac}' not found."}, indent=2)
        order['carrier_name'] = new_carrier.get('carrier_name')
        order['carrier_scac'] = new_carrier.get('scac')
        order_id_number = order_id.split('-')[1]
        order['tracking_number'] = f"{new_carrier.get('scac')}-{order_id_number}"
        return json.dumps(order, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "reassign_order_carrier", "description": "Changes the assigned carrier for a specific outbound order and generates a new tracking number.", "parameters": {"type": "object", "properties": {"order_id": {"type": "string"}, "new_carrier_scac": {"type": "string"}}, "required": ["order_id", "new_carrier_scac"]}}}
