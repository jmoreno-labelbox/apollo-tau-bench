from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class RecommendSkillTraining(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, skill: str = None) -> str:
        # Verify that the skill is relevant to the open positions.
        valid_skills = set()
        for role_entry in data.get("role_skill_catalog", {}).values():
            skills = role_entry.get("required_skills", [])
            if isinstance(skills, list):
                for skill_item in skills:
                    if isinstance(skill_item, str):
                        valid_skills.add(skill_item)
                    elif isinstance(skill_item, dict) and skill_item.get("skill"):
                        valid_skills.add(skill_item.get("skill"))

        # Exclude the recommendation if the skill is not listed in the catalog.
        if skill not in valid_skills:
            return f"Skill '{skill}' not found in catalog - no training recommendation made"

        # Create a training suggestion that includes only essential information.
        recommendation = {
            "user_id": user_id,
            "skill": skill,
            "timestamp": datetime.now().isoformat(),
        }
        table = data.setdefault("training_recommendations", {})
        key = f"{len(table)}"
        table[key] = recommendation
        return f"{user_id} needs {skill} training"
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RecommendSkillTraining",
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
