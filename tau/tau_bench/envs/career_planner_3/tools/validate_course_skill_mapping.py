# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ValidateCourseSkillMapping(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        course_id = kwargs.get("course_id")
        skill_name = kwargs.get("skill_name")
        courses = data.get("course_catalog", [])

        course = None
        for c in courses:
            if c["course_id"] == course_id:
                course = c
                break

        if not course:
            return json.dumps(
                {"valid": False, "error": "Course not found", "course_id": course_id},
                indent=2,
            )

        # Check if skill is covered by the course
        skills_covered = []
        for skill_imparted in course.get("skills_imparted", []):
            skills_covered.append(skill_imparted.get("skill", ""))

        if skill_name in skills_covered:
            return json.dumps(
                {
                    "valid": True,
                    "course_id": course_id,
                    "skill_name": skill_name,
                    "course_name": course.get("name", ""),
                },
                indent=2,
            )

        return json.dumps(
            {
                "valid": False,
                "error": "Skill not covered by course",
                "course_id": course_id,
                "skill_name": skill_name,
                "skills_covered": skills_covered,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "validate_course_skill_mapping",
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
