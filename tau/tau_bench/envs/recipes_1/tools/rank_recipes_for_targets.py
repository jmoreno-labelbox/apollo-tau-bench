# Sierra copyright.

from typing import Tuple
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _json_dump








def _recipe_by_id(data: Dict[str, Any], recipe_id: int) -> Optional[Dict[str, Any]]:
    return next((r for r in data.get("recipes", []) if int(r.get("recipe_id")) == recipe_id), None)

def _parse_json_list_ids(json_str: str) -> List[int]:
    try:
        arr = json.loads(json_str)
        if isinstance(arr, list):
            return [int(x) for x in arr]
    except Exception:
        pass
    return []

def _json_dump(obj: Any) -> str:
    return json.dumps(obj, indent=2, ensure_ascii=False)

class RankRecipesForTargets(Tool):
    """Score recipes by closeness to (target_calories, target_protein); lower score is better."""
    @staticmethod
    def invoke(data: Dict[str, Any], needed_count = 7, recipe_ids_json = "[]", target_calories = 2000, target_protein = 100) -> str:
        target_calories = int(target_calories)
        target_protein = int(target_protein)
        needed_count = int(needed_count)
        ids = _parse_json_list_ids(recipe_ids_json)
        scored: List[Tuple[float, int, float]] = []
        for rid in ids:
            r = _recipe_by_id(data, rid)
            if not r:
                continue
            cal = int(r.get("calories_per_serving", 0))
            prot = int(r.get("protein_g_per_serving", 0))
            dev = abs(cal - target_calories) / max(1, target_calories) + 10.0 * abs(prot - target_protein) / max(1, target_protein)
            scored.append((dev, rid, float(prot)))
        picked = [rid for _, rid, _ in sorted(scored, key=lambda x: (x[0], -x[2], x[1]))[:needed_count]]
        return _json_dump({"selected_recipe_ids_json": json.dumps(picked)})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"rank_recipes_for_targets",
            "description":"Select up to N recipes closest to nutrition targets.",
            "parameters":{"type":"object","properties":{
                "recipe_ids_json":{"type":"string"},
                "needed_count":{"type":"integer"},
                "target_calories":{"type":"integer"},
                "target_protein":{"type":"integer"}
            },"required":["recipe_ids_json","needed_count","target_calories","target_protein"]}
        }}