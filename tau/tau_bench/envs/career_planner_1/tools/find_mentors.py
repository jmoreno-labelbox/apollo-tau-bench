# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindMentors(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], mentee_id: str, focus_areas: List[str]) -> str:
        mentors = data.get("user_mentorship", [])

        # Use a broader definition of expertise, including roles and general expertise
        def get_mentor_expertise_set(mentor):
            expertise = set(mentor.get("expertise", []))
            roles = set(mentor.get("mentoring_roles", []))
            return expertise.union(roles)

        # Find mentors whose expertise/roles overlap with the focus areas
        # and who are explicitly compatible with the mentee.
        matches = []
        focus_set = set(focus_areas)
        for mentor in mentors:
            if mentor.get("availability") == "Full":
                continue

            # Check for compatibility
            if mentee_id not in mentor.get("compatible_user_ids", []):
                continue

            # Check for expertise overlap
            mentor_expertise = get_mentor_expertise_set(mentor)
            if focus_set.intersection(mentor_expertise):
                matches.append(
                    {
                        "mentor_id": mentor.get("mentor_id"),
                        "name": mentor.get("name"),
                        "expertise": list(mentor_expertise),
                    }
                )

        return json.dumps({"mentors": matches}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "find_mentors",
                "description": "Finds suitable and available mentors for a mentee based on required focus areas and compatibility.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "mentee_id": {
                            "type": "string",
                            "description": "The user ID of the mentee seeking mentorship.",
                        },
                        "focus_areas": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "A list of skills or topics the mentorship should focus on.",
                        },
                    },
                    "required": ["mentee_id", "focus_areas"],
                },
            },
        }
