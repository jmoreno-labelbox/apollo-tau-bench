# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class find_project_by_name(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], name: str) -> str:
        projects = list(data.get("projects", {}).values())
        for project in projects:
            if project.get("name") == name:
                return json.dumps(project, indent=2)
        return json.dumps({"error": f"Project with name '{name}' not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return { "type": "function", "function": { "name": "find_project_by_name", "description": "Finds a project by its exact name.", "parameters": { "type": "object", "properties": { "name": { "type": "string" } }, "required": ["name"] } } }
