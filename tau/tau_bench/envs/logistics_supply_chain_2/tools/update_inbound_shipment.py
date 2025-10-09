from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateInboundShipment(Tool):
    """Utility for modifying details of inbound shipments."""

    @staticmethod
    def invoke(data: dict[str, Any], shipment_id: str = None, updates: dict[str, Any] = None) -> str:
        shipments = data.get("inbound_shipments", [])

        for shipment in shipments:
            if shipment["shipment_id"] == shipment_id:
                shipment.update(updates)
                payload = {"success": f"inbound shipment {shipment_id} updated"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": f"shipment_id {shipment_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateInboundShipment",
                "description": "Update inbound shipment by ID",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "shipment_id": {
                            "type": "string",
                            "description": "The inbound shipment ID to update",
                        },
                        "updates": {
                            "type": "object",
                            "description": "Fields and values to update",
                        },
                    },
                    "required": ["shipment_id", "updates"],
                },
            },
        }
