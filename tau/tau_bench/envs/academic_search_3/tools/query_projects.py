# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class QueryProjects(Tool):
    """Tool to query projects by ID or name."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        projects = list(data.get('projects', {}).values())
        results = []
        for proj in projects:
            match = True
            if kwargs.get('project_id') and kwargs['project_id'] != proj.get('project_id'): match = False
            if kwargs.get('project_name') and kwargs['project_name'].lower() not in proj.get('project_name', '').lower(): match = False
            if match:
                results.append(proj)
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "query_projects", "description": "Queries research projects by ID or name.", "parameters": {"type": "object", "properties": {
            "project_id": {"type": "string", "description": "The project's ID."},
            "project_name": {"type": "string", "description": "The project's name."}
        }, "required": []}}}
