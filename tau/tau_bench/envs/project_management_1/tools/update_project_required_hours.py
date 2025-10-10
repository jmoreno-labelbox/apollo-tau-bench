# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateProjectRequiredHours(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], project_id, required_hours) -> str:

        if not all([project_id, required_hours]):
            return json.dumps({"error": "project_id and required hours are required"})

        projects = list(data.get("projects", {}).values())

        for project in projects:
            if project.get("project_id") == project_id:
                project["required_hours_per_week"] = required_hours
                return json.dumps({"success": True, "project": project})

        return json.dumps({"error": f"Project with ID '{project_id}' not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_project_required_hours",
                "description": "Update the hours per week required by a project",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {
                            "type": "string",
                            "description": "The project ID",
                        },
                        "required_hours": {
                            "type": "integer",
                            "description": "Hours per week required by the project",
                        },
                    },
                    "required": ["project_id", "required_hours"],
                },
            },
        }
