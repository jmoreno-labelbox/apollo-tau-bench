from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class BuildFeaturesCsvPath(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], city_slug: str = None) -> str:
        if not city_slug:
            payload = {"error": "Missing city_slug"}
            out = json.dumps(payload)
            return out
        payload = {
            "city_slug": city_slug,
            "features_csv_path": "/processed_data/features.csv",
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "BuildFeaturesCsvPath",
                "description": "Returns canonical features CSV path for a city_slug.",
                "parameters": {
                    "type": "object",
                    "properties": {"city_slug": {"type": "string"}},
                    "required": ["city_slug"],
                },
            },
        }
