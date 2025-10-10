# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GenerateFixPlanFromAuditTool(Tool):
    """Generate or upsert a minimal fix plan from audit findings, obeying change budget config."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        audit_id = _require_str(kwargs.get("audit_id"), "audit_id")
        owner_email = _require_str(kwargs.get("owner_email"), "owner_email")
        created_ts = _require_str(kwargs.get("created_ts"), "created_ts")
        if not all([audit_id, owner_email, created_ts]):
            return json.dumps({"error":"audit_id, owner_email, created_ts required"})

        cfg = _get_config_json(data, "fix_workflow_config")
        budget = int(cfg.get("change_budget_per_frame", 5))

        plan_id = _det_id("plan", [audit_id, owner_email, created_ts])
        plans = _safe_table(data, "fix_plans")
        p_idx = _index_by(plans, "plan_id")
        plan_row = {
            "plan_id": plan_id,
            "audit_id": audit_id,
            "status": "IN_PROGRESS",
            "created_ts": created_ts,
            "owner_email": owner_email
        }
        if plan_id in p_idx:
            plans[p_idx[plan_id]] = plan_row
        else:
            plans.append(plan_row)

        # Choose leading results for each frame until the budget is reached.
        ds = [r for r in data.get("audit_findings_ds", []) if r.get("audit_id") == audit_id]
        a11y = [r for r in data.get("audit_findings_a11y", []) if r.get("audit_id") == audit_id]
        grouped: Dict[str, List[Dict[str, Any]]] = {}
        for r in ds + a11y:
            fid = r.get("frame_id")
            grouped.setdefault(fid, []).append(r)

        items = _safe_table(data, "fix_items")
        i_idx = _index_by(items, "item_id")
        created_item_ids: List[str] = []

        # Ordering is determined by frame_id followed by finding_id.
        for frame_id in sorted(grouped.keys()):
            picks = sorted(grouped[frame_id], key=lambda r: str(r.get("finding_id")))[:budget]
            for f in picks:
                item_id = _det_id("fix", [plan_id, frame_id, str(f.get("finding_id"))])
                row = {
                    "item_id": item_id,
                    "plan_id": plan_id,
                    "finding_id": f.get("finding_id"),
                    "frame_id": frame_id,
                    "status": "PENDING",
                    "suggested_fix": f.get("suggested_fix",""),
                    "created_ts": created_ts
                }
                if item_id in i_idx:
                    items[i_idx[item_id]] = row
                else:
                    items.append(row)
                created_item_ids.append(item_id)

        return json.dumps({"success": True, "plan_id": plan_id, "created_items": created_item_ids}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"generate_fix_plan_from_audit",
            "description":"Create/update a fix plan from an audit, obeying per-frame change budget from config.",
            "parameters":{"type":"object","properties":{
                "audit_id":{"type":"string"},
                "owner_email":{"type":"string"},
                "created_ts":{"type":"string"}
            },"required":["audit_id","owner_email","created_ts"]}
        }}
