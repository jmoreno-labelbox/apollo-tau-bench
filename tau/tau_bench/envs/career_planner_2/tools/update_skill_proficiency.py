from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class UpdateSkillProficiency(Tool):
    """Revise the proficiency level of a user's skills."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, skill: str = None, new_level: int = None) -> str:
        uid = user_id
        skill = skill
        level = new_level
        skills = data.setdefault("user_skills", [])
        skills[:] = [
            s for s in skills if not (s["user_id"] == uid and s["skill"] == skill)
        ]
        skills.append(
            {
                "user_id": uid,
                "skill": skill,
                "proficiency_level": level,
                "updated_date": datetime.utcnow().date().isoformat(),
            }
        )
        payload = {"success": f"{uid} {skill} -> {level}"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateSkillProficiency",
                "description": "Update skill level.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "skill": {"type": "string"},
                        "new_level": {"type": "string"},
                    },
                    "required": ["user_id", "skill", "new_level"],
                },
            },
        }
