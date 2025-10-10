# Copyright Sierra Inc.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetStationsByLocation(Tool):
    """
    Returns a noaa_station_searches record by exact latitude, longitude, and radius_km.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], query_latitude: float, query_longitude: float, radius_km: float) -> str:
        rows = list(data.get("noaa_station_searches", {}).values())
        for row in rows:
            if row.get("query_latitude") == query_latitude and row.get("query_longitude") == query_longitude and row.get("radius_km") == radius_km:
                return json.dumps(row)
        return json.dumps({"error": "station search not found", "query_latitude": query_latitude, "query_longitude": query_longitude, "radius_km": radius_km})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_stations_by_location",
                "description": "Returns a noaa_station_searches record by exact query coordinates and radius.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query_latitude": {"type": "number"},
                        "query_longitude": {"type": "number"},
                        "radius_km": {"type": "number"}
                    },
                    "required": ["query_latitude", "query_longitude", "radius_km"]
                }
            }
        }
