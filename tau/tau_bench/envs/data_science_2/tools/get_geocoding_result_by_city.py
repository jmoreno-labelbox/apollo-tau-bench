from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetGeocodingResultByCity(Tool):
    """Fetches geocoding_results based on query_city."""

    @staticmethod
    def invoke(data: dict[str, Any], query_city: str) -> str:
        rows = data.get("geocoding_results", [])
        for row in rows:
            if row.get("query_city") == query_city:
                payload = row
                out = json.dumps(payload)
                return out
        payload = {"error": "geocoding result not found", "query_city": query_city}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetGeocodingResultByCity",
                "description": "Retrieves a geocoding result by query_city.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query_city": {
                            "type": "string",
                            "description": "City name used in geocoding query.",
                        }
                    },
                    "required": ["query_city"],
                },
            },
        }
