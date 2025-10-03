from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class BuildMetricsSummaryPath(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], model_name: str = None, end_ts: str = None) -> str:
        if not model_name or not end_ts:
            payload = {"error": "Missing model_name or end_ts"}
            out = json.dumps(payload)
            return out
        y1 = end_ts[:10].replace("-", "")
        payload = {
                "metrics_summary_path": f"/processed_data/metrics_summary_{model_name}_{y1}.csv"
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "BuildMetricsSummaryPath",
                "description": "Builds canonical metrics summary CSV path from model_name and end_ts.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "model_name": {"type": "string"},
                        "end_ts": {"type": "string"},
                    },
                    "required": ["model_name", "end_ts"],
                },
            },
        }
