# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindInboundShipmentsBySupplier(Tool):
    """Finds all inbound shipments from a specific supplier ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], supplier_id) -> str:
        inbound_shipments = list(data.get("inbound_shipments", {}).values())
        found_shipments = []
        for shipment in inbound_shipments:
            if shipment.get("supplier_id") == supplier_id:
                found_shipments.append(shipment)
        if found_shipments:
            return json.dumps(found_shipments)
        return json.dumps({"message": "No inbound shipments found for that supplier"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_inbound_shipments_by_supplier",
                "description": "Finds all inbound shipments associated with a specific supplier ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {
                            "type": "string",
                            "description": "The ID of the supplier (e.g., 'SUP-1001').",
                        }
                    },
                    "required": ["supplier_id"],
                },
            },
        }
