from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class InitiateProject(Tool):
    """Utility for establishing a new research project."""

    @staticmethod
    def invoke(data: dict[str, Any], project_name: str = None, lead_researcher_id: str = None, funding_source_id: str = None) -> str:
        projects = data.get("projects", {}).values()
        new_project = {
            "project_id": f"proj_{len(projects) + 1:02d}",
            "project_name": project_name,
            "lead_researcher_id": lead_researcher_id,
            "status": "new",
            "start_date": datetime.now().strftime("%Y-%m-%d"),
            "end_date": None,
            "linked_articles": [],
            "funding_source_id": funding_source_id,
            "logs": [],
        }
        data["projects"][project_id] = new_project
        payload = new_project
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "InitiateProject",
                "description": "Creates a new research project.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_name": {
                            "type": "string",
                            "description": "The name of the new project.",
                        },
                        "lead_researcher_id": {
                            "type": "string",
                            "description": "The user ID of the lead researcher.",
                        },
                        "funding_source_id": {
                            "type": "string",
                            "description": "The ID of the funding source for the project.",
                        },
                    },
                    "required": ["project_name", "lead_researcher_id"],
                },
            },
        }
