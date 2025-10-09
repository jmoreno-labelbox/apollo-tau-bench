from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any, Dict



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateShipmentStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], shipment_id: str, status: str) -> str:
        inbound_shipments = data.get("inbound_shipments", {}).values()

        shipment = next((s for s in inbound_shipments.values() if s.get("shipment_id") == shipment_id), None)
        if not shipment:
            return json.dumps({"error": f"Shipment {shipment_id} not found"})

        old_status = shipment.get("status")
        shipment["status"] = status
        shipment["last_updated"] = get_current_timestamp()

        if status == "Received":
            shipment["actual_arrival_date"] = get_current_year_month_day()

        return json.dumps({
            "shipment_id": shipment_id,
            "old_status": old_status,
            "new_status": status,
            "updated_timestamp": shipment["last_updated"]
        })
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateShipmentStatus",
                "description": "Update the status of an inbound shipment",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "shipment_id": {"type": "string", "description": "Shipment identifier"},
                        "status": {"type": "string", "description": "New shipment status"}
                    },
                    "required": ["shipment_id", "status"]
                }
            }
        }
