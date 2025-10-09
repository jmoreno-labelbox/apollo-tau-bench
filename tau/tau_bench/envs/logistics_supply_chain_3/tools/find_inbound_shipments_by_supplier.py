from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class FindInboundShipmentsBySupplier(Tool):
    """Identifies all inbound shipments associated with a particular supplier ID."""

    @staticmethod
    def invoke(data: dict[str, Any], supplier_id: str = None) -> str:
        inbound_shipments = data.get("inbound_shipments", {}).values()
        found_shipments = []
        for shipment in inbound_shipments:
            if shipment.get("supplier_id") == supplier_id:
                found_shipments.append(shipment)
        if found_shipments:
            payload = found_shipments
            out = json.dumps(payload)
            return out
        payload = {"message": "No inbound shipments found for that supplier"}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindInboundShipmentsBySupplier",
                "description": "Finds all inbound shipments associated with a specific supplier ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_id": {
                            "type": "string",
                            "description": "The ID of the supplier (e.g., 'SUP-1001').",
                        }
                    },
                    "required": ["supplier_id"],
                },
            },
        }
