from tau_bench.envs.tool import Tool
import json
from typing import Any

class NormalizeSpatialData(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], **kwargs) -> str:
        pass
        payload = {"grid": "12x12_catcher_view"}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "NormalizeSpatialData",
                "description": "Normalizes spatial pitch/location data.",
                "parameters": {
                    "type": "object",
                    "properties": {"source_table": {"type": "string"}},
                },
                "required": [],
            },
        }
