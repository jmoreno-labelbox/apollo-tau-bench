# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchProjects(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Searches for research projects.
        - Filters by 'project_name' and/or 'funding_source_id'.
        - If no parameters are provided, returns all projects.
        """
        project_name = kwargs.get('project_name')
        funding_source_id = kwargs.get('funding_source_id')

        projects = list(data.get('projects', {}).values())

        if not project_name and not funding_source_id:
            return json.dumps(projects, indent=2)

        results = [
            p for p in projects
            if (not project_name or project_name.lower() in p.get('project_name', '').lower()) and
               (not funding_source_id or p.get('funding_source_id') == funding_source_id)
        ]
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """
        Returns the function schema to be used by the language model.
        """
        return {
            "type": "function",
            "function": {
                "name": "search_projects",
                "description": "Searches for research projects by name or funding source ID. If no parameters are provided, returns all projects.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_name": {"type": "string", "description": "The name of the project to search for."},
                        "funding_source_id": {"type": "string", "description": "The ID of the funding source to filter projects."}
                    }
                }
            }
        }
