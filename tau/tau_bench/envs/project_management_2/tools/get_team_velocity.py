# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetTeamVelocity(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        team_id = kwargs.get("team_id")
        last_n_sprints = kwargs.get("last_n_sprints", 3)

        if not team_id:
            return json.dumps({"error": "team_id is required"})

        sprints = list(data.get("sprints", {}).values())

        team_sprints = [
            s
            for s in sprints
            if s.get("team_id") == team_id and s.get("status") == "completed"
        ]

        team_sprints.sort(key=lambda x: x.get("end_date", ""), reverse=True)

        recent_sprints = team_sprints[:last_n_sprints]

        if not recent_sprints:
            return json.dumps(
                {
                    "team_id": team_id,
                    "average_velocity": 0,
                    "sprints_analyzed": 0,
                    "message": "No completed sprints found for this team",
                }
            )

        velocities = [s.get("velocity", 0) for s in recent_sprints]
        average_velocity = sum(velocities) / len(velocities) if velocities else 0

        return json.dumps(
            {
                "team_id": team_id,
                "average_velocity": round(average_velocity, 1),
                "sprints_analyzed": len(recent_sprints),
                "individual_velocities": velocities,
                "trend": "improving"
                if len(velocities) > 1 and velocities[0] > velocities[-1]
                else "stable",
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_team_velocity",
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
