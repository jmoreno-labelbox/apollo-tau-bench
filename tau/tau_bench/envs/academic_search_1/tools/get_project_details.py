# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetProjectDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], project_id) -> str:
        if not project_id:
            return json.dumps({"error": "project_id is required."})

        projects = list(data.get('projects', {}).values())
        for p in projects:
            if p.get('project_id') == project_id:
                return json.dumps(p, indent=2)

        return json.dumps({"error": f"Project with ID '{project_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_project_details", "description": "Retrieves the full details for a single project by its unique ID.", "parameters": {"type": "object", "properties": {"project_id": {"type": "string", "description": "The unique ID of the project to retrieve."}}, "required": ["project_id"]}}}
