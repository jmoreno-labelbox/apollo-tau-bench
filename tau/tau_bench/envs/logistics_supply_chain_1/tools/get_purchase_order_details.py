# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetPurchaseOrderDetails(Tool):
    """Retrieves details of an inbound shipment by its Purchase Order number."""
    @staticmethod
    def invoke(data: Dict[str, Any], po_number) -> str:
        if not po_number:
            return json.dumps({"error": "po_number is required."}, indent=2)

        shipment = next((s for s in data.get('inbound_shipments', []) if s.get('purchase_order_number') == po_number), None)

        if not shipment:
            return json.dumps({"error": f"Shipment for Purchase Order '{po_number}' not found."}, indent=2)

        return json.dumps(shipment, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_purchase_order_details",
                "description": "Retrieves the shipment details associated with a given Purchase Order (PO) number.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "po_number": {"type": "string", "description": "The Purchase Order number to search for."}
                    },
                    "required": ["po_number"]
                }
            }
        }
