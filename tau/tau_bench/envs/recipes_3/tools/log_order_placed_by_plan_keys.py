# Sierra copyright.

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

class LogOrderPlacedByPlanKeys(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], household_id: int, user_id: int, week_start_date: str, store_id: int
    ) -> str:
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
        gl = next(
            (
                lt
                for lt in data.get("grocery_lists", [])
                if int(lt.get("source_meal_plan_id")) == int(plan.get("meal_plan_id"))
            ),
            None,
        )
        if not gl:
            return json.dumps({"error": "grocery_list not found for keys"})
        orders = [
            o
            for o in list(data.get("orders", {}).values())
            if int(o.get("household_id")) == int(household_id)
            and int(o.get("store_id")) == int(store_id)
            and int(o.get("list_id")) == int(gl.get("list_id"))
        ]
        if not orders:
            return json.dumps({"error": "order not found for keys"})
        order = sorted(orders, key=lambda o: int(o.get("order_id", 0)), reverse=True)[0]
        tbl = _tbl(data, "audit_logs")
        next_id = _max_id(tbl, "audit_id", 12000) + 1
        row = {
            "audit_id": next_id,
            "household_id": int(household_id),
            "user_id": int(user_id),
            "entity_type": "orders",
            "entity_id": int(order.get("order_id")),
            "action_enum": "place_order",
            "payloadjson": {"store_id": int(store_id), "list_id": int(gl.get("list_id"))},
            "created_at": "2025-01-03T10:00:00",
        }
        tbl.append(row)
        return json.dumps({"audit_id": next_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "log_order_placed_by_plan_keys",
                "description": "Audit order placement by (household_id, week_start_date, store_id).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "user_id": {"type": "integer"},
                        "week_start_date": {"type": "string"},
                        "store_id": {"type": "integer"},
                    },
                    "required": ["household_id", "user_id", "week_start_date", "store_id"],
                },
            },
        }