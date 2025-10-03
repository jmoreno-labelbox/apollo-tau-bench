from tau_bench.envs.tool import Tool
import json
import re
import uuid
from collections import Counter
from datetime import datetime
from typing import Any

class UpdateProjectDetails(Tool):
    """Modifies the information of an existing research project."""

    @staticmethod
    def invoke(data: dict[str, Any], *, project_id: Any = None, project_name: str = None, status: str = None, linked_article_ids: list = None, lead_researcher_id: str = None) -> str:
        project_id = project_id
        if not project_id:
            payload = {"error": "project_id is required."}
            out = json.dumps(payload)
            return out

        project = next(
            (p for p in data.get("projects", []) if p.get("project_id") == project_id),
            None,
        )
        if not project:
            payload = {"error": f"Project with ID '{project_id}' not found."}
            out = json.dumps(payload)
            return out

        updatable_fields = ["project_name", "status", "linked_article_ids", "lead_researcher_id"]
        updates = {"project_name": project_name, "status": status, "linked_article_ids": linked_article_ids, "lead_researcher_id": lead_researcher_id}
        for key, value in updates.items():
            if key in updatable_fields and value is not None:
                project[key] = value
        payload = {"success": True, "project": project}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateProjectDetails",
                "description": "Updates details of an existing project, such as its name or linked articles.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {
                            "type": "string",
                            "description": "The ID of the project to update.",
                        },
                        "project_name": {
                            "type": "string",
                            "description": "The new name for the project.",
                        },
                        "status": {
                            "type": "string",
                            "description": "The new status for the project.",
                        },
                        "linked_article_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "A new list of linked article IDs.",
                        },
                        "lead_researcher_id": {
                            "type": "string",
                            "description": "The new lead researcher ID for the project.",
                        },
                    },
                    "required": ["project_id"],
                },
            },
        }
