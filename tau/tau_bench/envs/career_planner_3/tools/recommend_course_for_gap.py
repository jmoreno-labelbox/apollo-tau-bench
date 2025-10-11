# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RecommendCourseForGap(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], target_role, user_id) -> str:
        gaps = data.get("skill_gap_analysis", [])
        user_gaps = [
            g
            for g in gaps
            if g["user_id"] == user_id and g["target_role"] == target_role
        ]

        if not user_gaps:
            return json.dumps({"error": "No gap found."}, indent=2)

        # Identify the most critical skill deficiency alongside the corresponding courses.
        skill_gaps = user_gaps[0].get("skill_gaps", [])
        highest_priority_gap = None

        # Order by priority (High, Medium, Low) and severity of gap (High, Medium, Low).
        priority_order = {"High": 3, "Medium": 2, "Low": 1}
        severity_order = {"High": 3, "Medium": 2, "Low": 1}

        for skill_gap in skill_gaps:
            if skill_gap.get("recommended_courses"):
                if not highest_priority_gap:
                    highest_priority_gap = skill_gap
                else:
                    # First, compare based on priority, followed by severity.
                    current_priority = priority_order.get(
                        skill_gap.get("priority", "Low"), 1
                    )
                    current_severity = severity_order.get(
                        skill_gap.get("gap_severity", "Low"), 1
                    )

                    best_priority = priority_order.get(
                        highest_priority_gap.get("priority", "Low"), 1
                    )
                    best_severity = severity_order.get(
                        highest_priority_gap.get("gap_severity", "Low"), 1
                    )

                    if current_priority > best_priority or (
                        current_priority == best_priority
                        and current_severity > best_severity
                    ):
                        highest_priority_gap = skill_gap

        if highest_priority_gap:
            # Retrieve the initial course for the highest priority gap (deterministic).
            return json.dumps(
                {
                    "recommended_course": highest_priority_gap.get(
                        "recommended_courses"
                    )[0],
                    "skill": highest_priority_gap.get("skill_name"),
                    "priority": highest_priority_gap.get("priority"),
                    "gap_severity": highest_priority_gap.get("gap_severity"),
                },
                indent=2,
            )

        return json.dumps({"error": "No suitable course found."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "recommend_course_for_gap",
                "description": "Recommends the highest priority course from the catalog to close a user's skill gap for a target role.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the user.",
                        },
                        "target_role": {
                            "type": "string",
                            "description": "The role the user is targeting.",
                        },
                    },
                    "required": ["user_id", "target_role"],
                },
            },
        }
