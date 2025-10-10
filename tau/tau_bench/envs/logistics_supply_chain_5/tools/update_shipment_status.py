# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateShipmentStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], shipment_id: str, status: str) -> str:
        inbound_shipments = data.get("inbound_shipments", [])

        shipment = next((s for s in inbound_shipments if s.get("shipment_id") == shipment_id), None)
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
                "name": "update_shipment_status",
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
