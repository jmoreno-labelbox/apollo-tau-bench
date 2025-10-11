# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateProject(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], department, project_name, required_hours_per_week, end_date = "to be defined", need_resources = "true", priority = "low", project_id = f"project_{uuid.uuid4().hex[:8]}", start_date = "to be defined", status = "active") -> str:

        if not all([project_name, department, required_hours_per_week]):
            return json.dumps({"error": "project_name, required_hours_per_week and department are required parameters"})

        projects = list(data.get("projects", {}).values())

        new_project = {
            "project_id": project_id,
            "project_name": project_name,
            "department": department,
            "status": status,
            "priority": priority,
            "required_hours_per_week": required_hours_per_week,
            "need_resources": need_resources,
            "start_date": start_date,
            "end_date": end_date,
        }

        projects.append(new_project)

        return json.dumps(
            {
                "success": True,
                "project_id": project_id,
                "name": project_name,
                "department": department,
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_project",
                "description": "Create a new project",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string", "description": "Project name"},
                        "project_id": {
                            "type": "string",
                            "description": "ID for the project",
                        },
                        "priority": {
                            "type": "str",
                            "description": "Project's priority",
                        },
                        "status": {
                            "type": "string",
                            "description": "Project's priority",
                        },
                        "start_date": {
                            "type": "string",
                            "description": "Project's start date",
                        },
                        "end_date": {
                            "type": "string",
                            "description": "Project's end date",
                        },
                        "required_hours_per_week": {
                            "type": "integer",
                            "description": "Project's required allocation hours per week",
                        },
                        "department": {
                            "type": "string",
                            "description": "Project's department",
                        },
                        "needs_resources": {
                            "type": "boolean",
                            "description": "Indicates if the project need more allocation",
                        },
                    },
                    "required": ["project_name", "department", "required_hours_per_week"],
                },
            },
        }
