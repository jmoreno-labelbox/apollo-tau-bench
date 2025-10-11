# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RankRecipesForTargets(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        recipe_ids: List[int],
        needed_count: int,
        target_calories: int,
        target_protein: int,
    ) -> str:
        scored: List[Tuple[float, int, float]] = []
        for rid in recipe_ids or []:
            r = _recipe_by_id(data, int(rid))
            if not r:
                continue
            cal = int(r.get("calories_per_serving", 0))
            prot = int(r.get("protein_g_per_serving", 0))
            dev = abs(cal - target_calories) / max(1, target_calories) + 10.0 * abs(
                prot - target_protein
            ) / max(1, target_protein)
            scored.append((dev, int(rid), float(prot)))
        picked = [
            rid
            for _, rid, _ in sorted(scored, key=lambda x: (x[0], -x[2], x[1]))[: int(needed_count)]
        ]
        return json.dumps({"selected_recipe_ids": picked})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "rank_recipes_for_targets",
                "description": "Select up to N recipe_ids closest to nutrition targets.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recipe_ids": {"type": "array", "items": {"type": "integer"}},
                        "needed_count": {"type": "integer"},
                        "target_calories": {"type": "integer"},
                        "target_protein": {"type": "integer"},
                    },
                    "required": ["recipe_ids", "needed_count", "target_calories", "target_protein"],
                },
            },
        }
