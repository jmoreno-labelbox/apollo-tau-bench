# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SummarizeTeamExpansion(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id = kwargs.get("project_id")
        new_team_members = kwargs.get("new_team_members", [])
        additional_hours = kwargs.get("additional_hours", 0)
        existing_hours = kwargs.get("existing_hours", 0)

        if not all([project_id, new_team_members, additional_hours is not None]):
            return json.dumps(
                {
                    "error": "project_id, new_team_members, and additional_hours are required"
                }
            )

        total_hours = existing_hours + additional_hours

        return json.dumps(
            {
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
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "summarize_team_expansion",
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
