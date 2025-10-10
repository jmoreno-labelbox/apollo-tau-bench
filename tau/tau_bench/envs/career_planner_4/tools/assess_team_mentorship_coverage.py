# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class assess_team_mentorship_coverage(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], team_id: str) -> str:
        teams = data.get("teams", [])
        team = next((t for t in teams if t.get("team_id") == team_id), None)

        if not team:
            return json.dumps({"error": "Team not found"}, indent=2)

        members = team.get("team_members", [])
        mentorship_relationships = data.get("user_mentorship_relationships", [])

        members_with_mentors = []
        for member in members:
            has_mentor = any(
                r.get("mentee_id") == member and r.get("status") == "Active"
                for r in mentorship_relationships
            )
            members_with_mentors.append({"user_id": member, "has_mentor": has_mentor})

        mentorship_coverage = (
            sum(1 for m in members_with_mentors if m["has_mentor"]) / len(members)
            if members
            else 0
        )

        return json.dumps(
            {
                "team_id": team_id,
                "total_members": len(members),
                "members_with_mentors": sum(
                    1 for m in members_with_mentors if m["has_mentor"]
                ),
                "mentorship_coverage": mentorship_coverage,
                "member_status": members_with_mentors,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "assess_team_mentorship_coverage",
                "description": "Assess mentorship coverage for a team",
                "parameters": {
                    "type": "object",
                    "properties": {"team_id": {"type": "string"}},
                    "required": ["team_id"],
                },
            },
        }
