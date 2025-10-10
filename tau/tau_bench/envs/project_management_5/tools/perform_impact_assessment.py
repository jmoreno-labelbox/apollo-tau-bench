# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class PerformImpactAssessment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cr_id = kwargs.get("cr_id")
        assessed_by = kwargs.get("assessed_by")
        timeline_impact_weeks = kwargs.get("timeline_impact_weeks", 0)
        budget_impact = kwargs.get("budget_impact", 0)
        resource_requirements = kwargs.get("resource_requirements", [])
        technical_dependencies = kwargs.get("technical_dependencies", [])

        if not all([cr_id, assessed_by]):
            return json.dumps({"error": "cr_id and assessed_by are required"})

        change_requests = list(data.get("change_requests", {}).values())
        budgets = list(data.get("budgets", {}).values())

        cr = next((c for c in change_requests if c.get("cr_id") == cr_id), None)
        if not cr:
            return json.dumps({"error": f"Change request '{cr_id}' not found"})

        project_budget = next(
            (b for b in budgets if b.get("project_id") == cr.get("project_id")), None
        )
        budget_impact_percentage = 0
        if project_budget and budget_impact:
            total_budget = project_budget.get("total_budget", 0)
            budget_impact_percentage = (
                (budget_impact / total_budget * 100) if total_budget > 0 else 0
            )

        allocations = list(data.get("allocations", {}).values())
        resource_conflicts = []
        for req in resource_requirements:
            emp_id = req.get("employee_id")
            emp_allocations = [
                a
                for a in allocations
                if a.get("employee_id") == emp_id and a.get("status") == "active"
            ]
            total_hours = sum(a.get("hours_per_week", 0) for a in emp_allocations)
            if total_hours + req.get("hours_per_week", 0) > 40:
                resource_conflicts.append(emp_id)

        critical_paths = list(data.get("critical_paths", {}).values())
        project_critical_path = next(
            (
                cp
                for cp in critical_paths
                if cp.get("project_id") == cr.get("project_id")
            ),
            None,
        )
        affects_critical_path = False
        if project_critical_path and timeline_impact_weeks > 0:
            affects_critical_path = True

        requires_risk_assessment = affects_critical_path

        approval_levels_required = ["project_manager"]
        if budget_impact > 50000 or budget_impact_percentage > 10:
            approval_levels_required.append("finance")
        if affects_critical_path or timeline_impact_weeks > 4:
            approval_levels_required.append("pmo_director")
        if cr.get("priority") == "critical" or budget_impact > 100000:
            approval_levels_required.append("executive_sponsor")

        risk_score = 0
        if timeline_impact_weeks > 8:
            risk_score += 3
        elif timeline_impact_weeks > 4:
            risk_score += 2
        elif timeline_impact_weeks > 0:
            risk_score += 1

        if budget_impact_percentage > 20:
            risk_score += 3
        elif budget_impact_percentage > 10:
            risk_score += 2
        elif budget_impact_percentage > 5:
            risk_score += 1

        if len(resource_conflicts) > 2:
            risk_score += 3
        elif len(resource_conflicts) > 0:
            risk_score += 2

        overall_risk = (
            "critical"
            if risk_score >= 6
            else "high"
            if risk_score >= 4
            else "medium"
            if risk_score >= 2
            else "low"
        )

        assessment_id = f"ia_{uuid.uuid4().hex[:8]}"

        impact_assessment = {
            "assessment_id": assessment_id,
            "cr_id": cr_id,
            "assessed_by": assessed_by,
            "assessment_date": datetime.now().isoformat(),
            "timeline_impact_weeks": timeline_impact_weeks,
            "budget_impact": budget_impact,
            "budget_impact_percentage": round(budget_impact_percentage, 1),
            "resource_requirements": resource_requirements,
            "resource_conflicts": resource_conflicts,
            "technical_dependencies": technical_dependencies,
            "affects_critical_path": affects_critical_path,
            "requires_risk_assessment": requires_risk_assessment,
            "approval_levels_required": approval_levels_required,
            "overall_risk": overall_risk,
        }

        cr["impact_assessment"] = impact_assessment
        cr["approvals_required"] = approval_levels_required
        cr["requires_risk_assessment"] = requires_risk_assessment

        return json.dumps({"success": True, "impact_assessment": impact_assessment})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "perform_impact_assessment",
                "description": "Perform impact assessment for a change request",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cr_id": {"type": "string", "description": "Change request ID"},
                        "assessed_by": {
                            "type": "string",
                            "description": "ID of person performing assessment",
                        },
                        "timeline_impact_weeks": {
                            "type": "number",
                            "description": "Impact on timeline in weeks",
                        },
                        "budget_impact": {
                            "type": "number",
                            "description": "Budget impact in dollars",
                        },
                        "resource_requirements": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "employee_id": {"type": "string"},
                                    "hours_per_week": {"type": "number"},
                                    "duration_weeks": {"type": "number"},
                                },
                            },
                            "description": "Additional resource requirements",
                        },
                        "technical_dependencies": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Technical dependencies",
                        },
                    },
                    "required": ["cr_id", "assessed_by"],
                },
            },
        }
