# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetTopRatedCarriers(Tool):
    """Tool to return carriers sorted by highest average_rating."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        carriers = data.get("carriers", [])
        list_of_carriers = kwargs.get("list_of_scacs", None)
        sorted_carriers = sorted(
            carriers,
            key=lambda c: c.get("performance_metrics", {}).get("average_rating", 0),
            reverse=True
        )
        if list_of_carriers:
            return json.dumps([[sc['scac'], sc['performance_metrics']['average_rating']] for sc in sorted_carriers if sc['scac'] in list_of_carriers],
                              indent=2)
        return json.dumps([[sc['scac'], sc['performance_metrics']['average_rating']] for sc in sorted_carriers], indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_top_rated_carriers",
                "description": "Retrieve carriers sorted by highest average rating.",
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
