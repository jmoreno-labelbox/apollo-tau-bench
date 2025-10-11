# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _json_dump
from . import _first_user_id
def _household_for_user(data: Dict[str, Any], user_id: Optional[int]) -> Optional[Dict[str, Any]]:
    if user_id is not None:
        h = next((h for h in data.get("households", []) if h.get("primary_user_id") == user_id), None)
        if h:
            return h
    households = data.get("households", [])
    if not households:
        return None
    return sorted(households, key=lambda h: int(h.get("household_id", 10**9)))[0]

def _max_id(records: List[Dict[str, Any]], key: str, default: int) -> int:
    if not records:
        return default
    return max(int(r.get(key, default)) for r in records)

def _latest_order_for_household(data: Dict[str, Any], household_id: Optional[int]) -> Optional[Dict[str, Any]]:
    if household_id is None:
        return None
    orders = [o for o in data.get("orders", []) if o.get("household_id") == household_id]
    if not orders:
        return None
    return sorted(orders, key=lambda o: int(o.get("order_id", 0)), reverse=True)[0]

def _latest_meal_plan_for_household(data: Dict[str, Any], household_id: Optional[int]) -> Optional[Dict[str, Any]]:
    if household_id is None:
        return None
    plans = [m for m in data.get("meal_plans", []) if m.get("household_id") == household_id]
    if not plans:
        return None
    return sorted(plans, key=lambda m: int(m.get("meal_plan_id", 0)), reverse=True)[0]

def _latest_list_for_household(data: Dict[str, Any], household_id: Optional[int]) -> Optional[Dict[str, Any]]:
    if household_id is None:
        return None
    lists_ = [l for l in data.get("grocery_lists", []) if l.get("household_id") == household_id]
    if not lists_:
        return None
    return sorted(lists_, key=lambda l: int(l.get("list_id", 0)), reverse=True)[0]

def _json_dump(obj: Any) -> str:
    return json.dumps(obj, indent=2, ensure_ascii=False)

def _first_user_id(data: Dict[str, Any]) -> Optional[int]:
    users = data.get("users", [])
    if not users:
        return None
    return int(sorted(users, key=lambda u: int(u.get("user_id", 10**9)))[0]["user_id"])

def _default_household_id(data: Dict[str, Any], user_id: Optional[int] = None) -> Optional[int]:
    hh = _household_for_user(data, user_id)
    return hh.get("household_id") if hh else None

class LogAuditEvent(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], entity_id, entity_type, household_id, user_id, action_enum = "create", payload_json = {}) -> str:
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