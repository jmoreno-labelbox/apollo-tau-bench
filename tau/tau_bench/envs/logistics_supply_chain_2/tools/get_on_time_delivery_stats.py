# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetOnTimeDeliveryStats(Tool):
    """Tool to calculate average on-time delivery percentage across all carriers."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        carriers = data.get("carriers", [])
        list_of_carriers = kwargs.get("list_of_scacs", None)
        if not carriers:
            return json.dumps({"average_on_time_delivery": 0.0}, indent=2)
        if list_of_carriers:
            carriers = [c for c in carriers if c["scac"] in list_of_carriers]
        total = sum(c.get("performance_metrics", {}).get("on_time_delivery_percentage", 0) for c in carriers)
        average = total / len(carriers)
        return json.dumps({"average_on_time_delivery": average}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_on_time_delivery_stats",
                "description": "Calculate average on-time delivery percentage across all carriers.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_of_scacs": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            },
                            "description": "List of carriers to choose from."
                        }
                    }
                }
            }
        }
