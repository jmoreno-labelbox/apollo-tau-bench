from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any, Dict



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class SearchInboundShipments(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], sku: str = None, destination_warehouse_id: str = None, status: str = None) -> str:
        inbound_shipments = data.get("inbound_shipments", [])
        inventory = data.get("inventory", [])

        # Retrieve the existing stock for the SKU/warehouse
        current_inventory = next(
            (item for item in inventory
             if item.get("sku") == sku and item.get("warehouse_id") == destination_warehouse_id),
            None
        )

        current_available = current_inventory.get("quantity_available", 0) if current_inventory else 0
        current_inbound = current_inventory.get("quantity_inbound", 0) if current_inventory else 0

        # Narrow down the shipments that match
        results = []
        for shipment in inbound_shipments:
            match = True
            # Verify if the shipment includes the SKU by searching the data structure
            if sku and not any(sku in str(value) for value in shipment.values()):
                match = False
            if destination_warehouse_id and shipment.get("destination_warehouse_id") != destination_warehouse_id:
                match = False
            if status and shipment.get("status") != status:
                match = False
            if match:
                results.append(shipment)

        # Determine the total anticipated stock by adding actual inventory to inbound
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
                "name": "SearchInboundShipments",
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
