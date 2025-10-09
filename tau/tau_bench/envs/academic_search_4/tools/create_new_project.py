from tau_bench.envs.tool import Tool
import json
import re
import uuid
from collections import Counter
from datetime import datetime
from typing import Any

class CreateNewProject(Tool):
    """Initiates a new research project."""

    @staticmethod
    def invoke(data: dict[str, Any], *, project_name: Any = None, lead_researcher_id: Any = None, project_id_override: Any = None, linked_article_ids: list = None) -> str:
        project_name = project_name
        lead_researcher_id = lead_researcher_id
        project_id_override = project_id_override

        if not all([project_name, lead_researcher_id]):
            payload = {"error": "project_name and lead_researcher_id are required."}
            out = json.dumps(
                payload)
            return out

        new_project_id = (
            project_id_override
            if project_id_override
            else f"proj_{uuid.uuid4().hex[:4]}"
        )

        new_project = {
            "project_id": new_project_id,
            "project_name": project_name,
            "lead_researcher_id": lead_researcher_id,
            "status": "active",
            "start_date": datetime.now().strftime("%Y-%m-%d"),
            "end_date": None,
            "linked_articles": linked_article_ids if linked_article_ids is not None else [],
        }
        if "projects" not in data:
            data["projects"] = []
        data["projects"][project_id] = new_project
        payload = {"success": True, "project": new_project}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateNewProject",
                "description": "Creates a new research project.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_name": {"type": "string"},
                        "lead_researcher_id": {"type": "string"},
                        "linked_article_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                        "project_id_override": {
                            "type": "string",
                            "description": "Optional. A specific ID to assign to the new project.",
                        },
                    },
                    "required": ["project_name", "lead_researcher_id"],
                },
            },
        }
