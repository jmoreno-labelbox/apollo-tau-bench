# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateProjectStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], new_end_date, new_status, project_id) -> str:

        if not project_id or not new_status:
            return json.dumps({"error": "project_id and new_status are required."})

        for project in list(data.get('projects', {}).values()):
            if project['project_id'] == project_id:
                project['status'] = new_status
                if new_end_date is not None:
                    project['end_date'] = new_end_date
                else:
                    project['end_date'] = None
                return json.dumps({"success": True, "project": project})
        return json.dumps({"error": f"Project with ID '{project_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_project_status",
                "description": "Updates the status of a project (e.g., 'active', 'completed') and can optionally update its end date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "The ID of the project to update."},
                        "new_status": {"type": "string", "description": "The new status to set for the project."},
                        "new_end_date": {"type": "string", "description": "Optional. The new end date for the project in YYYY-MM-DD format."}
                    },
                    "required": ["project_id", "new_status"]
                }
            }
        }
