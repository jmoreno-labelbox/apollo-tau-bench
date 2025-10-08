from tau_bench.envs.tool import Tool
import json
from typing import Any

class RecordGeocodingResult(Tool):
    """Adds a geocoding_results record."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        query_city: str,
        latitude: float,
        longitude: float,
        canonical_name: str,
        provider: str,
        query_ts: str
    ) -> str:
        record = {
            "query_city": query_city,
            "latitude": latitude,
            "longitude": longitude,
            "canonical_name": canonical_name,
            "provider": provider,
            "query_ts": query_ts
        }
        if not {
            "query_city",
            "latitude",
            "longitude",
            "canonical_name",
            "provider",
            "query_ts",
        }.issubset(set(record.keys())):
            payload = {"error": "missing required fields"}
            out = json.dumps(payload)
            return out
        data.setdefault("geocoding_results", []).append(record)
        payload = {"status": "inserted", "record": record}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "recordGeocodingResult",
                "description": "Appends a geocoding_results record.",
                "parameters": {
                    "type": "object",
                    "properties": {"record": {"type": "object"}},
                    "required": ["record"],
                },
            },
        }
