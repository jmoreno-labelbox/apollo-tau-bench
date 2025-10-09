from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ValidateCourseSkillMapping(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], course_id: str = None, skill_name: str = None) -> str:
        courses = data.get("course_catalog", {}).values()

        course = None
        for c in courses:
            if c["course_id"] == course_id:
                course = c
                break

        if not course:
            payload = {"valid": False, "error": "Course not found", "course_id": course_id}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        # Verify whether the course includes the skill
        skills_covered = []
        for skill_imparted in course.get("skills_imparted", []):
            skills_covered.append(skill_imparted.get("skill", ""))

        if skill_name in skills_covered:
            payload = {
                    "valid": True,
                    "course_id": course_id,
                    "skill_name": skill_name,
                    "course_name": course.get("name", ""),
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        payload = {
                "valid": False,
                "error": "Skill not covered by course",
                "course_id": course_id,
                "skill_name": skill_name,
                "skills_covered": skills_covered,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ValidateCourseSkillMapping",
                "description": "Validates that a course covers a specific skill.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "course_id": {
                            "type": "string",
                            "description": "The ID of the course to validate.",
                        },
                        "skill_name": {
                            "type": "string",
                            "description": "The skill to check coverage for.",
                        },
                    },
                    "required": ["course_id", "skill_name"],
                },
            },
        }
