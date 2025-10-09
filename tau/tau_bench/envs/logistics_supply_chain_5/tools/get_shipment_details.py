from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any, Dict



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetShipmentDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], shipment_id: str, inbound_shipments: list = None) -> str:
        if inbound_shipments is None:
            inbound_shipments = data.get("inbound_shipments", {}).values()

        shipment = next((s for s in inbound_shipments.values() if s.get("shipment_id") == shipment_id), None)

        if not shipment:
            return json.dumps({"error": f"Shipment {shipment_id} not found"})

        return json.dumps(shipment)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetShipmentDetails",
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
