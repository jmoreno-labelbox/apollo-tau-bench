# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LogMealHistoryCreateByKeys(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        household_id: int,
        user_id: int,
        plan_date: str,
        recipe_id: int,
        reason: Optional[str] = None,
    ) -> str:
        hist = next(
            (
                h
                for h in data.get("meal_history", [])
                if int(h.get("household_id")) == int(household_id)
                and str(h.get("plan_date")) == str(plan_date)
                and int(h.get("recipe_id")) == int(recipe_id)
            ),
            None,
        )
        if not hist:
            # If not located, select the most recent history_id for the household/date as a fallback option (deterministic).
            cands = [
                h
                for h in data.get("meal_history", [])
                if int(h.get("household_id")) == int(household_id)
                and str(h.get("plan_date")) == str(plan_date)
            ]
            if not cands:
                return json.dumps({"error": "meal_history not found for keys"})
            hist = sorted(cands, key=lambda h: int(h.get("history_id", 0)), reverse=True)[0]
        tbl = _tbl(data, "audit_logs")
        next_id = _max_id(tbl, "audit_id", 12000) + 1
        payload = {"date": str(plan_date)}
        if reason:
            payload["reason"] = str(reason)
        row = {
            "audit_id": next_id,
            "household_id": int(household_id),
            "user_id": int(user_id),
            "entity_type": "meal_history",
            "entity_id": int(hist.get("history_id")),
            "action_enum": "create",
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
                "name": "log_meal_history_create_by_keys",
                "description": "Append audit log for meal_history creation by keys.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "user_id": {"type": "integer"},
                        "plan_date": {"type": "string"},
                        "recipe_id": {"type": "integer"},
                        "reason": {"type": "string"},
                    },
                    "required": ["household_id", "user_id", "plan_date", "recipe_id"],
                },
            },
        }
