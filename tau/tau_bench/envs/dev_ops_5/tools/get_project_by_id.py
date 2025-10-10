# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetProjectById(Tool):
    """Retrieves a project by its ID."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id = kwargs.get("id")
        projects = list(data.get("projects", {}).values())
        for p in projects:
            if p.get("id") == project_id:
                return json.dumps(p)
        return json.dumps({"error": f"Project with ID '{project_id}' not found."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_project_by_id",
                "description": "Retrieves a project by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"id": {"type": "string"}},
                    "required": ["id"],
                },
            },
        }
