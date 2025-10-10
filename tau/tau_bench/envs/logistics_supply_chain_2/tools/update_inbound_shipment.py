# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateInboundShipment(Tool):
    """Tool to update inbound shipment information."""

    @staticmethod
    def invoke(data: Dict[str, Any], shipment_id, updates) -> str:
        shipments = list(data.get("inbound_shipments", {}).values())

        for shipment in shipments:
            if shipment["shipment_id"] == shipment_id:
                shipment.update(updates)
                return json.dumps({"success": f"inbound shipment {shipment_id} updated"}, indent=2)
        return json.dumps({"error": f"shipment_id {shipment_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_inbound_shipment",
                "description": "Update inbound shipment by ID",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "shipment_id": {"type": "string", "description": "The inbound shipment ID to update"},
                        "updates": {"type": "object", "description": "Fields and values to update"}
                    },
                    "required": ["shipment_id", "updates"]
                }
            }
        }
