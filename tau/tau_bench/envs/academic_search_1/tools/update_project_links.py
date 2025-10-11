# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateProjectLinks(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], add_article_id, project_id) -> str:
        if not all([project_id, add_article_id]):
            return json.dumps({"error": "project_id and add_article_id are required."})

        for project in list(data.get('projects', {}).values()):
            if project['project_id'] == project_id:
                if add_article_id not in project.get('linked_articles', []):
                    project['linked_articles'].append(add_article_id)
                return json.dumps({"success": True, "project": project})

        return json.dumps({"error": f"Project with ID '{project_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_project_links", "description": "Links an additional article to an existing project.", "parameters": {"type": "object", "properties": {"project_id": {"type": "string", "description": "The ID of the project to update."}, "add_article_id": {"type": "string", "description": "The ID of the article to link to the project."}}, "required": ["project_id", "add_article_id"]}}}
