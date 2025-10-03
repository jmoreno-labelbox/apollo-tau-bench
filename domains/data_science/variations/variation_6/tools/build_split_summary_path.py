from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class BuildSplitSummaryPath(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], city_slug: str = None, method: str = None, split_ts: str = None) -> str:
        if not city_slug or not method or not split_ts:
            payload = {"error": "Missing city_slug, method, or split_ts"}
            out = json.dumps(payload)
            return out
        ymd = split_ts[:10].replace("-", "")
        path = f"/data/splits/{city_slug}_{method}_split_{ymd}.json"
        payload = {
            "city_slug": city_slug,
            "method": method,
            "split_ts": split_ts,
            "split_summary_json_path": path,
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "BuildSplitSummaryPath",
                "description": "Builds canonical split_summary_json_path from city_slug, method, and split_ts.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "city_slug": {"type": "string"},
                        "method": {"type": "string"},
                        "split_ts": {"type": "string"},
                    },
                    "required": ["city_slug", "method", "split_ts"],
                },
            },
        }
