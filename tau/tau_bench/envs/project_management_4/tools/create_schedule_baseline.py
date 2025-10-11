# Copyright Sierra

import datetime, uuid
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateScheduleBaseline(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], approval_ref, baseline_name, project_id, baseline_id = f"base_{uuid.uuid4().hex[:8]}", baseline_type = "initial", create_date = datetime.now(timezone.utc).isoformat(), executive_approval = False, notes = "", pmo_approval = False) -> str:

        if not all([project_id, baseline_name]):
            return json.dumps({"error": "project_id and baseline_name are required"})

        milestones = list(data.get("milestones", {}).values())
        schedule_baselines = data.get("schedule_baselines", [])

        current_quarter = (datetime.now(timezone.utc).month - 1) // 3 + 1
        current_year = datetime.now(timezone.utc).year

        quarterly_baselines = [
            b
            for b in schedule_baselines
            if b.get("project_id") == project_id
            and b.get("year") == current_year
            and b.get("quarter") == current_quarter
            and b.get("baseline_type") != "initial"
        ]

        if len(quarterly_baselines) >= 1 and not pmo_approval:
            return json.dumps(
                {
                    "error": "Only one baseline update allowed per quarter without PMO approval. Set pmo_approval=True if approved."
                }
            )

        project_milestones = [
            m for m in milestones if m.get("project_id") == project_id
        ]

        if not project_milestones:
            return json.dumps(
                {"error": f"No milestones found for project '{project_id}'"}
            )

        downstream_impacts = []
        for milestone in project_milestones:

            deps = data.get("milestone_dependencies", [])
            successors = [
                d.get("successor_id")
                for d in deps
                if d.get("predecessor_id") == milestone.get("milestone_id")
            ]

            if successors:
                downstream_impacts.append(
                    {
                        "milestone_id": milestone.get("milestone_id"),
                        "milestone_name": milestone.get("milestone_name"),
                        "downstream_count": len(successors),
                        "downstream_milestones": successors,
                    }
                )

        milestone_snapshots = []
        max_variance = 0

        for milestone in project_milestones:

            original_baseline_start = milestone.get(
                "original_baseline_start",
                milestone.get("baseline_start", milestone.get("start_date")),
            )
            original_baseline_target = milestone.get(
                "original_baseline_target",
                milestone.get("baseline_target", milestone.get("target_date")),
            )

            snapshot = {
                "milestone_id": milestone.get("milestone_id"),
                "milestone_name": milestone.get("milestone_name"),
                "baseline_start": milestone.get("start_date"),
                "baseline_target": milestone.get("target_date"),
                "current_start": milestone.get("start_date"),
                "current_target": milestone.get("target_date"),
                "original_baseline_start": original_baseline_start,
                "original_baseline_target": original_baseline_target,
                "variance_days": 0,
            }

            orig_target = datetime.fromisoformat(
                original_baseline_target.replace("Z", "+00:00")
            )
            curr_target = datetime.fromisoformat(
                milestone.get("target_date").replace("Z", "+00:00")
            )
            variance_days = (curr_target - orig_target).days
            variance_percentage = (
                abs(variance_days)
                / max((orig_target - datetime.now(timezone.utc)).days, 1)
                * 100
            )

            snapshot["variance_from_original_days"] = variance_days
            snapshot["variance_from_original_percentage"] = round(
                variance_percentage, 1
            )

            milestone_snapshots.append(snapshot)

            if variance_percentage > 20 and not executive_approval:
                return json.dumps(
                    {
                        "error": f"Milestone '{milestone.get('milestone_name')}' has {variance_percentage:.1f}% variance from original baseline. Executive approval required."
                    }
                )

        new_baseline = {
            "baseline_id": baseline_id,
            "project_id": project_id,
            "baseline_name": baseline_name,
            "baseline_type": baseline_type,
            "approval_ref": approval_ref,
            "pmo_approval": pmo_approval,
            "executive_approval": executive_approval,
            "notes": notes,
            "milestone_count": len(milestone_snapshots),
            "max_variance_days": max_variance,
            "variance_percentage": 0,
            "milestone_snapshots": milestone_snapshots,
            "downstream_impacts": downstream_impacts,
            "created_date": create_date,
            "year": datetime.fromisoformat(create_date).year,
            "quarter": (datetime.now(timezone.utc).month - 1) // 3 + 1,
        }

        schedule_baselines.append(new_baseline)

        for milestone in project_milestones:
            if "original_baseline_start" not in milestone:
                milestone["original_baseline_start"] = milestone.get(
                    "baseline_start", milestone.get("start_date")
                )
            if "original_baseline_target" not in milestone:
                milestone["original_baseline_target"] = milestone.get(
                    "baseline_target", milestone.get("target_date")
                )

            milestone["baseline_start"] = milestone.get("start_date")
            milestone["baseline_target"] = milestone.get("target_date")

        return json.dumps({"success": True, "baseline": new_baseline})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_schedule_baseline",
                "description": "Create a schedule baseline for a project",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "Project ID"},
                        "baseline_id": {"type": "string", "description": "Baseline ID"},
                        "create_date": {"type": "date", "description": "Creation date"},
                        "baseline_name": {
                            "type": "string",
                            "description": "Name of the baseline",
                        },
                        "baseline_type": {
                            "type": "string",
                            "description": "Type: initial, quarterly, rebaseline",
                        },
                        "approval_ref": {
                            "type": "string",
                            "description": "Approval reference number",
                        },
                        "notes": {
                            "type": "string",
                            "description": "Notes about the baseline",
                        },
                        "pmo_approval": {
                            "type": "boolean",
                            "description": "PMO approval for multiple quarterly updates",
                        },
                        "executive_approval": {
                            "type": "boolean",
                            "description": "Executive approval for >20% variance",
                        },
                    },
                    "required": ["project_id", "baseline_name"],
                },
            },
        }
