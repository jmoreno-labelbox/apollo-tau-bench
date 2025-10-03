from tau_bench.envs.tool import Tool
import json
from typing import Any

class RedactFields(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], payload: dict[str, Any], fields: list[str]) -> str:
        redacted = {k: v for k, v in payload.items() if k not in fields}
        payload = redacted
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "redactFields",
                "description": "Remove specified keys from a dict.",
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
