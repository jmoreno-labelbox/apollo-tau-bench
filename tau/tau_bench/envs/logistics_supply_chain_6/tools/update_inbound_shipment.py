# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateInboundShipment(Tool):
    """Tool to update details of an inbound shipment."""

    @staticmethod
    def invoke(data: Dict[str, Any], shipment_id: str, destination_warehouse_id: Optional[str] = None, destination_warehouse_name: Optional[str] = None, destination_address: Optional[str] = None, destination_city: Optional[str] = None, estimated_arrival_date: Optional[str] = None, status: Optional[str] = None, carrier_id: Optional[str] = None, carrier_name: Optional[str] = None, carrier_scac:
               Optional[str] = None) -> str:
        """Execute the tool with given parameters."""
        shipments = data.get("inbound_shipments", [])
        for shipment in shipments:
            if shipment.get("shipment_id") == shipment_id:
                # if shipment["status"] not in ["In Transit", "On Hold"]:
                # return json.dumps({"error": f"Unable to update shipment {shipment_id} with status '{shipment['status']}'"}, indent=2)
                if destination_warehouse_id:
                    shipment["destination_warehouse_id"] = destination_warehouse_id
                if destination_warehouse_name:
                    shipment["destination_warehouse_name"] = destination_warehouse_name
                if destination_address:
                    shipment["destination_address"] = destination_address
                if destination_city:
                    shipment["destination_city"] = destination_city
                if estimated_arrival_date:
                    shipment["estimated_arrival_date"] = estimated_arrival_date
                if status:
                    shipment["status"] = status
                if carrier_id:
                    shipment["carrier_id"] = carrier_id
                if carrier_name:
                    shipment["carrier_name"] = carrier_name
                if carrier_scac:
                    shipment["carrier_scac"] = carrier_scac
                return json.dumps({"shipment_id": shipment_id, "updated_details": shipment}, indent=2)
        return json.dumps({"error": f"Shipment with ID {shipment_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """Return tool specification for AI agent."""
        return {
            "type": "function",
            "function": {
                "name": "update_inbound_shipment",
                "description": "Updates the details of an in-transit or delayed inbound shipment.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "shipment_id": {"type": "string", "description": "The ID of the shipment to update."},
                        "destination_warehouse_id": {"type": "string", "description": "The new destination warehouse ID."},
                        "destination_warehouse_name": {"type": "string", "description": "The new destination warehouse name."},
                        "destination_address": {"type": "string", "description": "The new destination address."},
                        "destination_city": {"type": "string", "description": "The new destination city."},
                        "estimated_arrival_date": {"type": "string", "description": "The new estimated arrival date in YYYY-MM-DD format."},
                        "status": {"type": "string", "description": "The new status of the shipment (e.g., 'Delayed')."},
                        "carrier_id": {"type": "string", "description": "The new carrier ID of the shipment."},
                        "carrier_name": {"type": "string", "description": "The new carrier name of the shipment."},
                        "carrier_scac": {"type": "string", "description": "The new carrier SCAC of the shipment."},
                    },
                    "required": ["shipment_id"],
                },
            },
        }
