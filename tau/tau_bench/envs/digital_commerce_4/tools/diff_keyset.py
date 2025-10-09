from tau_bench.envs.tool import Tool
import json
from typing import Any

class DiffKeyset(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        left: dict[str, Any],
        right: dict[str, Any],
        keys: list[str],
    ) -> str:
        changes = {}
        for k in keys:
            lv = left.get(k, None)
            rv = right.get(k, None)
            if lv != rv:
                changes[k] = {"before": lv, "after": rv}
        payload = {"keys": keys, "changes": changes}
        out = json.dumps(payload, indent=2)
        return out
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "diffKeyset",
                "description": "Diff two dicts across selected keys.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "left": {"type": "object"},
                        "right": {"type": "object"},
                        "keys": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["left", "right", "keys"],
                },
            },
        }
