from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class GetTopRatedCarriers(Tool):
    """Utility for listing carriers arranged by their highest average rating."""

    @staticmethod
    def invoke(data: dict[str, Any], list_of_scacs: list[str] = None) -> str:
        carriers = data.get("carriers", [])
        sorted_carriers = sorted(
            carriers,
            key=lambda c: c.get("performance_metrics", {}).get("average_rating", 0),
            reverse=True,
        )
        if list_of_scacs:
            payload = [
                [sc["scac"], sc["performance_metrics"]["average_rating"]]
                for sc in sorted_carriers
                if sc["scac"] in list_of_scacs
            ]
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = [
            [sc["scac"], sc["performance_metrics"]["average_rating"]]
            for sc in sorted_carriers
        ]
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTopRatedCarriers",
                "description": "Retrieve carriers sorted by highest average rating.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "list_of_scacs": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of carriers to choose from.",
                        }
                    },
                },
            },
        }
