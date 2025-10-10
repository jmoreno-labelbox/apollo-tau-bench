# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AssignFundingToProject(Tool):
    """Tool to assign a funding source to a project."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id = kwargs.get('project_id')
        funding_source_id = kwargs.get('funding_source_id')
        if not project_id or not funding_source_id:
            return json.dumps({"error": "project_id and funding_source_id are required."})

        projects = list(data.get('projects', {}).values())
        for project in projects:
            if project.get('project_id') == project_id:
                project['funding_source_id'] = funding_source_id
                return json.dumps({"success": True, "project_id": project_id, "funding_source_id": funding_source_id})
        return json.dumps({"error": "Project not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "assign_funding_to_project",
                "description": "Assigns a funding source to a research project.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "The ID of the project to be funded."},
                        "funding_source_id": {"type": "string", "description": "The ID of the funding source."}
                    },
                    "required": ["project_id", "funding_source_id"]
                }
            }
        }
