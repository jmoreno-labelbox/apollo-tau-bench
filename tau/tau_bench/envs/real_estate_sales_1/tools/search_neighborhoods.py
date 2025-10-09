from tau_bench.envs.tool import Tool
import json
from typing import Any

class SearchNeighborhoods(Tool):
    """Look for neighborhoods according to specified criteria."""

    @staticmethod
    def invoke(data: dict[str, Any], city: str = None, min_avg_price: float = 0, max_avg_price: float = float("inf"),
    neighborhood_name: Any = None,
    ) -> str:
        neighborhoods = data.get("neighborhoods", [])
        results = []

        for neighborhood in neighborhoods:
            avg_price = neighborhood.get("avg_home_price", 0)
            if city and city.lower() not in neighborhood.get("city", "").lower():
                continue
            if not (min_avg_price <= avg_price <= max_avg_price):
                continue
            results.append(neighborhood)
        payload = {
                "search_criteria": {
                    "city": city,
                    "min_avg_price": min_avg_price,
                    "max_avg_price": max_avg_price,
                },
                "neighborhood_count": len(results),
                "neighborhoods": results,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchNeighborhoods",
                "description": "Search for neighborhoods based on criteria",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "city": {"type": "string", "description": "City to search CO"},
                        "min_avg_price": {
                            "type": "number",
                            "description": "Minimum average home price",
                        },
                        "max_avg_price": {
                            "type": "number",
                            "description": "Maximum average home price",
                        },
                    },
                    "required": [],
                },
            },
        }
