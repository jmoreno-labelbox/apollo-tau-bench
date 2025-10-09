from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetInboundShipmentDetails(Tool):
    """Utility for retrieving information about an inbound shipment."""

    @staticmethod
    def invoke(data: dict[str, Any], shipment_id: str) -> str:
        """Run the tool with the provided parameters."""
        shipments = data.get("inbound_shipments", [])
        for shipment in shipments:
            if shipment.get("shipment_id") == shipment_id:
                payload = shipment
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Shipment with ID {shipment_id} not found"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        """Provide the specifications of the tool for the AI agent."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetInboundShipmentDetails",
                "description": "Retrieves full details for a specific inbound shipment from a supplier.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "shipment_id": {
                            "type": "string",
                            "description": "The ID of the inbound shipment.",
                        }
                    },
                    "required": ["shipment_id"],
                },
            },
        }
