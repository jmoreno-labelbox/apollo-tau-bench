from tau_bench.envs.tool import Tool
import json
from typing import Any

class WriteLocaleBundle(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], locale: str, keys: list[str]) -> str:
        localization_workflow = _get_table(data, "localization_workflow")
        bundle_name = f"bundle-{locale}-{len(keys)}"
        entry = {"bundle": bundle_name, "locale": locale, "keys": keys}
        localization_workflow.append(entry)
        payload = {"bundle_uri": f"artifact://bundle/{bundle_name}"}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "WriteLocaleBundle",
                "description": "Writes a deterministic locale bundle record and returns a bundle URI.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "locale": {"type": "string"},
                        "keys": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["locale", "keys"],
                },
            },
        }
