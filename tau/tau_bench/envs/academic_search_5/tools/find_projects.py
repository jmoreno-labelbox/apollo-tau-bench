# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindProjects(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], end_date_year, lead_researcher_id, project_id, project_name, status) -> str:
        if project_id:
            for project in list(data.get('projects', {}).values()):
                if project.get('project_id') == project_id:
                    return json.dumps(project, indent=2)
            return json.dumps({"error": f"Project with ID '{project_id}' not found."})

        # Incorporate an additional parameter into the validation process.
        if not any([project_name, lead_researcher_id, status, end_date_year]):
            return json.dumps({"error": "At least one search parameter (project_name, lead_researcher_id, status, or end_date_year) is required for a general search."})

        projects = list(data.get('projects', {}).values())
        results = []
        for project in projects:
            name_match = not project_name or project_name.lower() in project.get('project_name', '').lower()
            lead_match = not lead_researcher_id or lead_researcher_id == project.get('lead_researcher_id')
            status_match = not status or status.lower() == project.get('status', '').lower()

            # Implement year comparison functionality.
            project_end_date = project.get('end_date')
            year_match = (not end_date_year or
                          (project_end_date and project_end_date.startswith(str(end_date_year))))

            # Incorporate year_match into the last condition.
            if name_match and lead_match and status_match and year_match:
                results.append(project)

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_projects",
                "description": "Searches for projects by various criteria OR retrieves a single project by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "The specific ID of the project to retrieve."},
                        "project_name": {"type": "string", "description": "The name of the project."},
                        "lead_researcher_id": {"type": "string", "description": "The user ID of the lead researcher."},
                        "status": {"type": "string", "description": "The current status of the project."},
                        # Incorporate an additional parameter into the schema.
                        "end_date_year": {"type": "integer", "description": "The year the project ended, to filter by completion year."}
                    }
                }
            }
        }
