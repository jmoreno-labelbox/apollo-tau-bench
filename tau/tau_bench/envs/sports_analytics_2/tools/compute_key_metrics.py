from tau_bench.envs.tool import Tool
import json
from typing import Any

class ComputeKeyMetrics(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], **kwargs) -> str:
        pass
        payload = {"metrics_table": "key_metrics"}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ComputeKeyMetrics",
                "description": "Computes key pitcher metrics.",
                "parameters": {
                    "type": "object",
                    "properties": {"source_table": {"type": "string"}},
                },
                "required": [],
            },
        }
