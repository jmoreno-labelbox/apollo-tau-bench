# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ExceptionRaiser(Tool):
    """
    Produce deterministic alerts based on provided insights + rules.
    Caller passes exactly what to evaluate; tool emits structured alerts and counts.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], insights = [], plan_id = "", rules = {
        "zero_delivery_impressions": 0,
        "cap_hit_spend": None,
        "data_gap_days": None
    }) -> str:
        plan_id: str = plan_id
        insights: List[Dict[str, Any]] = insights
        rules: Dict[str, Any] = rules

        alerts: List[Dict[str, Any]] = []

        zdi = rules.get("zero_delivery_impressions", 0)
        for row in insights:
            imp = row.get("impressions")
            if imp is not None and imp <= zdi:
                alerts.append({
                    "type": "zero_delivery",
                    "adset_id": str(row.get("adset_id", "")),
                    "severity": "high",
                    "details": {"impressions": imp, "threshold": zdi}
                })

        cap = rules.get("cap_hit_spend")
        if cap is not None:
            for row in insights:
                spend = row.get("spend")
                if spend is not None and spend >= cap:
                    alerts.append({
                        "type": "cap_hit",
                        "adset_id": str(row.get("adset_id", "")),
                        "severity": "medium",
                        "details": {"spend": spend, "cap": cap}
                    })

        gap = rules.get("data_gap_days")
        if gap is not None:
            for row in insights:
                missing_days = row.get("missing_days")
                if missing_days is not None and missing_days >= gap:
                    alerts.append({
                        "type": "data_gap",
                        "adset_id": str(row.get("adset_id", "")),
                        "severity": "medium",
                        "details": {"missing_days": missing_days, "threshold": gap}
                    })

        return json.dumps({"success": True, "plan_id": plan_id, "count": len(alerts), "alerts": alerts}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "exception_raiser",
                "description": "Create deterministic alerts from insights and rule thresholds.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_id": {"type": "string"},
                        "insights": {"type": "array", "items": {"type": "object"}},
                        "rules": {"type": "object"}
                    },
                    "required": ["insights"],
                    "additionalProperties": False
                }
            }
        }
