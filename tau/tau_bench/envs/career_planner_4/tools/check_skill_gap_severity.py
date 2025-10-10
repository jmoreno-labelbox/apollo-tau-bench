# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class check_skill_gap_severity(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id: str, skill: str) -> str:
        """
        Checks the severity of a specific skill gap for a user from their analysis report.
        """
        # Retrieve the comprehensive analysis report for the designated user.
        user_analysis = next(
            (
                a
                for a in data.get("skill_gap_analysis", [])
                if a.get("user_id") == user_id
            ),
            None,
        )

        if not user_analysis:
            return json.dumps(
                {"error": f"Skill gap analysis not found for user {user_id}"}, indent=2
            )

        # Identify the precise skill deficiency in the user's report.
        skill_gap_details = next(
            (
                g
                for g in user_analysis.get("skill_gaps", [])
                if g.get("skill_name", "").lower() == skill.lower()
            ),
            None,
        )

        if not skill_gap_details:
            return json.dumps(
                {
                    "error": f"Skill '{skill}' not found in the analysis for user {user_id}"
                },
                indent=2,
            )

        # Retrieve the information directly from the identified skill gap record.
        return json.dumps(
            {
                "user_id": user_id,
                "skill": skill_gap_details.get("skill_name"),
                "severity": skill_gap_details.get("gap_severity"),
                "current_proficiency": skill_gap_details.get("current_proficiency"),
                "required_proficiency": skill_gap_details.get("required_proficiency"),
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "check_skill_gap_severity",
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
