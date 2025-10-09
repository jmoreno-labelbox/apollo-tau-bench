from tau_bench.envs.tool import Tool
import json
import uuid
from collections import Counter
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetProjectDetails(Tool):
    """Looks for projects using project_name, linked_article_id, or project_id."""

    @staticmethod
    def invoke(
        data: dict[str, Any], 
        project_name: str = None, 
        linked_article_id: str = None, 
        project_id: str = None
    ) -> str:
        if not any([project_name, linked_article_id, project_id]):
            payload = data.get("projects", {}).values()
            out = json.dumps(payload, indent=2)
            return out
        projects = data.get("projects", {}).values()
        results = [
            p
            for p in projects.values() if (
                not project_name
                or project_name.lower() in p.get("project_name", "").lower()
            )
            and (
                not linked_article_id
                or linked_article_id in p.get("linked_articles", [])
            )
            and (not project_id or p.get("project_id") == project_id)
        ]
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProjectDetails",
                "description": "Searches for projects by project_name, linked_article_id, or project_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_name": {"type": "string"},
                        "linked_article_id": {"type": "string"},
                        "project_id": {"type": "string"},
                    },
                },
            },
        }
