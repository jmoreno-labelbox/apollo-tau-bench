from tau_bench.envs.tool import Tool
import json
import random
from typing import Any

class FindInboundShipment(Tool):
    """Locates a particular inbound shipment according to supplier and origin."""

    @staticmethod
    def invoke(data: dict[str, Any], supplier_name: str = None, origin_city: str = None, status: str = None) -> str:
        if not all([supplier_name, origin_city]):
            payload = {"error": "supplier_name and origin_city are required arguments."}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        shipments = data.get("inbound_shipments", [])
        results = [
            s
            for s in shipments
            if s.get("supplier_name") == supplier_name
            and s.get("origin_city") == origin_city
            and (not status or s.get("status") == status)
        ]
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindInboundShipment",
                "description": "Finds inbound shipments from a specific supplier and origin city, optionally filtering by status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "supplier_name": {"type": "string"},
                        "origin_city": {"type": "string"},
                        "status": {
                            "type": "string",
                            "description": "Optional status to filter by (e.g., 'In Transit').",
                        },
                    },
                    "required": ["supplier_name", "origin_city"],
                },
            },
        }
