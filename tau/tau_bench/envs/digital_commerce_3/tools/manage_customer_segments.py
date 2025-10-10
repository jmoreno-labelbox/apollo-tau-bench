# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import FIXED_NOW


class ManageCustomerSegments(Tool):
    """Create and manage customer segments based on behavior and demographics."""

    @staticmethod
    def invoke(data: Dict[str, Any], segment_name: Any, criteria: Any = None) -> str:
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

        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "manage_customer_segments",
                "description": "Create and manage customer segments based on behavior and demographics.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "segment_name": {"type": "string"},
                        "criteria": {"type": "object", "properties": {
                            "min_orders": {"type": "integer", "description": "Optional. Minimum number of orders in the specified period."},
                            "period_days": {"type": "integer", "description": "Optional. Number of days that just passed to consider for the order count."},
                            "lifetime_spend_usd": {"type": "integer", "description": "Optional. Minimum lifetime spend in USD."},
                        }},
                    },
                    "required": ["segment_name"],
                },
            },
        }
