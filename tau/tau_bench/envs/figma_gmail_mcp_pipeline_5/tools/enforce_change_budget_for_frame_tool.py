from tau_bench.envs.tool import Tool
import hashlib
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class EnforceChangeBudgetForFrameTool(Tool):
    """Verify if a frame surpasses the fix-item change budget (from config) within a plan."""

    @staticmethod
    def invoke(data: dict[str, Any], plan_id: str = None, frame_id: str = None) -> str:
        plan_id = _require_str(plan_id, "plan_id")
        frame_id = _require_str(frame_id, "frame_id")
        if not (plan_id and frame_id):
            payload = {"error": "plan_id and frame_id required"}
            out = json.dumps(payload)
            return out

        cfg = _get_config_json(data, "fix_workflow_config")
        budget = int(cfg.get("change_budget_per_frame", 5))

        items = data.get("fix_items", [])
        count = sum(
            1
            for r in items
            if r.get("plan_id") == plan_id and r.get("frame_id") == frame_id
        )
        payload = {
                "plan_id": plan_id,
                "frame_id": frame_id,
                "count": count,
                "budget": budget,
                "exceeds": count > budget,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "EnforceChangeBudgetForFrame",
                "description": "Return whether a frame's fix items exceed the per-frame budget.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_id": {"type": "string"},
                        "frame_id": {"type": "string"},
                    },
                    "required": ["plan_id", "frame_id"],
                },
            },
        }
