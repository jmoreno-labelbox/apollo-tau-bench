# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RecommendSkillTraining(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get("user_id")
        skill = kwargs.get("skill")

        # Validate that the skill is relevant for available roles
        valid_skills = set()
        for role_entry in data.get("role_skill_catalog", []):
            skills = role_entry.get("required_skills", [])
            if isinstance(skills, list):
                for skill_item in skills:
                    if isinstance(skill_item, str):
                        valid_skills.add(skill_item)
                    elif isinstance(skill_item, dict) and skill_item.get("skill"):
                        valid_skills.add(skill_item.get("skill"))

        # If skill not in catalog, skip recommendation
        if skill not in valid_skills:
            return f"Skill '{skill}' not found in catalog - no training recommendation made"

        # Create training recommendation with only essential data
        recommendation = {
            "user_id": user_id,
            "skill": skill,
            "timestamp": datetime.now().isoformat(),
        }
        data.setdefault("training_recommendations", []).append(recommendation)
        return f"{user_id} needs {skill} training"

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "recommend_skill_training",
                "description": "Adds a training recommendation for a user on a specific skill.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "User receiving recommendation",
                        },
                        "skill": {"type": "string", "description": "Skill to develop"},
                    },
                    "required": ["user_id", "skill"],
                },
            },
        }
