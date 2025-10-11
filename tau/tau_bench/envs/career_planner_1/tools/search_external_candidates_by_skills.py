from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class SearchExternalCandidatesBySkills(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], required_skills: list = None) -> str:
        required_skills_raw = required_skills if required_skills is not None else []

        # Diligently retrieve skill names from potentially unstructured data.
        required = set()
        for skill_item in required_skills_raw:
            if isinstance(skill_item, str):
                required.add(skill_item)
            elif isinstance(skill_item, dict) and skill_item.get("skill"):
                required.add(skill_item.get("skill"))

        talent_network = data.get("talent_network", {}).values()

        # Check: Verify that the talent network has been successfully loaded.
        if not talent_network:
            payload = {"error": "Talent network not loaded", "matches": []}
            out = json.dumps(
                payload, indent=2
            )
            return out

        matches = []
        for c in talent_network:
            # Extract skill names from candidate skills to support both formats.
            candidate_skills = set()
            cand_skills = c.get("skills", [])

            if isinstance(cand_skills, list):
                for skill in cand_skills:
                    if isinstance(skill, str):
                        candidate_skills.add(skill)
                    elif isinstance(skill, dict) and skill.get("skill"):
                        candidate_skills.add(skill.get("skill"))

            # Validate matches - handle both direct matches and skills in a hierarchy.
            has_match = False

            # First, verify for a direct intersection.
            if required.intersection(candidate_skills):
                has_match = True
            else:
                # Analyze hierarchical matches by expanding necessary skills.
                expanded_required = set()
                for req_skill in required:
                    expanded_required.add(req_skill)
                    # Find this skill in the role catalog to identify detailed skills.
                    for role_entry in data.get("role_skill_catalog", {}).values():
                        for skill_category in role_entry.get("required_skills", []):
                            if (
                                isinstance(skill_category, dict)
                                and skill_category.get("skill") == req_skill
                            ):
                                specific_skills = skill_category.get(
                                    "specific_skills", []
                                )
                                expanded_required.update(specific_skills)

                if expanded_required.intersection(candidate_skills):
                    has_match = True

            if has_match:
                matches.append(c)
        payload = matches
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchExternalCandidatesBySkills",
                "description": "Search talent network candidates by skill match.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "required_skills": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of skills required for the role",
                        }
                    },
                    "required": ["required_skills"],
                },
            },
        }
