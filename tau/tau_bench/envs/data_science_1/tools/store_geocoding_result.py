# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require


class StoreGeocodingResult(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        req = ["query_city", "latitude", "longitude"]
        err = _require(kwargs, req)
        if err: return err
        row = {
            "query_city": kwargs["query_city"],
            "latitude": kwargs["latitude"], "longitude": kwargs["longitude"],
            "canonical_name": kwargs.get("canonical_name"),
            "provider": "open-meteo",
            "raw_json_path_nullable": kwargs.get("raw_json_path_nullable"),
            "query_ts": kwargs.get("query_ts")
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
