# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SetGeocodeCity(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        city_name = kwargs.get("city_name")

        results = list(data.get("geocoding_results", {}).values())
        for result in results:
            if result.get("query_city") == city_name:
                return json.dumps(result)
        json_city_path = "_".join(city_name.split()).lower()
        result = {
            "geo_id": "GEO_001",
            "query_city": city_name,
            "latitude": LAT,
            "longitude": LONG,
            "raw_json_path_nullable": f"/data/raw/geocoding_{json_city_path}.json",
        }
        list(data.get("geocoding_results", {}).values()).append(result)
        return json.dumps(result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SetGeocodeCity",
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
