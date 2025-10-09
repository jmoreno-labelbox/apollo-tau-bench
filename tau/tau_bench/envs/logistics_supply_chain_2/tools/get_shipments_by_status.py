from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class GetShipmentsByStatus(Tool):
    """Utility for fetching shipments based on their status (e.g., 'In Transit', 'Received')."""

    @staticmethod
    def invoke(data: dict[str, Any], status: str = "", list_of_ids: list = None) -> str:
        status = status.lower()
        list_of_shipments = list_of_ids
        shipments = data.get("inbound_shipments", [])
        filtered = [
            s["shipment_id"] for s in shipments if s.get("status", "").lower() == status
        ]
        if list_of_shipments:
            filtered = [s for s in filtered if s in list_of_shipments]
        payload = filtered
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetShipmentsByStatus",
                "description": "Retrieve shipments filtered by status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {
                            "type": "string",
                            "description": "Shipment status to filter by (e.g., 'In Transit').",
                        },
                        "list_of_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of shipments to choose from.",
                        },
                    },
                    "required": ["status"],
                },
            },
        }
