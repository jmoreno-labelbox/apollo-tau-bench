# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchExternalCandidatesBySkills(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        required_skills_raw = kwargs.get("required_skills", [])

        # Safely extract skill names from potentially mixed data
        required = set()
        for skill_item in required_skills_raw:
            if isinstance(skill_item, str):
                required.add(skill_item)
            elif isinstance(skill_item, dict) and skill_item.get("skill"):
                required.add(skill_item.get("skill"))

        talent_network = data.get("talent_network", [])

        # Debug: Check if talent network is loaded
        if not talent_network:
            return json.dumps(
                {"error": "Talent network not loaded", "matches": []}, indent=2
            )

        matches = []
        for c in talent_network:
            # Extract skill names from candidate skills - handle both formats
            candidate_skills = set()
            cand_skills = c.get("skills", [])

            if isinstance(cand_skills, list):
                for skill in cand_skills:
                    if isinstance(skill, str):
                        candidate_skills.add(skill)
                    elif isinstance(skill, dict) and skill.get("skill"):
                        candidate_skills.add(skill.get("skill"))

            # Check for matches - handle both direct matches and hierarchical skills
            has_match = False

            # First check direct intersection
            if required.intersection(candidate_skills):
                has_match = True
            else:
                # Check hierarchical matches by expanding required skills
                expanded_required = set()
                for req_skill in required:
                    expanded_required.add(req_skill)
                    # Find this skill in the role catalog to get specific skills
                    for role_entry in data.get("role_skill_catalog", []):
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

        # Return just the matches for compatibility
        return json.dumps(matches, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_external_candidates_by_skills",
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
