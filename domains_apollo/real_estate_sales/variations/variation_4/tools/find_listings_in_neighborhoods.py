from tau_bench.envs.tool import Tool
import json
from typing import Any

class FindListingsInNeighborhoods(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], neighborhood_ids: list = None) -> str:
        neighborhood_ids = neighborhood_ids or []
        return FindListings.invoke(data, neighborhood_ids=neighborhood_ids)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "findListingsInNeighborhoods",
                "description": "Find listings within the provided neighborhoods.",
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
