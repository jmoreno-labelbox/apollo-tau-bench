# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _first_user_id


class LogAuditEvent(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        household_id = kwargs.get("household_id")
        user_id = kwargs.get("user_id")
        entity_type = kwargs.get("entity_type")
        entity_id = kwargs.get("entity_id")
        action_enum = kwargs.get("action_enum", "create")
        payload_json = kwargs.get("payload_json", {})
        if user_id is None:
            user_id = _first_user_id(data)
        if household_id is None:
            household_id = _default_household_id(data, user_id)
        if not entity_type or entity_id is None:
            mp = _latest_meal_plan_for_household(data, household_id)
            gl = _latest_list_for_household(data, household_id)
            od = _latest_order_for_household(data, household_id)
            candidates = []
            if mp: candidates.append(("meal_plans", int(mp["meal_plan_id"])))
            if gl: candidates.append(("grocery_lists", int(gl["list_id"])))
            if od: candidates.append(("orders", int(od["order_id"])))
            if candidates:
                entity_type, entity_id = sorted(candidates, key=lambda x: x[1], reverse=True)[0]
            else:
                entity_type, entity_id = "system", 0
        al = data.get("audit_logs", [])
        next_a = _max_id(al, "audit_id", 12000) + 1
        row = {
            "audit_id": next_a,
            "household_id": household_id,
            "user_id": user_id,
            "entity_type": str(entity_type),
            "entity_id": entity_id,
            "action_enum": str(action_enum),
            "payload_json": payload_json,
            "created_at": "2025-01-03T10:00:00Z"
        }
        al.append(row)
        return _json_dump({"audit_id": next_a})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{"name":"log_audit_event","description":"Insert an audit row; infers household, user, entity_type/id, and defaults action to 'create'.","parameters":{"type":"object","properties":{"household_id":{"type":"integer"},"user_id":{"type":"integer"},"entity_type":{"type":"string"},"entity_id":{"type":"integer"},"action_enum":{"type":"string"},"payload_json":{"type":"object"}},"required":[]}}}
