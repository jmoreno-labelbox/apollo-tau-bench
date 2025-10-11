# Copyright Sierra

import uuid
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RegisterProject(Tool):
    """Creates a new research project."""
    @staticmethod
    def invoke(data: Dict[str, Any], lead_researcher_id, linked_article_id, project_id_override, project_name) -> str:
        project_name, lead_researcher_id, linked_article_id = project_name, lead_researcher_id, linked_article_id
        if not all([project_name, lead_researcher_id, linked_article_id]):
            return json.dumps({"error": "project_name, lead_researcher_id, and linked_article_id are required."})
        new_project = {
            "project_id": project_id_override if project_id_override else f"proj_{uuid.uuid4().hex[:4]}",
            "project_name": project_name,
            "lead_researcher_id": lead_researcher_id,
            "status": "active",
            "start_date": "2025-06-24",
            "end_date": None,
            "linked_articles": [linked_article_id],
            "funding_source_id": None
        }
        list(data.get('projects', {}).values()).append(new_project)
        return json.dumps({"success": True, "project": new_project}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "register_project", "description": "Creates a new research project.", "parameters": {"type": "object", "properties": {"project_name": {"type": "string"}, "lead_researcher_id": {"type": "string"}, "linked_article_id": {"type": "string"}, "project_id_override": {"type": "string"}}, "required": ["project_name", "lead_researcher_id", "linked_article_id"]}}}
