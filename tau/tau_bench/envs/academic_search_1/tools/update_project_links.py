from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class UpdateProjectLinks(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], project_id: Any = None, add_article_id: Any = None) -> str:
        project_id = project_id
        add_article_id = add_article_id
        if not all([project_id, add_article_id]):
            payload = {"error": "project_id and add_article_id are required."}
            out = json.dumps(payload)
            return out

        for project in data.get("projects", []):
            if project["study_id"] == project_id:
                if add_article_id not in project.get("connected_papers", []):
                    project["connected_papers"].append(add_article_id)
                payload = {"success": True, "project": project}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Project with ID '{project_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateProjectLinks",
                "description": "Links an additional article to an existing project.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {
                            "type": "string",
                            "description": "The ID of the project to update.",
                        },
                        "add_article_id": {
                            "type": "string",
                            "description": "The ID of the article to link to the project.",
                        },
                    },
                    "required": ["project_id", "add_article_id"],
                },
            },
        }
