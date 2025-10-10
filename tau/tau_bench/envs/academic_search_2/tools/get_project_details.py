# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetProjectDetails(Tool):
    """Searches for projects by project_name, linked_article_id, or project_id."""
    @staticmethod
    def invoke(data: Dict[str, Any], linked_article_id, project_id, project_name) -> str:
        project_name, linked_article_id, project_id = project_name, linked_article_id, project_id
        if not any([project_name, linked_article_id, project_id]):
            return json.dumps(list(data.get('projects', {}).values()), indent=2)
        projects = list(data.get('projects', {}).values())
        results = [
            p for p in projects if
            (not project_name or project_name.lower() in p.get('project_name', '').lower()) and
            (not linked_article_id or linked_article_id in p.get('linked_articles', [])) and
            (not project_id or p.get('project_id') == project_id)
        ]
        return json.dumps(results, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_project_details", "description": "Searches for projects by project_name, linked_article_id, or project_id.", "parameters": {"type": "object", "properties": {"project_name": {"type": "string"}, "linked_article_id": {"type": "string"}, "project_id": {"type": "string"}}}}}
