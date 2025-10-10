# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateSkillProficiency(Tool):
    """Update user skill proficiency level."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        uid = kwargs.get("user_id")
        skill = kwargs.get("skill")
        level = kwargs.get("new_level")
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
        return json.dumps({"success": f"{uid} {skill} -> {level}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_skill_proficiency",
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
