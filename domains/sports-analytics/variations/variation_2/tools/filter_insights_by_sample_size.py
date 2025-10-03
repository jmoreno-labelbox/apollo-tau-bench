from tau_bench.envs.tool import Tool
import json
from typing import Any

class FilterInsightsBySampleSize(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], **kwargs) -> str:
        pass
        kwargs.get("min_sample_size", 25)
        kwargs.get("source_table", "")
        payload = {"filtered_insights": "flags_filtered_sample"}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FilterInsightsBySampleSize",
                "description": "Filters insights by minimum sample size.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "min_sample_size": {"type": "integer"},
                        "source_table": {"type": "string"},
                    },
                    "required": ["min_sample_size"],
                },
            },
        }
