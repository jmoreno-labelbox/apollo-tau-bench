# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindNoaaStation(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], latitude, longitude) -> str:
        lat = latitude
        lon = longitude

        station_id = "NOAA_STATION_001"
        noaa_station_json = {
            "station_ids": station_id,
            "raw_json_path_nullable": f"/data/raw/noaa_station_{station_id}.json",
        }
        list(data.get("noaa_station_searches", {}).values()).append(noaa_station_json)
        return json.dumps(noaa_station_json)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindNoaaStation",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "latitude": {
                            "type": "number",
                            "description": "The latitude of the search area.",
                        },
                        "longitude": {
                            "type": "number",
                            "description": "The longitude of the search area.",
                        },
                        "radius_km": {
                            "type": "number",
                            "description": "The search radius in kilometers.",
                        },
                    },
                    "required": ["latitude", "longitude"],
                },
            },
        }
