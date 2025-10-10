# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateProject(Tool):
    """Updates an existing project's status, collaborators, linked articles, or funding source."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id = kwargs.get('project_id')
        if not project_id: return json.dumps({"error": "project_id is required."})
        project = next((p for p in list(data.get('projects', {}).values()) if p.get('project_id') == project_id), None)
        if not project: return json.dumps({"error": "Project not found."})

        standard_updatable_fields = ['project_name', 'status', 'end_date', 'funding_source_id']
        for key, value in kwargs.items():
            if key in standard_updatable_fields:
                project[key] = value

        if 'linked_articles' in kwargs:
            project['linked_articles'] = kwargs['linked_articles']

        if 'add_collaborators' in kwargs:
            if 'collaborators' not in project:
                project['collaborators'] = []

            provided_collaborators = kwargs.get('add_collaborators', [])
            users = list(data.get('users', {}).values())

            valid_collaborator_ids = []
            for collab_item in provided_collaborators:
                # Check if the item is already a valid user_id
                if any(u['user_id'] == collab_item for u in users):
                    valid_collaborator_ids.append(collab_item)
                # Otherwise, try to find by name
                else:
                    found_user = next((u for u in users if u['name'] == collab_item), None)
                    if found_user:
                        valid_collaborator_ids.append(found_user['user_id'])

            existing_collaborators = set(project.get('collaborators', []))
            updated_collaborators = sorted(list(existing_collaborators.union(set(valid_collaborator_ids))))
            project['collaborators'] = updated_collaborators

        return json.dumps({"success": True, "project": project}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_project", "description": "Updates a project's details, such as status, collaborators, linked articles, or funding.", "parameters": {"type": "object", "properties": {"project_id": {"type": "string"}, "status": {"type": "string"}, "project_name": {"type": "string"}, "add_collaborators": {"type": "array", "items": {"type": "string"}}, "funding_source_id": {"type": "string"}, "linked_articles": {"type": "array", "items": {"type": "string"}}}, "required": ["project_id"]}}}
