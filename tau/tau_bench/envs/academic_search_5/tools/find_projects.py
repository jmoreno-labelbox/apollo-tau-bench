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

class FindProjects(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        project_id: Any = None,
        project_name: Any = None,
        lead_researcher_id: Any = None,
        status: Any = None,
        end_date_year: Any = None
    ) -> str:
        project_id = project_id
        if project_id:
            for project in data.get("projects", []):
                if project.get("project_id") == project_id:
                    payload = project
                    out = json.dumps(payload, indent=2)
                    return out
            payload = {"error": f"Project with ID '{project_id}' not found."}
            out = json.dumps(payload)
            return out

        project_name = project_name
        lead_researcher_id = lead_researcher_id
        status = status
        end_date_year = end_date_year  # Additional parameter

        # Incorporate the new parameter into the validation process
        if not any([project_name, lead_researcher_id, status, end_date_year]):
            payload = {
                "error": "At least one search parameter (project_name, lead_researcher_id, status, or end_date_year) is required for a general search."
            }
            out = json.dumps(payload)
            return out

        projects = data.get("projects", [])
        results = []
        for project in projects:
            name_match = (
                not project_name
                or project_name.lower() in project.get("project_name", "").lower()
            )
            lead_match = not lead_researcher_id or lead_researcher_id == project.get(
                "lead_researcher_id"
            )
            status_match = (
                not status or status.lower() == project.get("status", "").lower()
            )

            # Implement logic for year matching
            project_end_date = project.get("end_date")
            year_match = not end_date_year or (
                project_end_date and project_end_date.startswith(str(end_date_year))
            )

            # Include year_match in the concluding condition
            if name_match and lead_match and status_match and year_match:
                results.append(project)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindProjects",
                "description": "Searches for projects by various criteria OR retrieves a single project by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {
                            "type": "string",
                            "description": "The specific ID of the project to retrieve.",
                        },
                        "project_name": {
                            "type": "string",
                            "description": "The name of the project.",
                        },
                        "lead_researcher_id": {
                            "type": "string",
                            "description": "The user ID of the lead researcher.",
                        },
                        "status": {
                            "type": "string",
                            "description": "The current status of the project.",
                        },
                        #Introduce the new parameter into the schema
                        "end_date_year": {
                            "type": "integer",
                            "description": "The year the project ended, to filter by completion year.",
                        },
                    },
                },
            },
        }
