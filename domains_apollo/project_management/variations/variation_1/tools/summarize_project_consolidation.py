from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class SummarizeProjectConsolidation(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], consolidated_to: str = None, total_hours: int = None, team_size: int = None, consolidated_projects: list = None) -> str:
        if consolidated_projects is None:
            consolidated_projects = []

        if not all([consolidated_to, total_hours is not None, team_size is not None]):
            payload = {"error": "consolidated_to, total_hours, and team_size are required"}
            out = json.dumps(payload)
            return out

        payload = {
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
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SummarizeProjectConsolidation",
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
