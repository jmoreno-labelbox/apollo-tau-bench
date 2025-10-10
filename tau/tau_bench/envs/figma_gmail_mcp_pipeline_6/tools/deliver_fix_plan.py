# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class deliver_fix_plan(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], plan_id: str, delivery_method: str, timestamp: str, request_id: str) -> str:
        deliveries = data.setdefault("fix_plan_deliveries", [])
        fix_items = data.get("fix_items", [])
        comments_tbl = data.setdefault("figma_comments", [])
        bot_email = _resolve_bot_email(data)
        run_id = _id_from_request("run", request_id) or _get_next_id(
            "run", [r.get("run_id", "") for r in deliveries if isinstance(r, dict)]
        )
        existing = next((r for r in deliveries if isinstance(r, dict) and r.get("run_id") == run_id), None)
        if existing:
            return json.dumps(existing, indent=2)

        items_for_plan: List[Dict[str, Any]] = []
        for it in fix_items:
            if isinstance(it, dict) and it.get("plan_id") == plan_id:
                items_for_plan.append(it)

        created_comment_ids: List[str] = []
        if (delivery_method or "").upper() == "COMMENTS":
            mirrored = {
                c.get("mirrored_item_id")
                for c in comments_tbl
                if isinstance(c, dict) and c.get("mirrored_item_id")
            }
            existing_ids = [c.get("comment_id", "") for c in comments_tbl if isinstance(c, dict)]

            for it in items_for_plan:
                item_id = it.get("item_id")
                status = (it.get("status") or "").upper()
                if not item_id or item_id in mirrored:
                    continue
                if status != "APPLIED":
                    new_cid = _get_next_id("comment", existing_ids)
                    art_id = it.get("artifact_id") or it.get("artifact_id_nullable")
                    title_val = it.get("title")
                    title = title_val if isinstance(title_val, str) and title_val.strip() else "Pending item"

                    comments_tbl.append({
                        "comment_id": new_cid,
                        "artifact_id": art_id,
                        "author_email": bot_email,
                        "content_html": f"[FixPlan] {item_id}: {title} — Status: {status or 'PENDING'}",
                        "mirrored_item_id": item_id,
                        "day": _ymd(timestamp),
                    })
                    existing_ids.append(new_cid)
                    created_comment_ids.append(new_cid)

        row = {
            "run_id": run_id,
            "plan_id": plan_id,
            "delivery_method": delivery_method,
            "mirrored_count": len(created_comment_ids),
            "comment_ids": created_comment_ids,
            "day": _ymd(timestamp),
        }
        deliveries.append(row)
        return json.dumps(row, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "deliver_fix_plan",
                "description": "Deliver a fix plan via a method (e.g., COMMENTS). For COMMENTS, mirror non-APPLIED items as Figma comments idempotently.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_id": {"type": "string"},
                        "delivery_method": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "request_id": {"type": "string"},
                    },
                    "required": ["plan_id", "delivery_method", "timestamp", "request_id"],
                },
            },
        }
