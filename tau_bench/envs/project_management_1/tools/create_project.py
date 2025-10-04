from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class CreateProject(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        project_name: str,
        department: str,
        required_hours_per_week: int,
        status: str = "active",
        priority: str = "low",
        need_resources: str = "true",
        start_date: str = "to be defined",
        end_date: str = "to be defined",
        project_id: str = None
    ) -> str:
        if project_id is None:
            project_id = f"project_{uuid.uuid4().hex[:8]}"

        if not all([project_name, department, required_hours_per_week]):
            payload = {
                "error": "project_name, required_hours_per_week and department are required parameters"
            }
            out = json.dumps(payload)
            return out

        projects = data.get("projects", [])

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
        payload = {
            "success": True,
            "project_id": project_id,
            "name": project_name,
            "department": department,
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateProject",
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
                            "type": \"integer\",
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
                    "required": [
                        "project_name",
                        "department",
                        "required_hours_per_week",
                    ],
                },
            },
        }
