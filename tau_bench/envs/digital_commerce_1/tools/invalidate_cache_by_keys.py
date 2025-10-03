from tau_bench.envs.tool import Tool
import json
from typing import Any

class InvalidateCacheByKeys(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], keys: list[str]) -> str:
        inv = _ensure_table(data, "cache_invalidations")
        ts = FIXED_NOW
        for k in keys:
            inv.append({"key": k, "invalidated_at": ts})
        return _json({"invalidated_count": len(keys)})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "InvalidateCacheByKeys",
                "description": "Invalidate specific cache entries by key.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "keys": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["keys"],
                },
            },
        }
