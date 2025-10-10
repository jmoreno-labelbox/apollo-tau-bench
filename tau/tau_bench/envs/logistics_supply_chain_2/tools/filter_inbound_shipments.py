# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FilterInboundShipments(Tool):
    """Tool to retrieve inbound shipments by key and value."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        shipments = data.get("inbound_shipments", [])
        key = kwargs.get("key")
        value = kwargs.get("value")
        list_of_shipments = kwargs.get("list_of_ids", None)
        result = [item['shipment_id'] for item in shipments if item[key].lower() == value.lower()]
        if list_of_shipments:
            result = [r for r in result if r in list_of_shipments]
        if result:
            return json.dumps({key: value, 'result': result}, indent=2)
        return json.dumps({"error": f"No matching shipments found for {key} {value}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "filter_inbound_shipments",
                "description": "Retrieve inbound shipments based on key and value.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_of_ids": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "description": "List of shipments to choose from."
                        },
                        "key": {
                            "type": "string",
                            "description": "Key to consider like carrier_scac."
                        },
                        "value": {
                            "type": "string",
                            "description": "Value to consider for this skey."
                        }
                    }
                }
            }
        }
