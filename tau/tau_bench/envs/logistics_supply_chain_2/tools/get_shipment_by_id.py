from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetShipmentById(Tool):
    """Utility for obtaining shipment information using the shipment ID."""

    @staticmethod
    def invoke(data: dict[str, Any], shipment_id: str) -> str:
        shipments = data.get("inbound_shipments", {}).values()
        for shipment in shipments.values():
            if shipment["shipment_id"] == shipment_id:
                payload = shipment
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Shipment with ID {shipment_id} not found."}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetShipmentById",
                "description": "Retrieve shipment details by shipment ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "shipment_id": {
                            "type": "string",
                            "description": "Unique shipment identifier (e.g., 'SHIP-0012').",
                        }
                    },
                    "required": ["shipment_id"],
                },
            },
        }
