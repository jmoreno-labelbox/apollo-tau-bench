# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetProjectDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], project_id) -> str:
        if not project_id:
            return json.dumps({"error": "project_id is required"})

        projects = list(data.get("projects", {}).values())
        allocations = data.get("allocations", [])
        allocated_hours = sum(
            allocation["hours_per_week"] for allocation in allocations if allocation["project_id"] == project_id
        )
        for project in projects:
            if project.get("project_id") == project_id:
                data = project.copy()
                data["allocated_hours"] = allocated_hours
                return json.dumps(data, indent=2)

        return json.dumps({"error": f"Project with ID '{project_id}' not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_project_details",
                "description": "Get details of a specific project",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {
                            "type": "string",
                            "description": "The project ID",
                        }
                    },
                    "required": ["project_id"],
                },
            },
        }
