from tau_bench.envs.tool import Tool
import json
from typing import Any

class compute_fix_plan_summary(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], plan_id: str, timestamp: str, request_id: str
    ) -> str:
        items = data.get("fix_items", [])
        total = 0
        pending_ids: list[str] = []
        applied_ids: list[str] = []
        for it in items:
            if not isinstance(it, dict) or it.get("plan_id") != plan_id:
                continue
            total += 1
            status = (it.get("status") or "").upper()
            if status == "APPLIED":
                applied_ids.append(it.get("item_id"))
            else:
                pending_ids.append(it.get("item_id"))
        summary = {
            "plan_id": plan_id,
            "total_count": total,
            "pending_count": len(pending_ids),
            "pending_item_ids": pending_ids,
            "applied_item_ids": applied_ids,
            "day": (timestamp or "").split("T")[0],
            "request_id": request_id,
        }
        payload = summary
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ComputeFixPlanSummary",
                "description": "Summarize fix plan items, counting APPLIED vs pending and listing pending item IDs.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_id": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "request_id": {"type": "string"},
                    },
                    "required": ["plan_id", "timestamp", "request_id"],
                },
            },
        }
