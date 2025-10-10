# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetShipmentById(Tool):
    """Tool to retrieve details of a shipment by shipment ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        shipment_id = kwargs.get("shipment_id")
        shipments = data.get("inbound_shipments", [])
        for shipment in shipments:
            if shipment["shipment_id"] == shipment_id:
                return json.dumps(shipment, indent=2)
        return json.dumps({"error": f"Shipment with ID {shipment_id} not found."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_shipment_by_id",
                "description": "Retrieve shipment details by shipment ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "shipment_id": {
                            "type": "string",
                            "description": "Unique shipment identifier (e.g., 'SHIP-0012')."
                        }
                    },
                    "required": ["shipment_id"]
                }
            }
        }
