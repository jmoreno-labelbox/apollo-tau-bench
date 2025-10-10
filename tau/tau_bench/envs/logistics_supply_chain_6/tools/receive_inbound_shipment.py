# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ReceiveInboundShipment(Tool):
    """Tool to process the receipt of an inbound shipment."""

    @staticmethod
    def invoke(data: Dict[str, Any], shipment_id: str, items_received: List[Dict[str, Any]]) -> str:
        """Execute the tool with given parameters."""

        shipments = data.get("inbound_shipments", [])
        inventory = list(data.get("inventory", {}).values())
        shipment_found = False
        for shipment in shipments:
            if shipment.get("shipment_id") == shipment_id:
                shipment_found = True
                if shipment["status"] == "Received":
                    return json.dumps({"error": f"Shipment {shipment_id} has already been received."}, indent=2)

                shipment["status"] = "Received"
                shipment["actual_arrival_date"] = "2024-07-19" # Emulating the current date

                # Revise stock levels.
                warehouse_id = shipment["destination_warehouse_id"]
                for received_item in items_received:
                    sku = received_item["sku"]
                    quantity = received_item["quantity"]
                    inv_item_found = False
                    for inv_item in inventory:
                        if inv_item["warehouse_id"] == warehouse_id and inv_item["sku"] == sku:
                            inv_item["quantity_on_hand"] += quantity
                            inv_item["quantity_available"] += quantity
                            inv_item_found = True
                            break
                    if not inv_item_found:
                        # This scenario is addressed by generating a new inventory entry, though it is presented in a simplified manner.
                        return json.dumps({"error": f"SKU {sku} not found in inventory for warehouse {warehouse_id}. Cannot receive."}, indent=2)

                return json.dumps({"shipment_id": shipment_id, "status": "Received"}, indent=2)

        if not shipment_found:
            return json.dumps({"error": f"Shipment with ID {shipment_id} not found"}, indent=2)
        return ""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Return tool specification for AI agent."""
        return {
            "type": "function",
            "function": {
                "name": "receive_inbound_shipment",
                "description": "Processes the receipt of an inbound shipment, updating its status and adding the received items to inventory.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "shipment_id": {"type": "string", "description": "The ID of the inbound shipment being received."},
                        "items_received": {
                            "type": "array", "items": {"type": "string"},
                            "description": "A list of SKUs and quantities that were received.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "sku": {"type": "string", "description": "Product SKU."},
                                    "quantity": {"type": "integer", "description": "Number of units received."}
                                },
                                "required": ["sku", "quantity"]
                            }
                        }
                    },
                    "required": ["shipment_id", "items_received"],
                },
            },
        }
