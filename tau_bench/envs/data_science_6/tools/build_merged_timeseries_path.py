from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class BuildMergedTimeseriesPath(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], city_slug: str = None, start_ts: str = None, end_ts: str = None) -> str:
        if not city_slug or not start_ts or not end_ts:
            payload = {"error": "Missing city_slug, start_ts, end_ts"}
            out = json.dumps(payload)
            return out
        y0 = start_ts[:10].replace("-", "")
        y1 = end_ts[:10].replace("-", "")
        payload = {
                "merged_timeseries_path": f"/processed_data/merged_timeseries_{city_slug}_{y0}_{y1}.csv"
            }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "BuildMergedTimeseriesPath",
                "description": "Builds canonical merged timeseries path from city_slug and analysis window.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "city_slug": {"type": "string"},
                        "start_ts": {"type": "string"},
                        "end_ts": {"type": "string"},
                    },
                    "required": ["city_slug", "start_ts", "end_ts"],
                },
            },
        }
