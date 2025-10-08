from tau_bench.envs.tool import Tool
import csv
import json
import re
from datetime import datetime
from typing import Any

class ExceptionRaiser(Tool):
    """
    Generate consistent alerts based on supplied insights and rules.
    The caller specifies exactly what to assess; the tool produces structured alerts and counts.
    """

    @staticmethod
    def invoke(
        data: dict[str, Any], 
        plan_id: str = "", 
        insights: list[dict[str, Any]] = [], 
        rules: dict[str, Any] = {
            "zero_delivery_impressions": 0,
            "cap_hit_spend": None,
            "data_gap_days": None,
        },
        date: str = None,
        adset_id: str = None) -> str:
        alerts: list[dict[str, Any]] = []

        zdi = rules.get("zero_delivery_impressions", 0)
        for row in insights:
            imp = row.get("impressions")
            if imp is not None and imp <= zdi:
                alerts.append(
                    {
                        "type": "zero_delivery",
                        "adset_id": str(row.get("adset_id", "")),
                        "severity": "high",
                        "details": {"impressions": imp, "threshold": zdi},
                    }
                )

        cap = rules.get("cap_hit_spend")
        if cap is not None:
            for row in insights:
                spend = row.get("spend")
                if spend is not None and spend >= cap:
                    alerts.append(
                        {
                            "type": "cap_hit",
                            "adset_id": str(row.get("adset_id", "")),
                            "severity": "medium",
                            "details": {"spend": spend, "cap": cap},
                        }
                    )

        gap = rules.get("data_gap_days")
        if gap is not None:
            for row in insights:
                missing_days = row.get("missing_days")
                if missing_days is not None and missing_days >= gap:
                    alerts.append(
                        {
                            "type": "data_gap",
                            "adset_id": str(row.get("adset_id", "")),
                            "severity": "medium",
                            "details": {"missing_days": missing_days, "threshold": gap},
                        }
                    )
        payload = {
                "success": True,
                "plan_id": plan_id,
                "count": len(alerts),
                "alerts": alerts,
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
                "name": "ExceptionRaiser",
                "description": "Create deterministic alerts from insights and rule thresholds.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_id": {"type": "string"},
                        "insights": {"type": "array", "items": {"type": "object"}},
                        "rules": {"type": "object"},
                    },
                    "required": ["insights"],
                    "additionalProperties": False,
                },
            },
        }
