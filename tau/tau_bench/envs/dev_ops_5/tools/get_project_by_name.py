# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetProjectByName(Tool):
    """Retrieves a project by its exact name."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_name = kwargs.get("name")
        projects = list(data.get("projects", {}).values())
        
        for project in projects:
            if project.get("name") == project_name:
                return json.dumps(project)
        
        return json.dumps({"error": f"Project with name '{project_name}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_project_by_name",
                "description": "Retrieves a project by its exact name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "The exact name of the project.",
                        }
                    },
                    "required": ["name"],
                },
            },
        }
