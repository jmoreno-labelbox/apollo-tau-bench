# Copyright Sierra

import datetime
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class InitiateProject(Tool):
    """Tool to create a new research project."""
    @staticmethod
    def invoke(data: Dict[str, Any], lead_researcher_id, project_name) -> str:
        projects = list(data.get('projects', {}).values())
        new_project = {
            "project_id": f"proj_{len(projects) + 1:02d}",
            "project_name": project_name,
            "lead_researcher_id": lead_researcher_id,
            "status": "new",
            "start_date": datetime.now().strftime('%Y-%m-%d'),
            "end_date": None,
            "linked_articles": [],
            "funding_source_id": None,
            "logs": []
        }
        projects.append(new_project)
        return json.dumps(new_project, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "initiate_project", "description": "Creates a new research project.", "parameters": {"type": "object", "properties": {
            "project_name": {"type": "string", "description": "The name of the new project."},
            "lead_researcher_id": {"type": "string", "description": "The user ID of the lead researcher."}
        }, "required": ["project_name", "lead_researcher_id"]}}}
