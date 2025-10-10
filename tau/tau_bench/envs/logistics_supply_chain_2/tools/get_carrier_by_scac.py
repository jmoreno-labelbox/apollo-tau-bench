# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCarrierBySCAC(Tool):
    """Tool to retrieve details of a carrier by carrier SCAC."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        carrier_scac = kwargs.get("carrier_scac")
        carriers = list(data.get("carriers", {}).values())
        for carrier in carriers:
            if carrier["scac"] == carrier_scac:
                return json.dumps(carrier, indent=2)
        return json.dumps({"error": f"Carrier with scac {carrier_scac} not found."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_carrier_by_scac",
                "description": "Retrieve Carrier details by carrier SCAC.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "carrier_scac": {
                            "type": "string",
                            "description": "Unique Carrier identifier."
                        }
                    },
                    "required": ["carrier_scac"]
                }
            }
        }
