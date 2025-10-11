# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from datetime import datetime


def get_current_timestamp() -> str:
    return "2025-07-31T12:00:00.000000"

def get_current_timestamp_object() -> datetime:
    return datetime.strptime(get_current_timestamp(), "%Y-%m-%dT%H:%M:%S.%f")

def get_current_year_month_day() -> str:
    return "2025-07-31"

def generate_unique_id() -> str:
    return 'fd520c73'

class UpdateCustomsStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], shipment_id: str, status: str) -> str:
        inbound_shipments = list(data.get("inbound_shipments", {}).values())

        shipment = next((s for s in inbound_shipments if s.get("shipment_id") == shipment_id), None)
        if not shipment:
            return json.dumps({"error": f"Shipment {shipment_id} not found"})

        old_status = shipment.get("customs_clearance_status")
        shipment["customs_clearance_status"] = status

        if status == "Cleared":
            shipment["customs_clearance_date"] = get_current_timestamp()
            shipment["customs_entry_number"] = f"US-{shipment_id}"

        return json.dumps({
            "shipment_id": shipment_id,
            "old_customs_status": old_status,
            "new_customs_status": status,
            "customs_entry_number": shipment.get("customs_entry_number")
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_customs_status",
                "description": "Update customs clearance status for a shipment",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "shipment_id": {"type": "string", "description": "Shipment identifier"},
                        "status": {"type": "string", "description": "New customs status"}
                    },
                    "required": ["shipment_id", "status"]
                }
            }
        }
