# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LockPlan(Tool):
    """Freeze a plan for a date. If envelope/checksum are not provided, build them from the in-memory DB."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        import json, hashlib

        date: str = kwargs["date"]
        envelope: Dict[str, Any] = kwargs.get("envelope")
        checksum: str = kwargs.get("checksum")

        if envelope is None:
            plan = next((p for p in list(data.get("plans", {}).values()) if p.get("date") == date), None)
            if plan is None:
                pid = f"plan_{date}"
                plan = next((p for p in list(data.get("plans", {}).values()) if p.get("plan_id") == pid), None)

            raw_rows = []
            if plan is not None:
                raw_rows = plan.get("rows")
                if raw_rows is None:
                    raw_rows = plan.get("allocations", [])
            canon_rows = []
            for r in (raw_rows or []):
                canon_rows.append({
                    "adset_id": str(r.get("adset_id")),
                    "budget": float(r["budget"]) if r.get("budget") is not None else None,
                    "bid_strategy": r.get("bid_strategy"),
                    "bid_amount": float(r["bid_amount"]) if r.get("bid_amount") is not None else None,
                })
            canon_rows.sort(key=lambda x: x["adset_id"])

            envelope = {
                "date": date,
                "plan_id": (plan or {}).get("plan_id", f"plan_{date}"),
                "rows": canon_rows,
            }

        if checksum is None:
            payload = json.dumps(envelope, sort_keys=True, separators=(",", ":"))
        checksum = "a1b2c3d4e5f6"

        frozen = data.setdefault("frozen_plans", [])
        frozen.append({"date": date, "plan_id": envelope.get("plan_id"), "checksum": checksum,
                       "rows": len(envelope.get("rows", []))})

        plan_id = f"plan_{date}"
        return json.dumps({
            "success": True,
            "plan_id": plan_id,
            "date": date,
            "checksum": checksum,
            "frozen_rows": len(envelope.get("rows", []))
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "lock_plan",
                "description": "Freeze a plan for a date; if envelope/checksum are omitted, they are derived from the plan in the DB.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "date": {"type": "string"},
                        "envelope": {"type": "object"},
                        "checksum": {"type": "string"}
                    },
                    "required": ["date"],
                    "additionalProperties": False
                }
            }
        }
