from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CreateInboundShipment(Tool):
    """Utility for generating a new record for an inbound shipment."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        supplier_id: str,
        destination_warehouse_id: str,
        carrier_id: str,
        items: list[dict[str, Any]],
        estimated_arrival_date: str
,
    supplier_name: Any = None,
    ) -> str:
        """Run the tool with the provided parameters."""
        inbound_shipments = data.get("inbound_shipments", [])

        new_shipment_id = f"SHIP-{len(inbound_shipments) + 1:04d}"

        new_shipment = {
            "shipment_id": new_shipment_id,
            "supplier_id": supplier_id,
            "destination_warehouse_id": destination_warehouse_id,
            "carrier_id": carrier_id,
            "status": "In Transit",
            "items": items,
            "estimated_arrival_date": estimated_arrival_date,
            "actual_arrival_date": None,
            "customs_status": "Cleared",
            "hazmat": any(item.get("hazmat", False) for item in items),
        }

        inbound_shipments.append(new_shipment)
        payload = new_shipment
        out = json.dumps(payload, indent=2)
        return out
        """Run the tool with the provided parameters."""
        pass
        inbound_shipments = data.get("inbound_shipments", [])

        new_shipment_id = f"SHIP-{len(inbound_shipments) + 1:04d}"

        new_shipment = {
            "shipment_id": new_shipment_id,
            "supplier_id": supplier_id,
            "destination_warehouse_id": destination_warehouse_id,
            "carrier_id": carrier_id,
            "status": "In Transit",
            "items": items,
            "estimated_arrival_date": estimated_arrival_date,
            "actual_arrival_date": None,
            "customs_status": "Cleared",
            "hazmat": any(item.get("hazmat", False) for item in items),
        }

        inbound_shipments.append(new_shipment)
        payload = new_shipment
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Provide the specifications of the tool for the AI agent."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "CreateInboundShipment",
                "description": "Creates a new inbound shipment record from a supplier to a warehouse.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {
                            "type": "string",
                            "description": "The ID of the supplier sending the shipment.",
                        },
                        "destination_warehouse_id": {
                            "type": "string",
                            "description": "The ID of the destination warehouse.",
                        },
                        "carrier_id": {
                            "type": "string",
                            "description": "The ID of the carrier transporting the shipment.",
                        },
                        "items": {
                            "type": "array",
                            "description": "A list of items in the shipment.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "sku": {
                                        "type": "string",
                                        "description": "Product SKU.",
                                    },
                                    "quantity": {
                                        "type": "integer",
                                        "description": "Number of units.",
                                    },
                                },
                                "required": ["sku", "quantity"],
                            },
                        },
                        "estimated_arrival_date": {
                            "type": "string",
                            "description": "The estimated arrival date in YYYY-MM-DD format.",
                        },
                    },
                    "required": [
                        "supplier_id",
                        "destination_warehouse_id",
                        "carrier_id",
                        "items",
                        "estimated_arrival_date",
                    ],
                },
            },
        }
