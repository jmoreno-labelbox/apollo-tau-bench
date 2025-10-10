# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateInboundShipment(Tool):
    """Tool to create a new inbound shipment record."""

    @staticmethod
    def invoke(data: Dict[str, Any], supplier_id: str, destination_warehouse_id: str, carrier_id: str, items: List[Dict[str, Any]], estimated_arrival_date: str) -> str:
        """Execute the tool with given parameters."""
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
            "hazmat": any(item.get("hazmat", False) for item in items)
        }

        inbound_shipments.append(new_shipment)

        return json.dumps(new_shipment, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Return tool specification for AI agent."""
        return {
            "type": "function",
            "function": {
                "name": "create_inbound_shipment",
                "description": "Creates a new inbound shipment record from a supplier to a warehouse.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {"type": "string", "description": "The ID of the supplier sending the shipment."},
                        "destination_warehouse_id": {"type": "string", "description": "The ID of the destination warehouse."},
                        "carrier_id": {"type": "string", "description": "The ID of the carrier transporting the shipment."},
                        "items": {
                            "type": "array",
                            "description": "A list of items in the shipment.",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "sku": {"type": "string", "description": "Product SKU."},
                                    "quantity": {"type": "integer", "description": "Number of units."}
                                },
                                "required": ["sku", "quantity"]
                            }
                        },
                        "estimated_arrival_date": {"type": "string", "description": "The estimated arrival date in YYYY-MM-DD format."}
                    },
                    "required": ["supplier_id", "destination_warehouse_id", "carrier_id", "items", "estimated_arrival_date"],
                },
            },
        }
