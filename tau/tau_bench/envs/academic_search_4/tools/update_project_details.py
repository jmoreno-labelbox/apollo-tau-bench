# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateProjectDetails(Tool):
    """Updates the details of an existing research project."""
    @staticmethod
    def invoke(data: Dict[str, Any], project_id) -> str:
        if not project_id:
            return json.dumps({"error": "project_id is required."})

        project = next((p for p in list(data.get('projects', {}).values()) if p.get('project_id') == project_id), None)
        if not project:
            return json.dumps({"error": f"Project with ID '{project_id}' not found."})

        updatable_fields = ['project_name', 'status', 'linked_article_ids']
        for key, value in kwargs.items():
            if key in updatable_fields:
                project[key] = value

        return json.dumps({"success": True, "project": project})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_project_details", "description": "Updates details of an existing project, such as its name or linked articles.", "parameters": {"type": "object", "properties": {"project_id": {"type": "string", "description": "The ID of the project to update."}, "project_name": {"type": "string", "description": "The new name for the project."}, "status": {"type": "string", "description": "The new status for the project."}, "linked_article_ids": {"type": "array", "items": {"type": "string"}, "description": "A new list of linked article IDs."}}, "required": ["project_id"]}}}
