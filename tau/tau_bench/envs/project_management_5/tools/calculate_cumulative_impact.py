# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CalculateCumulativeImpact(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], from_date, project_id, include_pending = False) -> str:

        if not project_id:
            return json.dumps({"error": "project_id is required"})

        change_requests = list(data.get("change_requests", {}).values())

        project_crs = [
            cr for cr in change_requests if cr.get("project_id") == project_id
        ]

        if from_date:
            project_crs = [
                cr for cr in project_crs if cr.get("created_date", "") >= from_date
            ]

        if include_pending:
            relevant_crs = [
                cr
                for cr in project_crs
                if cr.get("status") in ["approved", "pending_approval", "in_review"]
            ]
        else:
            relevant_crs = [cr for cr in project_crs if cr.get("status") == "approved"]

        total_budget_impact = 0
        total_timeline_impact = 0
        scope_additions = 0
        scope_reductions = 0
        requirement_changes = 0
        resource_additions = []

        for cr in relevant_crs:
            if impact := cr.get("impact_assessment"):
                total_budget_impact += impact.get("budget_impact", 0)
                total_timeline_impact += impact.get("timeline_impact_weeks", 0)
                resource_additions.extend(impact.get("resource_requirements", []))

            change_type = cr.get("change_type")
            if change_type == "scope_addition":
                scope_additions += 1
            elif change_type == "scope_reduction":
                scope_reductions += 1
            elif change_type == "requirement_change":
                requirement_changes += 1

        resource_summary = {}
        for req in resource_additions:
            emp_id = req.get("employee_id")
            if emp_id in resource_summary:
                resource_summary[emp_id] += req.get("hours_per_week", 0)
            else:
                resource_summary[emp_id] = req.get("hours_per_week", 0)

        risk_factors = []
        if total_budget_impact > 100000:
            risk_factors.append("High budget impact")
        if total_timeline_impact > 12:
            risk_factors.append("Significant schedule impact")
        if len(relevant_crs) > 10:
            risk_factors.append("High change volume")
        if len(resource_summary) > 5:
            risk_factors.append("Multiple resource impacts")

        overall_risk = (
            "critical"
            if len(risk_factors) >= 3
            else "high"
            if len(risk_factors) >= 2
            else "medium"
            if risk_factors
            else "low"
        )

        return json.dumps(
            {
                "project_id": project_id,
                "analysis_period": {
                    "from_date": from_date or "project_start",
                    "to_date": datetime.now().isoformat(),
                    "include_pending": include_pending,
                },
                "change_summary": {
                    "total_changes": len(relevant_crs),
                    "approved": len(
                        [cr for cr in relevant_crs if cr.get("status") == "approved"]
                    ),
                    "pending": len(
                        [cr for cr in relevant_crs if cr.get("status") != "approved"]
                    ),
                    "by_type": {
                        "scope_additions": scope_additions,
                        "scope_reductions": scope_reductions,
                        "requirement_changes": requirement_changes,
                    },
                },
                "cumulative_impact": {
                    "total_budget_impact": total_budget_impact,
                    "timeline_impact_weeks": total_timeline_impact,
                    "resources_needed": len(resource_summary),
                    "total_resource_hours": sum(resource_summary.values()),
                },
                "risk_assessment": {
                    "overall_risk": overall_risk,
                    "risk_factors": risk_factors,
                },
                "recommendations": [
                    "Consider project rebaseline" if len(relevant_crs) > 10 else None,
                    "Review resource capacity" if len(resource_summary) > 3 else None,
                    "Update stakeholder expectations"
                    if total_timeline_impact > 8
                    else None,
                ],
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_cumulative_impact",
                "description": "Calculate cumulative impact of all changes on a project",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "Project ID"},
                        "include_pending": {
                            "type": "boolean",
                            "description": "Include pending changes in calculation",
                        },
                        "from_date": {
                            "type": "string",
                            "description": "Start date for analysis (ISO format)",
                        },
                    },
                    "required": ["project_id"],
                },
            },
        }
