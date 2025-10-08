from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class BuildProcessedTimeseriesPath(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], city_slug: str = None) -> str:
        if not city_slug:
            payload = {"error": "Missing city_slug"}
            out = json.dumps(payload)
            return out
        path = f"/data/processed/timeseries_{city_slug}_weather.csv"
        payload = {"city_slug": city_slug, "csv_path": path}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "BuildProcessedTimeseriesPath",
                "description": "Builds canonical processed timeseries CSV path for a given city_slug.",
                "parameters": {
                    "type": "object",
                    "properties": {"city_slug": {"type": "string"}},
                    "required": ["city_slug"],
                },
            },
        }
