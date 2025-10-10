# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetShipmentsByStatus(Tool):
    """Tool to retrieve shipments filtered by status (e.g., 'In Transit', 'Received')."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        status = kwargs.get("status", "").lower()
        list_of_shipments = kwargs.get("list_of_ids", None)
        shipments = data.get("inbound_shipments", [])
        filtered = [s['shipment_id'] for s in shipments if s.get("status", "").lower() == status]
        if list_of_shipments:
            filtered = [s for s in filtered if s in list_of_shipments]
        return json.dumps(filtered, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_shipments_by_status",
                "description": "Retrieve shipments filtered by status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {
                            "type": "string",
                            "description": "Shipment status to filter by (e.g., 'In Transit')."
                        },
                        "list_of_ids": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "description": "List of shipments to choose from."
                        }
                    },
                    "required": ["status"]
                }
            }
        }
