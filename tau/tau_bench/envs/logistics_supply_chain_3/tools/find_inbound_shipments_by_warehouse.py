# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindInboundShipmentsByWarehouse(Tool):
    """Finds all inbound shipments destined for a specific warehouse ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], warehouse_id) -> str:
        inbound_shipments = list(data.get("inbound_shipments", {}).values())
        found_shipments = []
        for shipment in inbound_shipments:
            # Manage possible key errors for destination_warehouse_id.
            dest_id = shipment.get("destination_warehouse_id") or shipment.get(
                "destination_warehouse_id"
            )
            if dest_id == warehouse_id:
                found_shipments.append(shipment)
        if found_shipments:
            return json.dumps(found_shipments)
        return json.dumps({"message": "No inbound shipments found for that warehouse"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_inbound_shipments_by_warehouse",
                "description": "Finds all inbound shipments, including their status and expected arrival date, destined for a specific warehouse ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "warehouse_id": {
                            "type": "string",
                            "description": "The ID of the destination warehouse (e.g., 'WH-01').",
                        }
                    },
                    "required": ["warehouse_id"],
                },
            },
        }
