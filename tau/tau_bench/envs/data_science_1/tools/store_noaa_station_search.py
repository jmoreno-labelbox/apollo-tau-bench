from tau_bench.envs.tool import Tool
import json
from typing import Any

class StoreNoaaStationSearch(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        query_latitude: float = None,
        query_longitude: float = None,
        query_ts: str = None,
        radius_km: float = None,
        raw_json_path_nullable: str = None,
        station_distances_km: list[float] = None,
        station_ids: list[str] = None,
        station_latitudes: list[float] = None,
        station_longitudes: list[float] = None,
        station_names: list[str] = None,
        station_types_nullable: list[str] = None
    ) -> str:
        req = ["query_latitude", "query_longitude", "station_ids"]
        err = _require(locals(), req)
        if err:
            return err
        row = {
            "query_latitude": query_latitude,
            "query_longitude": query_longitude,
            "radius_km": radius_km,
            "station_ids": station_ids,
            "station_names": station_names,
            "station_distances_km": station_distances_km,
            "station_latitudes": station_latitudes,
            "station_longitudes": station_longitudes,
            "station_types_nullable": station_types_nullable,
            "raw_json_path_nullable": raw_json_path_nullable,
            "query_ts": query_ts,
        }
        payload = _append(data.setdefault("noaa_station_searches", []), row)
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "StoreNoaaStationSearch",
                "description": "Stores results of a NOAA tide-station proximity search.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query_latitude": {"type": "number"},
                        "query_longitude": {"type": "number"},
                        "radius_km": {"type": "number"},
                        "station_ids": {"type": "array", "items": {"type": "string"}},
                        "station_names": {"type": "array", "items": {"type": "string"}},
                        "station_distances_km": {
                            "type": "array",
                            "items": {"type": "number"},
                        },
                        "station_latitudes": {
                            "type": "array",
                            "items": {"type": "number"},
                        },
                        "station_longitudes": {
                            "type": "array",
                            "items": {"type": "number"},
                        },
                        "station_types_nullable": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "raw_json_path_nullable": {"type": "string"},
                        "query_ts": {"type": "string"},
                    },
                    "required": ["query_latitude", "query_longitude", "station_ids"],
                },
            },
        }
