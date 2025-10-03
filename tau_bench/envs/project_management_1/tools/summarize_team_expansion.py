from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class SummarizeTeamExpansion(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], project_id: str, new_team_members: list = [], additional_hours: int = 0, existing_hours: int = 0) -> str:
        if not all([project_id, new_team_members, additional_hours is not None]):
            payload = {
                    "error": "project_id, new_team_members, and additional_hours are required"
                }
            out = json.dumps(
                payload)
            return out

        total_hours = existing_hours + additional_hours
        payload = {
                "project_id": project_id,
                "new_team_members": new_team_members,
                "additional_hours": additional_hours,
                "total_hours": total_hours,
                "expansion_summary": {
                    "members_added": len(new_team_members),
                    "hours_added": additional_hours,
                    "final_allocation": total_hours,
                    "status": "completed",
                },
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SummarizeTeamExpansion",
                "description": "Generate a summary of team expansion operations",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {
                            "type": "string",
                            "description": "The project ID that was expanded",
                        },
                        "new_team_members": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of employee IDs added to the team",
                        },
                        "additional_hours": {
                            "type": "number",
                            "description": "Total additional hours allocated",
                        },
                        "existing_hours": {
                            "type": "number",
                            "description": "Existing hours before expansion",
                        },
                    },
                    "required": ["project_id", "new_team_members", "additional_hours"],
                },
            },
        }
