# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindInboundShipment(Tool):
    """Finds a specific inbound shipment based on supplier and origin."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        supplier_name = kwargs.get('supplier_name')
        origin_city = kwargs.get('origin_city')
        status = kwargs.get('status')
        if not all([supplier_name, origin_city]):
            return json.dumps({"error": "supplier_name and origin_city are required arguments."}, indent=2)
        shipments = data.get('inbound_shipments', [])
        results = [s for s in shipments if s.get('supplier_name') == supplier_name and s.get('origin_city') == origin_city and (not status or s.get('status') == status)]
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "find_inbound_shipment", "description": "Finds inbound shipments from a specific supplier and origin city, optionally filtering by status.", "parameters": {"type": "object", "properties": {"supplier_name": {"type": "string"}, "origin_city": {"type": "string"}, "status": {"type": "string", "description": "Optional status to filter by (e.g., 'In Transit')."}}, "required": ["supplier_name", "origin_city"]}}}
