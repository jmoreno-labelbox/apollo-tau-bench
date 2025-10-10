# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class StoreNoaaStationSearch(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        req = ["query_latitude", "query_longitude", "station_ids"]
        err = _require(kwargs, req)
        if err: return err
        row = {
            "query_latitude": kwargs["query_latitude"], "query_longitude": kwargs["query_longitude"],
            "radius_km": kwargs.get("radius_km"),
            "station_ids": kwargs["station_ids"],
            "station_names": kwargs.get("station_names"),
            "station_distances_km": kwargs.get("station_distances_km"),
            "station_latitudes": kwargs.get("station_latitudes"),
            "station_longitudes": kwargs.get("station_longitudes"),
            "station_types_nullable": kwargs.get("station_types_nullable"),
            "raw_json_path_nullable": kwargs.get("raw_json_path_nullable"),
            "query_ts": kwargs.get("query_ts")
        }
        return json.dumps(_append(data.setdefault("noaa_station_searches", []), row), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "store_noaa_station_search",
            "description": "Stores results of a NOAA tide-station proximity search.",
            "parameters": {"type": "object", "properties": {
                "query_latitude": {"type": "number"}, "query_longitude": {"type": "number"},
                "radius_km": {"type": "number"},
                "station_ids": {"type": "array", "items": {"type": "string"}},
                "station_names": {"type": "array", "items": {"type": "string"}},
                "station_distances_km": {"type": "array", "items": {"type": "number"}},
                "station_latitudes": {"type": "array", "items": {"type": "number"}},
                "station_longitudes": {"type": "array", "items": {"type": "number"}},
                "station_types_nullable": {"type": "array", "items": {"type": "string"}},
                "raw_json_path_nullable": {"type": "string"}, "query_ts": {"type": "string"}},
                "required": ["query_latitude", "query_longitude", "station_ids"]}}}
