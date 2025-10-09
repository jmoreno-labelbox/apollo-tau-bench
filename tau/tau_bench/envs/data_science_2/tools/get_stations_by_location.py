from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetStationsByLocation(Tool):
    """Provides a noaa_station_searches record based on precise latitude, longitude, and radius_km."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        query_latitude: float,
        query_longitude: float,
        radius_km: float,
    ) -> str:
        rows = data.get("noaa_station_searches", [])
        for row in rows:
            if (
                row.get("query_latitude") == query_latitude
                and row.get("query_longitude") == query_longitude
                and row.get("radius_km") == radius_km
            ):
                payload = row
                out = json.dumps(payload)
                return out
        payload = {
            "error": "station search not found",
            "query_latitude": query_latitude,
            "query_longitude": query_longitude,
            "radius_km": radius_km,
        }
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetStationsByLocation",
                "description": "Returns a noaa_station_searches record by exact query coordinates and radius.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query_latitude": {"type": "number"},
                        "query_longitude": {"type": "number"},
                        "radius_km": {"type": "number"},
                    },
                    "required": ["query_latitude", "query_longitude", "radius_km"],
                },
            },
        }
