from tau_bench.envs.tool import Tool
import json
from typing import Any

class CaptureLocContext(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], keys: list[str]) -> str:
        context = {k: f"artifact://context/{k}" for k in keys}
        payload = {"context_uris": context}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaptureLocContext",
                "description": "Returns deterministic context media URIs per string key.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "keys": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["keys"],
                },
            },
        }
