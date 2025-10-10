# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCarriersByRegion(Tool):
    """Tool to retrieve carriers by region."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        carriers = list(data.get("carriers", {}).values())
        region = kwargs.get("region", None)
        list_of_carriers = kwargs.get("list_of_scacs", None)
        if region:
            active_carriers = [carrier['scac'] for carrier in carriers if carrier.get("active_status") and region.lower() in carrier.get("regional_coverage").lower()]
        else:
            active_carriers = [carrier['scac'] for carrier in carriers if carrier.get("active_status")]
        if list_of_carriers:
            active_carriers = [carrier for carrier in active_carriers if carrier in list_of_carriers]
        return json.dumps(active_carriers, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_carriers_by_region",
                "description": "Retrieve all active carriers.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "region": {
                            "type": "string",
                            "description": "Region eg. Global"
                        },
                        "list_of_scacs": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "description": "List of SCACs to choose from."
                        }
                    }
                }
            }
        }
