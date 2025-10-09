from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class RecommendSkillTraining(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, skill: str = None) -> str:
        # Confirm that the skill is pertinent to available roles
        valid_skills = set()
        for role_entry in data.get("role_skill_catalog", {}).values():
            skills = role_entry.get("required_skills", [])
            if isinstance(skills, list):
                for skill_item in skills:
                    if isinstance(skill_item, str):
                        valid_skills.add(skill_item)
                    elif isinstance(skill_item, dict) and skill_item.get("skill"):
                        valid_skills.add(skill_item.get("skill"))

        # If the skill is absent from the catalog, omit the recommendation
        if skill not in valid_skills:
            return f"Skill '{skill}' not found in catalog - no training recommendation made"

        # Generate a training recommendation containing only necessary data
        recommendation = {
            "user_id": user_id,
            "skill": skill,
            "timestamp": datetime.now().isoformat(),
        }
        data.setdefault("training_recommendations", []).append(recommendation)
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
