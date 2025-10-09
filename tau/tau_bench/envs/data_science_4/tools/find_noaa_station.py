from tau_bench.envs.tool import Tool
import json
from typing import Any

class FindNoaaStation(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], latitude: float = None, longitude: float = None) -> str:
        station_id = "NOAA_STATION_001"
        noaa_station_json = {
            "station_ids": station_id,
            "raw_json_path_nullable": f"/data/raw/noaa_station_{station_id}.json",
        }
        data.get("noaa_station_searches", []).append(noaa_station_json)
        payload = noaa_station_json
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "findNoaaStation",
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
