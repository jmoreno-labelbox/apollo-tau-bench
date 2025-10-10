# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetActiveCarriers(Tool):
    """Tool to retrieve all active carriers."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        carriers = data.get("carriers", [])
        list_of_carriers = kwargs.get("list_of_scacs", None)
        if list_of_carriers:
            active_carriers = [carrier['scac'] for carrier in carriers if
                               carrier.get("active_status") and carrier['scac'] in list_of_carriers]
        else:
            active_carriers = [carrier['scac'] for carrier in carriers if carrier.get("active_status")]
        return json.dumps(active_carriers, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_active_carriers",
                "description": "Retrieve all active carriers.",
                "parameters": {
                    "type": "object",
                    "properties": {
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
