# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class compute_fix_plan_summary(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], plan_id: str, timestamp: str, request_id: str) -> str:
        items = data.get("fix_items", [])
        total = 0
        pending_ids: List[str] = []
        applied_ids: List[str] = []
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
        return json.dumps(summary, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"compute_fix_plan_summary",
            "description":"Summarize fix plan items, counting APPLIED vs pending and listing pending item IDs.",
            "parameters":{"type":"object","properties":{
                "plan_id":{"type":"string"},
                "timestamp":{"type":"string"},
                "request_id":{"type":"string"},
            },"required":["plan_id","timestamp","request_id"]}
        }}
