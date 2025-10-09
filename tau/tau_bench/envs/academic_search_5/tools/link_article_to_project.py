from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class LinkArticleToProject(Tool):
    """Utility for associating an article with a research project."""

    @staticmethod
    def invoke(data: dict[str, Any], project_id: Any = None, article_id: Any = None) -> str:
        project_id = project_id
        article_id = article_id
        if not project_id or not article_id:
            payload = {"error": "project_id and article_id are required."}
            out = json.dumps(payload)
            return out

        projects = data.get("projects", [])
        for project in projects:
            if project.get("project_id") == project_id:
                if "linked_articles" not in project:
                    project["linked_articles"] = []
                if article_id not in project["linked_articles"]:
                    project["linked_articles"].append(article_id)
                    payload = {
                            "success": True,
                            "project_id": project_id,
                            "article_id": article_id,
                        }
                    out = json.dumps(
                        payload)
                    return out
                else:
                    payload = {"error": "Article already linked to this project."}
                    out = json.dumps(
                        payload)
                    return out
        payload = {"error": "Project not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LinkArticleToProject",
                "description": "Links an existing article to a research project.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {
                            "type": "string",
                            "description": "The ID of the project.",
                        },
                        "article_id": {
                            "type": "string",
                            "description": "The ID of the article to link.",
                        },
                    },
                    "required": ["project_id", "article_id"],
                },
            },
        }
