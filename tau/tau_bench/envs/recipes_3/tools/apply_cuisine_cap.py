# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ApplyCuisineCap(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], recipe_ids: List[int], max_per_cuisine: int) -> str:
        counts: Dict[str, int] = {}
        selected: List[int] = []
        for rid in recipe_ids or []:
            r = _recipe_by_id(data, int(rid))
            if not r:
                continue
            cz = str(r.get("cuisine"))
            c = counts.get(cz, 0)
            if c < int(max_per_cuisine):
                selected.append(int(rid))
                counts[cz] = c + 1
        # Read-only behavior: return selection without mutating database
        return _json({"cuisine_limited_ids": selected})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "apply_cuisine_cap",
                "description": "Limit recipes to at most N per cuisine.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipe_ids": {"type": "array", "items": {"type": "integer"}},
                        "max_per_cuisine": {"type": "integer"},
                    },
                    "required": ["recipe_ids", "max_per_cuisine"],
                },
            },
        }
