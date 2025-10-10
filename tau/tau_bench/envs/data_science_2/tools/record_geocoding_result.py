# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RecordGeocodingResult(Tool):
    """
    Appends a geocoding_results record.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], record: Dict[str, Any]) -> str:
        if not {"query_city", "latitude", "longitude", "canonical_name", "provider", "query_ts"}.issubset(set(record.keys())):
            return json.dumps({"error": "missing required fields"})
        data.setdefault("geocoding_results", []).append(record)
        return json.dumps({"status": "inserted", "record": record})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "record_geocoding_result",
                "description": "Appends a geocoding_results record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "record": {"type": "object"}
                    },
                    "required": ["record"]
                }
            }
        }
