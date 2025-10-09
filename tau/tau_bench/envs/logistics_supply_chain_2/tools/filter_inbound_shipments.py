from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class FilterInboundShipments(Tool):
    """Utility for fetching inbound shipments based on specific key-value pairs."""

    @staticmethod
    def invoke(data: dict[str, Any], key: str, value: str, list_of_ids: list[str] = None) -> str:
        shipments = data.get("inbound_shipments", [])
        result = [
            item["shipment_id"]
            for item in shipments
            if item[key].lower() == value.lower()
        ]
        if list_of_ids:
            result = [r for r in result if r in list_of_ids]
        if result:
            payload = {key: value, "result": result}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"error": f"No matching shipments found for {key} {value}"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FilterInboundShipments",
                "description": "Retrieve inbound shipments based on key and value.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_of_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of shipments to choose from.",
                        },
                        "key": {
                            "type": "string",
                            "description": "Key to consider like carrier_scac.",
                        },
                        "value": {
                            "type": "string",
                            "description": "Value to consider for this skey.",
                        },
                    },
                },
            },
        }
