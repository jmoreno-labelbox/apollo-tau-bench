# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CompareAgainstBaseline(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id = kwargs.get("project_id")

        if not project_id:
            return json.dumps({"error": "project_id is required"})

        scope_baselines = data.get("scope_baselines", [])
        change_requests = data.get("change_requests", [])
        deliverables = data.get("deliverables", [])

        if baseline_version := kwargs.get("baseline_version"):
            baseline = next(
                (
                    b
                    for b in scope_baselines
                    if b.get("project_id") == project_id
                    and b.get("version") == baseline_version
                ),
                None,
            )
        else:

            baseline = next(
                (
                    b
                    for b in scope_baselines
                    if b.get("project_id") == project_id
                    and b.get("status") == "approved"
                ),
                None,
            )

        if not baseline:
            return json.dumps(
                {"error": f"No baseline found for project '{project_id}'"}
            )

        baseline_date = baseline.get("approved_date", baseline.get("created_date"))
        approved_changes = [
            cr
            for cr in change_requests
            if cr.get("project_id") == project_id
            and cr.get("status") == "approved"
            and cr.get("approval_date", "") > baseline_date
        ]

        scope_additions = []
        scope_reductions = []
        requirement_changes = []

        for cr in approved_changes:
            if cr.get("change_type") == "scope_addition":
                scope_additions.append(
                    {
                        "cr_id": cr.get("cr_id"),
                        "title": cr.get("title"),
                        "impact": cr.get("impact_assessment", {}),
                    }
                )
            elif cr.get("change_type") == "scope_reduction":
                scope_reductions.append(
                    {
                        "cr_id": cr.get("cr_id"),
                        "title": cr.get("title"),
                        "impact": cr.get("impact_assessment", {}),
                    }
                )
            elif cr.get("change_type") == "requirement_change":
                requirement_changes.append(
                    {
                        "cr_id": cr.get("cr_id"),
                        "title": cr.get("title"),
                        "impact": cr.get("impact_assessment", {}),
                    }
                )

        total_budget_impact = sum(
            cr.get("impact_assessment", {}).get("budget_impact", 0)
            for cr in approved_changes
        )
        total_timeline_impact = sum(
            cr.get("impact_assessment", {}).get("timeline_impact_weeks", 0)
            for cr in approved_changes
        )

        baseline_deliverable_ids = [
            d.get("deliverable_id") for d in baseline.get("deliverables", [])
        ]
        current_deliverable_ids = [
            d.get("deliverable_id")
            for d in deliverables
            if d.get("project_id") == project_id
        ]

        added_deliverables = list(
            set(current_deliverable_ids) - set(baseline_deliverable_ids)
        )
        removed_deliverables = list(
            set(baseline_deliverable_ids) - set(current_deliverable_ids)
        )

        variance_report = {
            "project_id": project_id,
            "baseline_version": baseline.get("version"),
            "baseline_date": baseline_date,
            "approved_changes_count": len(approved_changes),
            "scope_additions": scope_additions,
            "scope_reductions": scope_reductions,
            "requirement_changes": requirement_changes,
            "cumulative_impact": {
                "budget_variance": total_budget_impact,
                "timeline_variance_weeks": total_timeline_impact,
                "deliverables_added": len(added_deliverables),
                "deliverables_removed": len(removed_deliverables),
            },
            "variance_percentage": round(
                (
                    len(approved_changes)
                    / max(1, len(baseline.get("scope_items", [])))
                    * 100
                ),
                1,
            ),
            "recommendation": "Consider rebaselining"
            if len(approved_changes) > 5 or total_timeline_impact > 8
            else "Within acceptable variance",
        }

        return json.dumps(variance_report, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "compare_against_baseline",
                "description": "Compare current project scope against baseline",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "Project ID"},
                        "baseline_version": {
                            "type": "string",
                            "description": "Specific baseline version (optional, uses latest if not provided)",
                        },
                    },
                    "required": ["project_id"],
                },
            },
        }
