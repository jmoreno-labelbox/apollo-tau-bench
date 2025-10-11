# Sierra Copyright

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

class LogMealPlanCreateByKeys(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], household_id: int, user_id: int, week_start_date: str) -> str:
        plan = next(
            (
                p
                for p in data.get("meal_plans", [])
                if int(p.get("household_id")) == int(household_id)
                and str(p.get("week_start_date")) == str(week_start_date)
            ),
            None,
        )
        if not plan:
            return json.dumps({"error": "meal_plan not found for keys"})
        tbl = _tbl(data, "audit_logs")
        next_id = _max_id(tbl, "audit_id", 12000) + 1
        row = {
            "audit_id": next_id,
            "household_id": int(household_id),
            "user_id": int(user_id),
            "entity_type": "meal_plans",
            "entity_id": int(plan.get("meal_plan_id")),
            "action_enum": "create",
            "payloadjson": {"week_start_date": str(week_start_date)},
            "created_at": "2025-01-03T10:00:00",
        }
        tbl.append(row)
        return json.dumps({"audit_id": next_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "log_meal_plan_create_by_keys",
                "description": "Audit meal plan creation by (household_id, week_start_date).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "user_id": {"type": "integer"},
                        "week_start_date": {"type": "string"},
                    },
                    "required": ["household_id", "user_id", "week_start_date"],
                },
            },
        }