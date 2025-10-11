# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CalculateChangeROI(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], cr_id, benefit_timeframe_months = 12, expected_benefits = {}) -> str:

        if not cr_id:
            return json.dumps({"error": "cr_id is required"})

        change_requests = list(data.get("change_requests", {}).values())

        cr = next((c for c in change_requests if c.get("cr_id") == cr_id), None)
        if not cr:
            return json.dumps({"error": f"Change request '{cr_id}' not found"})

        impact = cr.get("impact_assessment", {})
        total_cost = impact.get("budget_impact", 0)

        for resource in impact.get("resource_requirements", []):
            hours = resource.get("hours_per_week", 0) * resource.get(
                "duration_weeks", 0
            )

            total_cost += hours * 150

        total_benefits = 0
        benefit_breakdown = {}

        for benefit_type, value in expected_benefits.items():
            if benefit_type == "cost_savings_monthly":
                total_value = value * benefit_timeframe_months
                total_benefits += total_value
                benefit_breakdown[benefit_type] = total_value
            elif benefit_type == "productivity_gain_percentage":

                monthly_cost = 10 * 150 * 160
                monthly_savings = monthly_cost * (value / 100)
                total_value = monthly_savings * benefit_timeframe_months
                total_benefits += total_value
                benefit_breakdown["productivity_savings"] = total_value
            elif benefit_type == "revenue_increase_monthly":
                total_value = value * benefit_timeframe_months
                total_benefits += total_value
                benefit_breakdown[benefit_type] = total_value
            else:

                total_benefits += value
                benefit_breakdown[benefit_type] = value

        roi_percentage = (
            ((total_benefits - total_cost) / total_cost * 100) if total_cost > 0 else 0
        )
        payback_period_months = (
            (total_cost / (total_benefits / benefit_timeframe_months))
            if total_benefits > 0
            else None
        )

        if roi_percentage > 50:
            recommendation = "Strongly recommended - High ROI"
        elif roi_percentage > 20:
            recommendation = "Recommended - Positive ROI"
        elif roi_percentage > 0:
            recommendation = "Consider with caution - Low ROI"
        else:
            recommendation = "Not recommended - Negative ROI"

        return json.dumps(
            {
                "cr_id": cr_id,
                "financial_analysis": {
                    "total_cost": total_cost,
                    "total_benefits": total_benefits,
                    "benefit_breakdown": benefit_breakdown,
                    "roi_percentage": round(roi_percentage, 1),
                    "payback_period_months": round(payback_period_months, 1)
                    if payback_period_months
                    else None,
                    "benefit_timeframe_months": benefit_timeframe_months,
                },
                "recommendation": recommendation,
                "assumptions": {
                    "hourly_rate": "$150/hour",
                    "working_hours_per_month": 160,
                },
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_change_roi",
                "description": "Calculate return on investment for a change request",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cr_id": {"type": "string", "description": "Change request ID"},
                        "expected_benefits": {
                            "type": "object",
                            "description": "Expected benefits mapping (e.g., cost_savings_monthly, productivity_gain_percentage, revenue_increase_monthly)",
                        },
                        "benefit_timeframe_months": {
                            "type": "number",
                            "description": "Timeframe for benefits calculation in months",
                        },
                    },
                    "required": ["cr_id"],
                },
            },
        }
