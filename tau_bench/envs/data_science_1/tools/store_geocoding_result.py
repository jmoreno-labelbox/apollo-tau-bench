from tau_bench.envs.tool import Tool
import json
from typing import Any

class StoreGeocodingResult(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        canonical_name: str = None,
        latitude: float = None,
        longitude: float = None,
        query_city: str = None,
        query_ts: str = None,
        raw_json_path_nullable: str = None
    ) -> str:
        req = ["query_city", "latitude", "longitude"]
        err = _require({"query_city": query_city, "latitude": latitude, "longitude": longitude}, req)
        if err:
            return err
        row = {
            "query_city": query_city,
            "latitude": latitude,
            "longitude": longitude,
            "canonical_name": canonical_name,
            "provider": "open-meteo",
            "raw_json_path_nullable": raw_json_path_nullable,
            "query_ts": query_ts,
        }
        payload = _append(data.setdefault("geocoding_results", []), row)
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "StoreGeocodingResult",
                "description": "Adds a geocoding row for the target city.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query_city": {"type": "string"},
                        "latitude": {"type": "number"},
                        "longitude": {"type": "number"},
                        "canonical_name": {"type": "string"},
                        "raw_json_path_nullable": {"type": "string"},
                        "query_ts": {"type": "string"},
                    },
                    "required": ["query_city", "latitude", "longitude"],
                },
            },
        }
