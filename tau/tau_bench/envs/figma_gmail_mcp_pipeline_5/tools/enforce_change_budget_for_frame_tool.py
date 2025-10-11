# © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _require_str(arg: Any, name: str) -> Optional[str]:
    """Return arg as str if valid, else None."""
    return arg if isinstance(arg, str) and arg.strip() else None

def _get_config_json(data: Dict[str, Any], key: str) -> Dict[str, Any]:
    """Read a config row from system_config and parse its JSON value."""
    rows = data.get("system_config", [])
    for r in rows:
        if r.get("config_key") == key:
            try:
                return json.loads(r.get("config_value_json") or "{}")
            except Exception:
                return {}
    return {}

class EnforceChangeBudgetForFrameTool(Tool):
    """Check if a frame exceeds fix-item change budget (from config) within a plan."""

    @staticmethod
    def invoke(data: Dict[str, Any], frame_id, plan_id) -> str:
        plan_id = _require_str(plan_id, "plan_id")
        frame_id = _require_str(frame_id, "frame_id")
        if not (plan_id and frame_id):
            return json.dumps({"error":"plan_id and frame_id required"})

        cfg = _get_config_json(data, "fix_workflow_config")
        budget = int(cfg.get("change_budget_per_frame", 5))

        items = data.get("fix_items", [])
        count = sum(1 for r in items if r.get("plan_id")==plan_id and r.get("frame_id")==frame_id)
        return json.dumps({"plan_id": plan_id, "frame_id": frame_id, "count": count, "budget": budget, "exceeds": count > budget}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"enforce_change_budget_for_frame",
            "description":"Return whether a frame's fix items exceed the per-frame budget.",
            "parameters":{"type":"object","properties":{
                "plan_id":{"type":"string"},
                "frame_id":{"type":"string"}
            },"required":["plan_id","frame_id"]}
        }}