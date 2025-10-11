# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ModifyProjectStatus(Tool):

    """Tool to update the status and/or end date of a research project."""
    @staticmethod
    def invoke(data: Dict[str, Any], end_date, new_status, project_id) -> str:

        if not project_id or not (new_status or end_date):
            return json.dumps({"error": "project_id and either new_status or end_date are required."})

        projects = list(data.get('projects', {}).values())
        for project in projects:
            if project.get('project_id') == project_id:
                if new_status:
                    project['status'] = new_status
                if end_date: # Update the end_date if it is specified.
                    project['end_date'] = end_date
                return json.dumps({"success": True, "project_id": project_id, "updated_fields": kwargs})
        return json.dumps({"error": "Project not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "modify_project_status",
                "description": "Updates the status and/or end date of a research project (e.g., 'active', 'completed', 'on_hold').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "The ID of the project to update."},
                        "new_status": {"type": "string", "description": "The new status for the project."},
                        # Incorporate end_date into the schema.
                        "end_date": {"type": "string", "description": "The new end date for the project (e.g., 'YYYY-MM-DD')."}
                    },
                    "required": ["project_id"]
                }
            }
        }
