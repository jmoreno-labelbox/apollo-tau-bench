from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ReceiveInboundShipment(Tool):
    """Utility for handling the receipt of an inbound shipment."""

    @staticmethod
    def invoke(
        data: dict[str, Any], shipment_id: str, items_received: list[dict[str, Any]]
    ) -> str:
        """Run the tool using the specified parameters."""
        shipments = data.get("inbound_shipments", {}).values()
        inventory = data.get("inventory", {}).values()
        shipment_found = False
        for shipment in shipments.values():
            if shipment.get("shipment_id") == shipment_id:
                shipment_found = True
                if shipment["status"] == "Received":
                    payload = {"error": f"Shipment {shipment_id} has already been received."}
                    out = json.dumps(
                        payload, indent=2,
                    )
                    return out

                shipment["status"] = "Received"
                shipment["actual_arrival_date"] = (
                    "2024-07-19"  # Mimicking the current date
                )

                # Revise inventory
                warehouse_id = shipment["destination_warehouse_id"]
                for received_item in items_received:
                    sku = received_item["sku"]
                    quantity = received_item["quantity"]
                    inv_item_found = False
                    for inv_item in inventory.values():
                        if (
                            inv_item["warehouse_id"] == warehouse_id
                            and inv_item["sku"] == sku
                        ):
                            inv_item["quantity_on_hand"] += quantity
                            inv_item["quantity_available"] += quantity
                            inv_item_found = True
                            break
                    if not inv_item_found:
                        payload = {
                            "error": f"SKU {sku} not found in inventory for warehouse {warehouse_id}. Cannot receive."
                        }
                        out = json.dumps(
                            payload, indent=2,
                        )
                        return out
                payload = {"shipment_id": shipment_id, "status": "Received"}
                out = json.dumps(
                    payload, indent=2
                )
                return out

        if not shipment_found:
            payload = {"error": f"Shipment with ID {shipment_id} not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        return ""
        """Run the tool using the specified parameters."""
        pass

        shipments = data.get("inbound_shipments", {}).values()
        inventory = data.get("inventory", {}).values()
        shipment_found = False
        for shipment in shipments.values():
            if shipment.get("shipment_id") == shipment_id:
                shipment_found = True
                if shipment["status"] == "Received":
                    payload = {"error": f"Shipment {shipment_id} has already been received."}
                    out = json.dumps(
                        payload, indent=2,
                    )
                    return out

                shipment["status"] = "Received"
                shipment["actual_arrival_date"] = (
                    "2024-07-19"  #Mimicking the current date
                )

                #Revise inventory
                warehouse_id = shipment["destination_warehouse_id"]
                for received_item in items_received:
                    sku = received_item["sku"]
                    quantity = received_item["quantity"]
                    inv_item_found = False
                    for inv_item in inventory.values():
                        if (
                            inv_item["warehouse_id"] == warehouse_id
                            and inv_item["sku"] == sku
                        ):
                            inv_item["quantity_on_hand"] += quantity
                            inv_item["quantity_available"] += quantity
                            inv_item_found = True
                            break
                    if not inv_item_found:
                        payload = {
                                "error": f"SKU {sku} not found in inventory for warehouse {warehouse_id}. Cannot receive."
                            }
                        out = json.dumps(
                            payload, indent=2,
                        )
                        return out
                payload = {"shipment_id": shipment_id, "status": "Received"}
                out = json.dumps(
                    payload, indent=2
                )
                return out

        if not shipment_found:
            payload = {"error": f"Shipment with ID {shipment_id} not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        return ""

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Provide tool specifications for the AI agent."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "ReceiveInboundShipment",
                "description": "Processes the receipt of an inbound shipment, updating its status and adding the received items to inventory.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "shipment_id": {
                            "type": "string",
                            "description": "The ID of the inbound shipment being received.",
                        },
                        "items_received": {
                            "type": "array",
                            "description": "A list of SKUs and quantities that were received.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "sku": {
                                        "type": "string",
                                        "description": "Product SKU.",
                                    },
                                    "quantity": {
                                        "type": "integer",
                                        "description": "Number of units received.",
                                    },
                                },
                                "required": ["sku", "quantity"],
                            },
                        },
                    },
                    "required": ["shipment_id", "items_received"],
                },
            },
        }
