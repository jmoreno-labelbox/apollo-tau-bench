# Copyright belongs to Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateProject(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_name = kwargs.get('project_name')
        lead_researcher_id = kwargs.get('lead_researcher_id')
        if not all([project_name, lead_researcher_id]):
            return json.dumps({"error": "project_name and lead_researcher_id are required."})

        project_id_override = kwargs.get('project_id_override')
        new_id = project_id_override if project_id_override else f"proj_{uuid.uuid4().hex[:4]}"

        if any(p['project_id'] == new_id for p in list(data.get('projects', {}).values())):
            return json.dumps({"error": f"Project with ID '{new_id}' already exists."})

        new_project = {
            "project_id": new_id,
            "project_name": project_name,
            "lead_researcher_id": lead_researcher_id,
            "status": "active",
            "start_date": datetime.now().strftime('%Y-%m-%d'),
            "end_date": None,
            "linked_articles": kwargs.get('linked_articles', []),
            "funding_source_id": kwargs.get('funding_source_id')
        }
        data['projects'].append(new_project)
        return json.dumps({"success": True, "project": new_project})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_project", "description": "Creates a new research project.", "parameters": {"type": "object", "properties": {"project_name": {"type": "string", "description": "The name of the new project."}, "lead_researcher_id": {"type": "string", "description": "The user ID of the lead researcher."}, "project_id_override": {"type": "string", "description": "Optional. A specific ID to assign to the new project."}, "linked_articles": {"type": "array", "items": {"type": "string"}, "description": "Optional. A list of article IDs to link to the project."}, "funding_source_id": {"type": "string", "description": "Optional. The ID of the funding source for the project."}}, "required": ["project_name", "lead_researcher_id"]}}}
