# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CheckMilestoneFloat(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id = kwargs.get("project_id")

        if not project_id:
            return json.dumps({"error": "project_id is required"})

        milestones = list(data.get("milestones", {}).values())
        project_milestones = [
            m for m in milestones if m.get("project_id") == project_id
        ]

        float_analysis = []

        for milestone in project_milestones:
            float_days = milestone.get("float_days", 0)
            is_critical = milestone.get("is_critical_path", False)

            if float_days < 0:
                float_status = "negative"
                risk_level = "critical"
            elif float_days == 0:
                float_status = "zero"
                risk_level = "high"
            elif float_days <= 5:
                float_status = "low"
                risk_level = "medium"
            else:
                float_status = "comfortable"
                risk_level = "low"

            float_analysis.append(
                {
                    "milestone_id": milestone.get("milestone_id"),
                    "milestone_name": milestone.get("milestone_name"),
                    "float_days": float_days,
                    "float_status": float_status,
                    "risk_level": risk_level,
                    "is_critical_path": is_critical,
                    "target_date": milestone.get("target_date"),
                    "status": milestone.get("status"),
                    "resource_allocation": milestone.get("resource_allocation", 100),
                }
            )

        float_analysis.sort(key=lambda x: x["float_days"])

        summary = {
            "negative_float": len(
                [f for f in float_analysis if f["float_status"] == "negative"]
            ),
            "zero_float": len(
                [f for f in float_analysis if f["float_status"] == "zero"]
            ),
            "low_float": len([f for f in float_analysis if f["float_status"] == "low"]),
            "comfortable_float": len(
                [f for f in float_analysis if f["float_status"] == "comfortable"]
            ),
            "critical_path_count": len(
                [f for f in float_analysis if f["is_critical_path"]]
            ),
        }

        return json.dumps(
            {
                "project_id": project_id,
                "float_analysis": float_analysis,
                "summary": summary,
                "total_milestones": len(float_analysis),
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "check_milestone_float",
                "description": "Check float/slack time for all project milestones",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "Project ID"}
                    },
                    "required": ["project_id"],
                },
            },
        }
