# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindInboundShipments(Tool):
    """Tool to find inbound shipments based on criteria."""

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        status: Optional[str] = None,
        supplier_id: Optional[str] = None,
        warehouse_id: Optional[str] = None,
    ) -> str:
        """Execute the tool with given parameters."""
        shipments = data.get("inbound_shipments", [])
        results = []
        for shipment in shipments:
            if (not status or shipment.get("status") == status) and \
               (not supplier_id or shipment.get("supplier_id") == supplier_id) and \
               (not warehouse_id or shipment.get("destination_warehouse_id") == warehouse_id):
                results.append(shipment)
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Return tool specification for AI agent."""
        return {
            "type": "function",
            "function": {
                "name": "find_inbound_shipments",
                "description": "Finds inbound shipments based on status, supplier, or destination warehouse.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {"type": "string", "description": "Filter by shipment status (e.g., 'In Transit', 'Received', 'Delayed')."},
                        "supplier_id": {"type": "string", "description": "Filter by the supplier's ID."},
                        "warehouse_id": {"type": "string", "description": "Filter by the destination warehouse ID."},
                    },
                },
            },
        }
