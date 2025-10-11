# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require






def _require(kwargs: Dict[str, Any], required: List[str]) -> Optional[str]:
    missing = [k for k in required if kwargs.get(k) is None]
    if missing:
        return json.dumps({"error": f"Missing required arguments: {', '.join(missing)}"}, indent=2)
    return None

def _append(table: List[Dict[str, Any]], row: Dict[str, Any]) -> Dict[str, Any]:
    table.append(row)
    return row

class StoreGeocodingResult(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], canonical_name, latitude, longitude, query_city, query_ts, raw_json_path_nullable) -> str:
        req = ["query_city", "latitude", "longitude"]
        err = _require(kwargs, req)
        if err: return err
        row = {
            "query_city": query_city,
            "latitude": latitude, "longitude": longitude,
            "canonical_name": canonical_name,
            "provider": "open-meteo",
            "raw_json_path_nullable": raw_json_path_nullable,
            "query_ts": query_ts
        }
        return json.dumps(_append(data.setdefault("geocoding_results", []), row), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "store_geocoding_result",
            "description": "Adds a geocoding row for the target city.",
            "parameters": {"type": "object", "properties": {
                "query_city": {"type": "string"}, "latitude": {"type": "number"}, "longitude": {"type": "number"},
                "canonical_name": {"type": "string"}, "raw_json_path_nullable": {"type": "string"},
                "query_ts": {"type": "string"}}, "required": ["query_city", "latitude", "longitude"]}}}