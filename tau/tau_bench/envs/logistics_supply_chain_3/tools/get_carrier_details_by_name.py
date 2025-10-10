# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCarrierDetailsByName(Tool):
    """Retrieves the full details for a carrier by its name."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        carrier_name = kwargs.get("carrier_name")
        carriers = list(data.get("carriers", {}).values())
        for carrier in carriers:
            if carrier.get("carrier_name") == carrier_name:
                return json.dumps(carrier)
        return json.dumps({"error": "Carrier not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_carrier_details_by_name",
                "description": "Retrieves the full record for a carrier by its exact name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "carrier_name": {
                            "type": "string",
                            "description": "The full name of the carrier.",
                        }
                    },
                    "required": ["carrier_name"],
                },
            },
        }
