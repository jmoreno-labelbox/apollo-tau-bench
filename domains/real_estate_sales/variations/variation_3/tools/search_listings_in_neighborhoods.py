from tau_bench.envs.tool import Tool
import json
from typing import Any

class SearchListingsInNeighborhoods(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], neighborhood_ids: list = None,
    price_min: Any = None,
    beds: Any = None,
    property_type: Any = None,
    baths: Any = None,
    price_max: Any = None,
    limit: Any = None
    ) -> str:
        neighborhood_ids = neighborhood_ids or []
        return SearchListings.invoke(data, neighborhood_ids=neighborhood_ids)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchListingsInNeighborhoods",
                "description": "Search listings within the provided neighborhoods.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "neighborhood_ids": {
                            "type": "array",
                            "items": {"type": "integer"},
                        },
                        "price_min": {"type": "integer"},
                        "price_max": {"type": "integer"},
                        "beds": {"type": "integer"},
                        "baths": {"type": "integer"},
                        "limit": {"type": "integer"},
                    },
                    "required": ["neighborhood_ids"],
                },
            },
        }
