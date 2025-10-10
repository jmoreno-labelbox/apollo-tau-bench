# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetShipmentDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], shipment_id: str) -> str:
        inbound_shipments = data.get("inbound_shipments", [])

        shipment = next((s for s in inbound_shipments if s.get("shipment_id") == shipment_id), None)

        if not shipment:
            return json.dumps({"error": f"Shipment {shipment_id} not found"})

        return json.dumps(shipment)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_shipment_details",
                "description": "Retrieve detailed information about a specific shipment",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "shipment_id": {"type": "string", "description": "Shipment identifier"}
                    },
                    "required": ["shipment_id"]
                }
            }
        }
