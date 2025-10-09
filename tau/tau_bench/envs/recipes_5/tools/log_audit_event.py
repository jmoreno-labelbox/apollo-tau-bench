from tau_bench.envs.tool import Tool
import json
from datetime import date, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class LogAuditEvent(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        household_id: int = None,
        user_id: int = None,
        entity_type: str = None,
        entity_id: int = None,
        action_enum: str = "create",
        payload_json: dict = {}
,
    created_at: Any = None,
    ) -> str:
        if user_id is None:
            user_id = _first_user_id(data)
        if household_id is None:
            household_id = _default_household_id(data, user_id)
        if not entity_type or entity_id is None:
            mp = _latest_meal_plan_for_household(data, household_id)
            gl = _latest_list_for_household(data, household_id)
            od = _latest_order_for_household(data, household_id)
            candidates = []
            if mp:
                candidates.append(("meal_plans", int(mp["meal_plan_id"])))
            if gl:
                candidates.append(("grocery_lists", int(gl["list_id"])))
            if od:
                candidates.append(("orders", int(od["order_id"])))
            if candidates:
                entity_type, entity_id = sorted(
                    candidates, key=lambda x: x[1], reverse=True
                )[0]
            else:
                entity_type, entity_id = "system", 0
        al = data.get("audit_logs", {}).values()
        next_a = _max_id(al, "audit_id", 12000) + 1
        row = {
            "audit_id": next_a,
            "household_id": household_id,
            "user_id": user_id,
            "entity_type": str(entity_type),
            "entity_id": entity_id,
            "action_enum": str(action_enum),
            "payload_json": payload_json,
            "created_at": "2025-01-03T10:00:00Z",
        }
        data["audit_logs"][row["audit_log_id"]] = row
        return _json_dump({"audit_id": next_a})
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LogAuditEvent",
                "description": "Insert an audit row; infers household, user, entity_type/id, and defaults action to 'create'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "household_id": {"type": "integer"},
                        "user_id": {"type": "integer"},
                        "entity_type": {"type": "string"},
                        "entity_id": {"type": "integer"},
                        "action_enum": {"type": "string"},
                        "payload_json": {"type": "object"},
                    },
                    "required": [],
                },
            },
        }
