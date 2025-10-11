# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _tbl(db: Dict[str, Any], name: str) -> List[Dict[str, Any]]:
    return db.setdefault(name, [])

def _max_id(rows: List[Dict[str, Any]], id_field: str, base: int) -> int:
    if not rows:
        return base
    vals: List[int] = []
    for r in rows:
        try:
            vals.append(int(r.get(id_field)))
        except Exception:
            pass
    return max(vals) if vals else base

class LogValidateSubstitutionsByPlanKeys(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        household_id: int,
        user_id: int,
        week_start_date: str,
        recipe_id: Optional[int] = None,
    ) -> str:
        # set entity_type to 'meal_history' where entity_id equals 0 according to policy note
        tbl = _tbl(data, "audit_logs")
        next_id = _max_id(tbl, "audit_id", 12000) + 1
        payload = {}
        if recipe_id is not None:
            payload["recipe_id"] = int(recipe_id)
        row = {
            "audit_id": next_id,
            "household_id": int(household_id),
            "user_id": int(user_id),
            "entity_type": "meal_history",
            "entity_id": 0,
            "action_enum": "validate_substitutions",
            "payloadjson": payload,
            "created_at": "2025-01-03T10:00:00",
        }
        tbl.append(row)
        return json.dumps({"audit_id": next_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "log_validate_substitutions_by_plan_keys",
                "description": "Audit substitutions validation for plan by keys (entity_type meal_history, id 0).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "user_id": {"type": "integer"},
                        "week_start_date": {"type": "string"},
                        "recipe_id": {"type": "integer"},
                    },
                    "required": ["household_id", "user_id", "week_start_date"],
                },
            },
        }