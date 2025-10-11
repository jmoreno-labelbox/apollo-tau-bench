from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class FindMentors(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], mentee_id: str, focus_areas: list[str]) -> str:
        pass
        mentors = data.get("user_mentorship", {}).values()

        # Embrace a broader concept of expertise that includes various roles and general knowledge.
        def get_mentor_expertise_set(mentor):
            pass
            expertise = set(mentor.get("expertise", []))
            roles = set(mentor.get("mentoring_roles", []))
            return expertise.union(roles)

        # Locate mentors whose skills and positions align with the key focus areas.
        # and who are evidently appropriate for the mentee.
        matches = []
        focus_set = set(focus_areas)
        for mentor in mentors:
            if mentor.get("availability") == "Full":
                continue

            # Check for compatibility.
            if mentee_id not in mentor.get("compatible_user_ids", []):
                continue

            # Check for overlapping skills.
            mentor_expertise = get_mentor_expertise_set(mentor)
            if focus_set.intersection(mentor_expertise):
                matches.append(
                    {
                        "mentor_id": mentor.get("mentor_id"),
                        "name": mentor.get("name"),
                        "expertise": list(mentor_expertise),
                    }
                )
        payload = {"mentors": matches}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "FindMentors",
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
