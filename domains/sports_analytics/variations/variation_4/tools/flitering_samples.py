from tau_bench.envs.tool import Tool
import json
from typing import Any

class FliteringSamples(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], min_sample_size: int = 25, source_table: str = "", game_pk: Any = None) -> str:
        payload = {"filtered_insights": "flags_filtered_sample"}
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
                "name": "sizes",
                "description": "Selects insights by minimum sample size.",
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
