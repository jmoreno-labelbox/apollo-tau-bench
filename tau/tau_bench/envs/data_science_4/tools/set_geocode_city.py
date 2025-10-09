from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class SetGeocodeCity(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], city_name: str) -> str:
        results = data.get("geocoding_results", {}).values()
        for result in results:
            if result.get("query_city") == city_name:
                payload = result
                out = json.dumps(payload)
                return out
        json_city_path = "_".join(city_name.split()).lower()
        result = {
            "geo_id": "GEO_001",
            "query_city": city_name,
            "latitude": LAT,
            "longitude": LONG,
            "raw_json_path_nullable": f"/data/raw/geocoding_{json_city_path}.json",
        }
        data["geocoding_results"][result["geocoding_result_id"]] = result
        payload = result
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "setGeocodeCity",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "city_name": {
                            "type": "string",
                            "description": "The name of the city.",
                        }
                    },
                    "required": ["city_name"],
                },
            },
        }
