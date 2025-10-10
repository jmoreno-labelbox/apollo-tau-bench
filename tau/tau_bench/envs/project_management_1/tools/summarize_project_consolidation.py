# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SummarizeProjectConsolidation(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], consolidated_to, team_size, total_hours, consolidated_projects = []) -> str:

        if not all([consolidated_to, total_hours is not None, team_size is not None]):
            return json.dumps(
                {"error": "consolidated_to, total_hours, and team_size are required"}
            )

        return json.dumps(
            {
                "consolidated_to": consolidated_to,
                "total_hours": total_hours,
                "team_size": team_size,
                "consolidation_summary": {
                    "target_project": consolidated_to,
                    "final_team_size": team_size,
                    "total_allocated_hours": total_hours,
                    "consolidated_projects": consolidated_projects,
                    "status": "completed",
                },
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "summarize_project_consolidation",
                "description": "Generate a summary of project consolidation operations",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "consolidated_to": {
                            "type": "string",
                            "description": "The target project ID where teams were consolidated",
                        },
                        "total_hours": {
                            "type": "number",
                            "description": "Total hours allocated to the consolidated project",
                        },
                        "team_size": {
                            "type": "number",
                            "description": "Final team size after consolidation",
                        },
                        "consolidated_projects": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of project IDs that were consolidated",
                        },
                    },
                    "required": ["consolidated_to", "total_hours", "team_size"],
                },
            },
        }
