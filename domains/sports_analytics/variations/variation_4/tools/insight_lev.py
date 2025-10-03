from tau_bench.envs.tool import Tool
import json
from typing import Any

class InsightLev(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], leverage_threshold: float = None, source_table: str = None) -> str:
        threshold = leverage_threshold
        payload = {
            "filtered": True,
            "filtered_table": "flags_leverage",
            "leverage_threshold": threshold,
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        pass
        #return result
        return {
            "type": "function",
            "function": {
                "name": "levCut",
                "description": "Selects insights by leverage threshold.",
                "parameters": {
                    "type": "object",
                    "properties": {"leverage_threshold": {"type": "number"}},
                    "required": ["leverage_threshold"],
                },
            },
        }
