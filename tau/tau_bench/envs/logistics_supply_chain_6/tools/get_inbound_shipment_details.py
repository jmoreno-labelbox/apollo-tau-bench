# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetInboundShipmentDetails(Tool):
    """Tool to get details of an inbound shipment."""

    @staticmethod
    def invoke(data: Dict[str, Any], shipment_id: str) -> str:
        """Execute the tool with given parameters."""
        shipments = data.get("inbound_shipments", [])
        for shipment in shipments:
            if shipment.get("shipment_id") == shipment_id:
                return json.dumps(shipment, indent=2)
        return json.dumps({"error": f"Shipment with ID {shipment_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Return tool specification for AI agent."""
        return {
            "type": "function",
            "function": {
                "name": "get_inbound_shipment_details",
                "description": "Retrieves full details for a specific inbound shipment from a supplier.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "shipment_id": {"type": "string", "description": "The ID of the inbound shipment."}
                    },
                    "required": ["shipment_id"],
                },
            },
        }
