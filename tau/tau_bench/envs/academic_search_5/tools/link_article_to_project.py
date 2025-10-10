# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LinkArticleToProject(Tool):
    """Tool to link an article to a research project."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id = kwargs.get('project_id')
        article_id = kwargs.get('article_id')
        if not project_id or not article_id:
            return json.dumps({"error": "project_id and article_id are required."})

        projects = list(data.get('projects', {}).values())
        for project in projects:
            if project.get('project_id') == project_id:
                if 'linked_articles' not in project:
                    project['linked_articles'] = []
                if article_id not in project['linked_articles']:
                    project['linked_articles'].append(article_id)
                    return json.dumps({"success": True, "project_id": project_id, "article_id": article_id})
                else:
                    return json.dumps({"error": "Article already linked to this project."})
        return json.dumps({"error": "Project not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "link_article_to_project",
                "description": "Links an existing article to a research project.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "The ID of the project."},
                        "article_id": {"type": "string", "description": "The ID of the article to link."}
                    },
                    "required": ["project_id", "article_id"]
                }
            }
        }
