from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class GetTeamVelocity(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], team_id: str, last_n_sprints: int = 3) -> str:
        if not team_id:
            payload = {"error": "team_id is required"}
            out = json.dumps(payload)
            return out

        sprints = data.get("sprints", [])

        team_sprints = [
            s
            for s in sprints
            if s.get("team_id") == team_id and s.get("status") == "completed"
        ]

        team_sprints.sort(key=lambda x: x.get("end_date", ""), reverse=True)

        recent_sprints = team_sprints[:last_n_sprints]

        if not recent_sprints:
            payload = {
                    "team_id": team_id,
                    "average_velocity": 0,
                    "sprints_analyzed": 0,
                    "message": "No completed sprints found for this team",
                }
            out = json.dumps(
                payload)
            return out

        velocities = [s.get("velocity", 0) for s in recent_sprints]
        average_velocity = sum(velocities) / len(velocities) if velocities else 0
        payload = {
                "team_id": team_id,
                "average_velocity": round(average_velocity, 1),
                "sprints_analyzed": len(recent_sprints),
                "individual_velocities": velocities,
                "trend": (
                    "improving"
                    if len(velocities) > 1 and velocities[0] > velocities[-1]
                    else "stable"
                ),
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTeamVelocity",
                "description": "Calculate team velocity based on completed sprints",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {"type": "string", "description": "The team ID"},
                        "last_n_sprints": {
                            "type": "integer",
                            "description": "Number of recent sprints to analyze (default: 3)",
                        },
                    },
                    "required": ["team_id"],
                },
            },
        }
