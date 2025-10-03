from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetTrends(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], time_windows: list = None, min_sample_size: int = 25) -> str:
        if time_windows is None:
            time_windows = []
        payload = {"trend_analysis": f"trends_min_{min_sample_size}"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        pass
        #return result
        return {
            "type": "function",
            "function": {
                "name": "findTrends",
                "description": "Examines performance trends across multiple time windows.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "time_windows": {"type": "array", "items": {"type": "integer"}},
                        "min_sample_size": {"type": "integer"},
                    },
                    "required": ["time_windows"],
                },
            },
        }
