# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetGeocodingResultByCity(Tool):
    """
    Retrieves geocoding_results by query_city.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], query_city: str) -> str:
        rows = data.get("geocoding_results", [])
        for row in rows:
            if row.get("query_city") == query_city:
                return json.dumps(row)
        return json.dumps({"error": "geocoding result not found", "query_city": query_city})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_geocoding_result_by_city",
                "description": "Retrieves a geocoding result by query_city.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query_city": {"type": "string", "description": "City name used in geocoding query."}
                    },
                    "required": ["query_city"]
                }
            }
        }
