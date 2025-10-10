# Sierra copyright.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetScheduleVariance(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], baseline_id, project_id) -> str:

        if not project_id:
            return json.dumps({"error": "project_id is required"})

        milestones = list(data.get("milestones", {}).values())
        schedule_baselines = data.get("schedule_baselines", [])

        project_milestones = [
            m for m in milestones if m.get("project_id") == project_id
        ]

        if baseline_id := baseline_id:
            baseline = next(
                (b for b in schedule_baselines if b.get("baseline_id") == baseline_id),
                None,
            )
        else:

            project_baselines = [
                b for b in schedule_baselines if b.get("project_id") == project_id
            ]
            baseline = (
                max(project_baselines, key=lambda x: x.get("created_date"))
                if project_baselines
                else None
            )

        if not baseline:
            return json.dumps(
                {"error": f"No baseline found for project '{project_id}'"}
            )

        variance_analysis = []
        total_variance_days = 0

        for milestone in project_milestones:

            baseline_snapshot = next(
                (
                    s
                    for s in baseline.get("milestone_snapshots", [])
                    if s.get("milestone_id") == milestone.get("milestone_id")
                ),
                None,
            )

            if baseline_snapshot:
                baseline_target = datetime.fromisoformat(
                    baseline_snapshot.get("baseline_target").replace("Z", "+00:00")
                )
                current_target = datetime.fromisoformat(
                    milestone.get("target_date").replace("Z", "+00:00")
                )

                variance_days = (current_target - baseline_target).days
                variance_percentage = (
                    variance_days
                    / max((baseline_target - datetime.now(timezone.utc)).days, 1)
                ) * 100

                original_variance_days = None
                original_variance_percentage = None
                if baseline_snapshot.get("original_baseline_target"):
                    orig_target = datetime.fromisoformat(
                        baseline_snapshot.get("original_baseline_target").replace(
                            "Z", "+00:00"
                        )
                    )
                    original_variance_days = (current_target - orig_target).days
                    original_variance_percentage = (
                        original_variance_days
                        / max((orig_target - datetime.now(timezone.utc)).days, 1)
                    ) * 100

                variance_analysis.append(
                    {
                        "milestone_id": milestone.get("milestone_id"),
                        "milestone_name": milestone.get("milestone_name"),
                        "baseline_target": baseline_snapshot.get("baseline_target"),
                        "current_target": milestone.get("target_date"),
                        "variance_days": variance_days,
                        "variance_percentage": round(variance_percentage, 1),
                        "original_baseline_target": baseline_snapshot.get(
                            "original_baseline_target"
                        ),
                        "original_variance_days": original_variance_days,
                        "original_variance_percentage": round(
                            original_variance_percentage, 1
                        )
                        if original_variance_percentage
                        else None,
                        "requires_executive_approval": original_variance_percentage
                        and abs(original_variance_percentage) > 20,
                        "status": milestone.get("status"),
                        "health": milestone.get("health"),
                    }
                )

                total_variance_days += abs(variance_days)

        variance_analysis.sort(key=lambda x: x["variance_days"], reverse=True)

        avg_variance = (
            total_variance_days / len(variance_analysis) if variance_analysis else 0
        )

        requiring_approval = [
            v for v in variance_analysis if v.get("requires_executive_approval", False)
        ]

        return json.dumps(
            {
                "delayed_milestones": len(
                    [v for v in variance_analysis if v["variance_days"] > 0]
                ),
                "project_id": project_id,
                "baseline_id": baseline.get("baseline_id"),
                "baseline_name": baseline.get("baseline_name"),
                "baseline_type": baseline.get("baseline_type"),
                "variance_analysis": variance_analysis,
                "summary": {
                    "total_milestones": len(variance_analysis),
                    "delayed_milestones": len(
                        [v for v in variance_analysis if v["variance_days"] > 0]
                    ),
                    "ahead_milestones": len(
                        [v for v in variance_analysis if v["variance_days"] < 0]
                    ),
                    "on_track_milestones": len(
                        [v for v in variance_analysis if v["variance_days"] == 0]
                    ),
                    "average_variance_days": round(avg_variance, 1),
                    "max_delay_days": max(
                        (v["variance_days"] for v in variance_analysis), default=0
                    ),
                    "milestones_requiring_executive_approval": len(requiring_approval),
                },
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_schedule_variance",
                "description": "Analyze schedule variance against baseline",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "Project ID"},
                        "baseline_id": {
                            "type": "string",
                            "description": "Specific baseline ID (optional)",
                        },
                    },
                    "required": ["project_id"],
                },
            },
        }
