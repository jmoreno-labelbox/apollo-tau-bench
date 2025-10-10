# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCarriersByMode(Tool):
    """Tool to retrieve carriers by supported mode."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        carriers = data.get("carriers", [])
        mode = kwargs.get("mode", None)
        list_of_carriers = kwargs.get("list_of_scacs", None)
        if mode:
            active_carriers = [carrier['scac'] for carrier in carriers if carrier.get("active_status") and mode in carrier.get("supported_modes")]
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
                "name": "get_carriers_by_mode",
                "description": "Retrieve all active carriers.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "mode": {
                            "type": "string",
                            "description": "Mode eg. Air, Sea, Truck"
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
