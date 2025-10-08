from tau_bench.envs.tool import Tool
import json
from typing import Any

class ManageCustomerSegments(Tool):
    """Establish and oversee customer segments according to behavior and demographics."""

    @staticmethod
    def invoke(data: dict[str, Any], segment_name: Any, criteria: Any = None) -> str:
        segment_name = f"{segment_name}".strip()
        if criteria is None:
            criteria = {}
        if not isinstance(criteria, dict):
            return _error("criteria must be an object.")
        if not segment_name:
            return _error("segment_name is required.")
        crit = dict(criteria)
        try:
            if "days" in crit and "period_days" not in crit:
                crit["period_days"] = int(crit.pop("days"))
        except Exception:
            crit["period_days"] = crit.pop("days")
        if "min_order" in crit and "min_orders" not in crit:
            crit["min_orders"] = crit.pop("min_order")
        for k in ("min_orders", "period_days", "lifetime_spend_usd"):
            if k in crit:
                try:
                    crit[k] = int(crit[k])
                except Exception:
                    pass
        segments = data.setdefault("customer_segments", [])
        segment_id = f"SEG_{len(segments) + 1:03d}"

        segment = {
            "segment_id": segment_id,
            "segment_name": segment_name,
            "criteria": crit,
            "customer_count": 10,
            "created_at": FIXED_NOW,
            "status": "active",
        }
        segments.append(segment)
        result = {
            "segment_id": segment_id,
            "segment_name": segment_name,
            "criteria": crit,
            "customer_count": 10,
        }

        _append_audit(
            data, "segment_created", segment_id, {"segment_name": segment_name}
        )
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ManageCustomerSegments",
                "description": "Create and manage customer segments based on behavior and demographics.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "segment_name": {"type": "string"},
                        "criteria": {"type": "object"},
                    },
                    "required": ["segment_name"],
                },
            },
        }
