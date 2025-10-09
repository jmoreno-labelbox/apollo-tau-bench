from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class RecommendCourseForGap(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, target_role: str = None) -> str:
        gaps = data.get("skill_gap_analysis", {}).values()
        user_gaps = [
            g
            for g in gaps.values() if g["user_id"] == user_id and g["target_role"] == target_role
        ]

        if not user_gaps:
            payload = {"error": "No gap found."}
            out = json.dumps(payload, indent=2)
            return out

        # Identify the most critical skill gap along with the courses that are offered
        skill_gaps = user_gaps[0].get("skill_gaps", [])
        highest_priority_gap = None

        # Arrange by priority (High to Low) and severity of the gap (High to Low)
        priority_order = {"High": 3, "Medium": 2, "Low": 1}
        severity_order = {"High": 3, "Medium": 2, "Low": 1}

        for skill_gap in skill_gaps:
            if skill_gap.get("recommended_courses"):
                if not highest_priority_gap:
                    highest_priority_gap = skill_gap
                else:
                    # Evaluate based on priority initially, followed by severity
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
            payload = {
                "recommended_course": highest_priority_gap.get(
                    "recommended_courses"
                )[0],
                "skill": highest_priority_gap.get("skill_name"),
                "priority": highest_priority_gap.get("priority"),
                "gap_severity": highest_priority_gap.get("gap_severity"),
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = {"error": "No suitable course found."}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RecommendCourseForGap",
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
