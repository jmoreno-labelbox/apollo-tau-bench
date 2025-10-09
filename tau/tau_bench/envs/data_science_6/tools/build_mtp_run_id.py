from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class BuildMtpRunId(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], city_slug: str = None, model_name: str = None, start_ts: str = None, end_ts: str = None) -> str:
        if not city_slug or not model_name or not start_ts or not end_ts:
            payload = {"error": "Missing city_slug, model_name, start_ts, or end_ts"}
            out = json.dumps(payload)
            return out
        y0 = start_ts[:10].replace("-", "")
        y1 = end_ts[:10].replace("-", "")
        payload = {"run_id": f"mt_{city_slug}_{model_name}_{y0}_{y1}_v1"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "BuildMtpRunId",
                "description": "Builds canonical MTP run_id from city_slug, model_name, and analysis window.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "city_slug": {"type": "string"},
                        "model_name": {"type": "string"},
                        "start_ts": {"type": "string"},
                        "end_ts": {"type": "string"},
                    },
                    "required": ["city_slug", "model_name", "start_ts", "end_ts"],
                },
            },
        }
