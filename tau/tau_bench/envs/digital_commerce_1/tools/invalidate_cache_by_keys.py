# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _ensure_table


class InvalidateCacheByKeys(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], keys: List[str]) -> str:
        inv = _ensure_table(data, "cache_invalidations")
        ts = FIXED_NOW
        for k in keys:
            inv.append({"key": k, "invalidated_at": ts})
        return _json({"invalidated_count": len(keys)})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "invalidate_cache_by_keys",
                "description": "Invalidate specific cache entries by key.",
                "parameters": {
                    "type": "object",
                    "properties": {"keys": {"type": "array", "items": {"type": "string"}}},
                    "required": ["keys"],
                },
            },
        }
