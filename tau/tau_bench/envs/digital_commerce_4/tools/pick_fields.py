from tau_bench.envs.tool import Tool
import json
from typing import Any

class PickFields(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], payload: dict[str, Any], fields: list[str]) -> str:
        picked = {k: payload.get(k, None) for k in sorted(fields)}
        payload = picked
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "pickFields",
                "description": "Return only the selected keys from a dict.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "payload": {"type": "object"},
                        "fields": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["payload", "fields"],
                },
            },
        }
