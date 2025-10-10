# © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetDelayedMilestones(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], project_id, include_recovery_plans = False) -> str:

        milestones = list(data.get("milestones", {}).values())
        recovery_plans = data.get("recovery_plans", [])

        if project_id:
            project_milestones = [
                m for m in milestones if m.get("project_id") == project_id
            ]
        else:
            project_milestones = milestones

        delayed_milestones = []

        for milestone in project_milestones:

            is_delayed = (
                milestone.get("float_days", 0) < 0
                or milestone.get("health") == "red"
                or milestone.get("status") == "delayed"
            )

            if is_delayed:
                delayed_info = {
                    "milestone_id": milestone.get("milestone_id"),
                    "milestone_name": milestone.get("milestone_name"),
                    "project_id": milestone.get("project_id"),
                    "target_date": milestone.get("target_date"),
                    "float_days": milestone.get("float_days", 0),
                    "health": milestone.get("health"),
                    "status": milestone.get("status"),
                    "owner_id": milestone.get("owner_id"),
                    "is_critical_path": milestone.get("is_critical_path"),
                    "resource_allocation": milestone.get("resource_allocation", 100),
                }

                if include_recovery_plans:

                    milestone_recovery_plans = [
                        rp
                        for rp in recovery_plans
                        if rp.get("milestone_id") == milestone.get("milestone_id")
                    ]
                    delayed_info["recovery_plans"] = milestone_recovery_plans
                    delayed_info["has_recovery_plan"] = (
                        len(milestone_recovery_plans) > 0
                    )

                delayed_milestones.append(delayed_info)

        delayed_milestones.sort(key=lambda x: x["float_days"])

        critical_delays_over_5 = [
            m
            for m in delayed_milestones
            if m["is_critical_path"] and m["float_days"] < -5
        ]

        return json.dumps(
            {
                "delayed_count": len(delayed_milestones),
                "delayed_milestones": delayed_milestones,
                "critical_delays": len(
                    [m for m in delayed_milestones if m["is_critical_path"]]
                ),
                "critical_delays_requiring_impact_analysis": len(
                    critical_delays_over_5
                ),
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_delayed_milestones",
                "description": "Get all delayed milestones with optional recovery plan information",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {
                            "type": "string",
                            "description": "Filter by project ID (optional)",
                        },
                        "include_recovery_plans": {
                            "type": "boolean",
                            "description": "Include recovery plan information",
                        },
                    },
                },
            },
        }
