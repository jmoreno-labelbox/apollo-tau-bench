# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchInboundShipments(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        sku = kwargs.get("sku")
        destination_warehouse_id = kwargs.get("destination_warehouse_id")
        status = kwargs.get("status")

        inbound_shipments = list(data.get("inbound_shipments", {}).values())
        inventory = list(data.get("inventory", {}).values())

        # Find current inventory for the SKU/warehouse
        current_inventory = next(
            (item for item in inventory
             if item.get("sku") == sku and item.get("warehouse_id") == destination_warehouse_id),
            None
        )

        current_available = current_inventory.get("quantity_available", 0) if current_inventory else 0
        current_inbound = current_inventory.get("quantity_inbound", 0) if current_inventory else 0

        # Filter matching shipments
        results = []
        for shipment in inbound_shipments:
            match = True
            # Check if shipment contains the SKU by looking for it in the data structure
            if sku and not any(sku in str(value) for value in shipment.values()):
                match = False
            if destination_warehouse_id and shipment.get("destination_warehouse_id") != destination_warehouse_id:
                match = False
            if status and shipment.get("status") != status:
                match = False
            if match:
                results.append(shipment)

        # Calculate total expected stock based on actual inventory + inbound
        total_expected_stock = current_available + current_inbound

        return json.dumps({
            "shipments": results,
            "current_available": current_available,
            "current_inbound": current_inbound,
            "total_expected_stock": total_expected_stock
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_inbound_shipments",
                "description": "Search for inbound shipments based on criteria",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {"type": "string", "description": "Product SKU to filter by"},
                        "destination_warehouse_id": {"type": "string", "description": "Destination warehouse"},
                        "status": {"type": "string", "description": "Shipment status to filter by"}
                    },
                    "required": []
                }
            }
        }
