from tau_bench.envs.tool import Tool
import json
from typing import Any

class UpdateInboundShipment(Tool):
    """Utility for modifying information related to an inbound shipment."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        shipment_id: str,
        destination_warehouse_id: str | None = None,
        destination_warehouse_name: str | None = None,
        destination_address: str | None = None,
        destination_city: str | None = None,
        estimated_arrival_date: str | None = None,
        status: str | None = None,
        carrier_id: str | None = None,
        carrier_name: str | None = None,
        carrier_scac: str | None = None
    ) -> str:
        """Run the tool using the specified parameters."""
        shipments = data.get("inbound_shipments", [])
        for shipment in shipments:
            if shipment.get("shipment_id") == shipment_id:
                # if shipment["status"] is not among ["In Transit", "Delayed"]:
                # return json.dumps({"error": f"Shipment {shipment_id} cannot be modified due to status '{shipment['status']}'"}, indent=2)
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
                payload = {"shipment_id": shipment_id, "updated_details": shipment}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": f"Shipment with ID {shipment_id} not found"}
        out = json.dumps(
            payload, indent=2
        )
        return out
        """Run the tool using the specified parameters."""
        pass
        shipments = data.get("inbound_shipments", [])
        for shipment in shipments:
            if shipment.get("shipment_id") == shipment_id:
                #if shipment["status"] is not among ["In Transit", "Delayed"]:
                #return json.dumps({"error": f"Shipment {shipment_id} cannot be modified due to status '{shipment['status']}'"}, indent=2)
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
                payload = {"shipment_id": shipment_id, "updated_details": shipment}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        payload = {"error": f"Shipment with ID {shipment_id} not found"}
        out = json.dumps(
            payload, indent=2
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        """Provide tool specifications for the AI agent."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "UpdateInboundShipment",
                "description": "Updates the details of an in-transit or delayed inbound shipment.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "shipment_id": {
                            "type": "string",
                            "description": "The ID of the shipment to update.",
                        },
                        "destination_warehouse_id": {
                            "type": "string",
                            "description": "The new destination warehouse ID.",
                        },
                        "destination_warehouse_name": {
                            "type": "string",
                            "description": "The new destination warehouse name.",
                        },
                        "destination_address": {
                            "type": "string",
                            "description": "The new destination address.",
                        },
                        "destination_city": {
                            "type": "string",
                            "description": "The new destination city.",
                        },
                        "estimated_arrival_date": {
                            "type": "string",
                            "description": "The new estimated arrival date in YYYY-MM-DD format.",
                        },
                        "status": {
                            "type": "string",
                            "description": "The new status of the shipment (e.g., 'Delayed').",
                        },
                        "carrier_id": {
                            "type": "string",
                            "description": "The new carrier ID of the shipment.",
                        },
                        "carrier_name": {
                            "type": "string",
                            "description": "The new carrier name of the shipment.",
                        },
                        "carrier_scac": {
                            "type": "string",
                            "description": "The new carrier SCAC of the shipment.",
                        },
                    },
                    "required": ["shipment_id"],
                },
            },
        }
