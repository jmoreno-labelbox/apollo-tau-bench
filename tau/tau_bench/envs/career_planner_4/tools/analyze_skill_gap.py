# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class analyze_skill_gap(Tool):
    @staticmethod
    def invoke(
        data,
        user_id: str,
        skill: str,
        current_level: str,
        required_level: str,
        recommended_courses: list,
    ) -> str:
        analysis = {
            "analysis_id": "SGA005",
            "user_id": user_id,
            "skill": skill,
            "current_proficiency": current_level,
            "required_proficiency": required_level,
            "recommended_courses": recommended_courses,
        }
        data.setdefault("skill_gap_analysis", []).append(analysis)
        return json.dumps(analysis, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "analyze_skill_gap",
                "description": "Perform and log a skill gap analysis for a given user and skill.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "skill": {"type": "string"},
                        "current_level": {"type": "string"},
                        "required_level": {"type": "string"},
                        "recommended_courses": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                    },
                    "required": [
                        "user_id",
                        "skill",
                        "current_level",
                        "required_level",
                        "recommended_courses",
                    ],
                },
            },
        }
