# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateProject(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_name = kwargs.get("project_name")
        department = kwargs.get("department")
        status = kwargs.get("status", "active")
        priority = kwargs.get("priority", "low")
        required_hours_per_week = kwargs.get("required_hours_per_week")
        need_resources = kwargs.get("need_resources", "true")
        start_date = kwargs.get("start_date", "to be defined")
        end_date = kwargs.get("end_date", "to be defined")
        project_id = kwargs.get("project_id", f"project_{uuid.uuid4().hex[:8]}")

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
                            "type": "int",
                            "description": "Project's required allocation hours per week",
                        },
                        "department": {
                            "type": "string",
                            "description": "Project's department",
                        },
                        "needs_resources": {
                            "type": "bool",
                            "description": "Indicates if the project need more allocation",
                        },
                    },
                    "required": ["project_name", "department", "required_hours_per_week"],
                },
            },
        }
