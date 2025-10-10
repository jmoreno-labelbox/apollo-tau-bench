# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateNewProject(Tool):
    """Creates a new research project."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_name = kwargs.get('project_name')
        lead_researcher_id = kwargs.get('lead_researcher_id')
        project_id_override = kwargs.get('project_id_override')

        if not all([project_name, lead_researcher_id]):
            return json.dumps({"error": "project_name and lead_researcher_id are required."})

        new_project_id = project_id_override if project_id_override else f"proj_{uuid.uuid4().hex[:4]}"

        new_project = {
            "project_id": new_project_id,
            "project_name": project_name,
            "lead_researcher_id": lead_researcher_id,
            "status": "active",
            "start_date": datetime.now().strftime('%Y-%m-%d'),
            "end_date": None,
            "linked_articles": kwargs.get('linked_article_ids', [])
        }
        data['projects'].append(new_project)
        return json.dumps({"success": True, "project": new_project})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_new_project", "description": "Creates a new research project.", "parameters": {"type": "object", "properties": {"project_name": {"type": "string"}, "lead_researcher_id": {"type": "string"}, "linked_article_ids": {"type": "array", "items": {"type": "string"}}, "project_id_override": {"type": "string", "description": "Optional. A specific ID to assign to the new project."}}, "required": ["project_name", "lead_researcher_id"]}}}
