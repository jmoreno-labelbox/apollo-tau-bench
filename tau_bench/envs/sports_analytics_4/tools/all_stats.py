from tau_bench.envs.tool import Tool
import json
from typing import Any

class AllStats(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], source_table: str = None) -> str:
        payload = {"metrics_table": "key_metrics"}
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
                "name": "getStats",
                "description": "Computes key pitcher metrics.",
                "parameters": {
                    "type": "object",
                    "properties": {"source_table": {"type": "string"}},
                },
                "required": [],
            },
        }
