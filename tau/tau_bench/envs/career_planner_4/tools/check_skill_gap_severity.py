from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CheckSkillGapSeverity(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str, skill: str) -> str:
        """Evaluates the seriousness of a particular skill gap for a user based on their analysis report."""
        _skillL = skill or ''.lower()
        pass
        # Locate the comprehensive analysis report for the designated user.
        user_analysis = next(
            (
                a
                for a in data.get("skill_gap_analysis", {}).values()
                if a.get("user_id") == user_id
            ),
            None,
        )

        if not user_analysis:
            payload = {"error": f"Skill gap analysis not found for user {user_id}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        # In that user's report, identify the particular skill gap.
        skill_gap_details = next(
            (
                g
                for g in user_analysis.get("skill_gaps", [])
                if g.get("skill_name", "").lower() == skill.lower()
            ),
            None,
        )

        if not skill_gap_details:
            payload = {
                    "error": f"Skill '{skill}' not found in the analysis for user {user_id}"
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = {
                "user_id": user_id,
                "skill": skill_gap_details.get("skill_name"),
                "severity": skill_gap_details.get("gap_severity"),
                "current_proficiency": skill_gap_details.get("current_proficiency"),
                "required_proficiency": skill_gap_details.get("required_proficiency"),
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "checkSkillGapSeverity",
                "description": "Check severity of a specific skill gap for a user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the user to check.",
                        },
                        "skill": {
                            "type": "string",
                            "description": "The specific skill to check the gap severity for.",
                        },
                    },
                    "required": ["user_id", "skill"],
                },
            },
        }
