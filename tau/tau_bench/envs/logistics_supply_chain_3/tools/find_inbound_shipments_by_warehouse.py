from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class FindInboundShipmentsByWarehouse(Tool):
    """Locates all inbound shipments intended for a particular warehouse ID."""

    @staticmethod
    def invoke(data: dict[str, Any], warehouse_id: str = None) -> str:
        inbound_shipments = data.get("inbound_shipments", {}).values()
        found_shipments = []
        for shipment in inbound_shipments:
            dest_id = shipment.get("destination_warehouse_id") or shipment.get(
                "destination_warehouse_id"
            )
            if dest_id == warehouse_id:
                found_shipments.append(shipment)
        if found_shipments:
            payload = found_shipments
            out = json.dumps(payload)
            return out
        payload = {"message": "No inbound shipments found for that warehouse"}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindInboundShipmentsByWarehouse",
                "description": "Finds all inbound shipments, including their status and expected arrival date, destined for a specific warehouse ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "warehouse_id": {
                            "type": "string",
                            "description": "The ID of the destination warehouse (e.g., 'WH-01').",
                        }
                    },
                    "required": ["warehouse_id"],
                },
            },
        }
