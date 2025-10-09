from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class AssessTeamMentorshipCoverage(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], team_id: str) -> str:
        teams = data.get("teams", [])
        team = next((t for t in teams if t.get("team_id") == team_id), None)

        if not team:
            payload = {"error": "Team not found"}
            out = json.dumps(payload, indent=2)
            return out

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
        payload = {
                "team_id": team_id,
                "total_members": len(members),
                "members_with_mentors": sum(
                    1 for m in members_with_mentors if m["has_mentor"]
                ),
                "mentorship_coverage": mentorship_coverage,
                "member_status": members_with_mentors,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "assessTeamMentorshipCoverage",
                "description": "Assess mentorship coverage for a team",
                "parameters": {
                    "type": "object",
                    "properties": {"team_id": {"type": "string"}},
                    "required": ["team_id"],
                },
            },
        }
