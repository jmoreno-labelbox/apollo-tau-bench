from tau_bench.envs.tool import Tool
import json
import uuid
from collections import Counter
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class RegisterProject(Tool):
    """Establishes a new research project."""

    @staticmethod
    def invoke(data: dict[str, Any], project_name: str = None, lead_researcher_id: Any = None, linked_article_id: Any = None, project_id_override: Any = None) -> str:
        if not all([project_name, lead_researcher_id, linked_article_id]):
            payload = {
                    "error": "project_name, lead_researcher_id, and linked_article_id are required."
                }
            out = json.dumps(
                payload)
            return out
        new_project = {
            "project_id": (
                project_id_override
                if project_id_override
                else f"proj_{uuid.uuid4().hex[:4]}"
            ),
            "project_name": project_name,
            "lead_researcher_id": lead_researcher_id,
            "status": "active",
            "start_date": "2025-06-24",
            "end_date": None,
            "linked_articles": [linked_article_id],
            "funding_source_id": None,
        }
        data.get("projects", []).append(new_project)
        payload = {"success": True, "project": new_project}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RegisterProject",
                "description": "Creates a new research project.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_name": {"type": "string"},
                        "lead_researcher_id": {"type": "string"},
                        "linked_article_id": {"type": "string"},
                        "project_id_override": {"type": "string"},
                    },
                    "required": [
                        "project_name",
                        "lead_researcher_id",
                        "linked_article_id",
                    ],
                },
            },
        }
