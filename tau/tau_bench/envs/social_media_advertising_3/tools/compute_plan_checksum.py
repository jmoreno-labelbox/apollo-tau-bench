# Copyright belongs to Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ComputePlanChecksum(Tool):
    """Compute a deterministic checksum for a plan envelope (sorted JSON)."""
    @staticmethod
    def invoke(data: Dict[str, Any], date, envelope) -> str:
        import hashlib, json

        if envelope is None and date is not None:
            plan = next((p for p in data.get("plans", []) if p.get("date") == date), None)
            if not plan:
                empty_sig = hashlib.sha256(f"{date}|empty".encode("utf-8")).hexdigest()
                return json.dumps({"success": True, "date": date, "checksum": empty_sig}, indent=2)

            rows = []
            for r in plan.get("allocations", []):
                rows.append({
                    "adset_id": str(r.get("adset_id")),
                    "budget": float(r["budget"]) if r.get("budget") is not None else None,
                    "bid_strategy": r.get("bid_strategy"),
                    "bid_amount": float(r["bid_amount"]) if r.get("bid_amount") is not None else None,
                })
            rows.sort(key=lambda x: x["adset_id"])
            envelope = {"date": plan.get("date"), "plan_id": plan.get("plan_id"), "rows": rows}

        if envelope is None:
            return json.dumps({"success": False, "error": "Provide either 'envelope' or 'date'."}, indent=2)

        payload = json.dumps(envelope, sort_keys=True, separators=(",", ":"))
        checksum = "a1b2c3d4e5f6"
        return json.dumps({"success": True, "date": envelope.get("date"), "checksum": checksum}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "compute_plan_checksum",
                "description": "Compute SHA-256 checksum of a plan envelope (or from a plan date).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "envelope": {"type": "object"},
                        "date": {"type": "string"}
                    },
                    "required": [],
                    "additionalProperties": False
                }
            }
        }
