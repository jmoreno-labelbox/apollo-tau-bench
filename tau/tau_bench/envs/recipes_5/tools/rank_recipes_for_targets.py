# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _json_dump


class RankRecipesForTargets(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], member_id, target_calories, target_protein, needed_count = 7) -> str:
        ids = _ids_from_kwargs_or_defaults(data, kwargs)
        needed_count = int(needed_count)
        tc = target_calories
        tp = target_protein
        if tc is None or tp is None:
            tc2, tp2 = _pick_target_from_member(data, member_id)
            target_calories = int(tc if tc is not None else tc2)
            target_protein = int(tp if tp is not None else tp2)
        else:
            target_calories = int(tc)
            target_protein = int(tp)
        scored: List[Tuple[float, int]] = []
        for rid in ids:
            r = _recipe_by_id(data, rid)
            if not r:
                continue
            dc = abs(int(r.get("calories_per_serving", 0)) - target_calories)
            dp = abs(int(r.get("protein_g_per_serving", 0)) - target_protein)
            score = float(dc) + float(dp) * 10.0
            scored.append((score, rid))
        picked = [rid for _, rid in sorted(scored, key=lambda x: (x[0], x[1]))[:needed_count]]
        return _json_dump({"selected_recipe_ids_json": json.dumps(picked)})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"rank_recipes_for_targets","description":"Select up to N recipes closest to nutrition targets; targets default from a household member.","parameters":{"type":"object","properties":{"recipe_ids_json":{"type":"string"},"filter_token":{"type":"string"},"meal_type":{"type":"string"},"min_protein_g":{"type":"integer"},"peanut_free":{"type":"boolean"},"needed_count":{"type":"integer"},"target_calories":{"type":"integer"},"target_protein":{"type":"integer"},"member_id":{"type":"integer"}},"required":[]}}}
