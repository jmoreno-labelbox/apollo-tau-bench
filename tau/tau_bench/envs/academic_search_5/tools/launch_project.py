# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LaunchProject(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], funding_source_id, lead_researcher_id, project_id_override, project_name) -> str:

        project_id = project_id_override if project_id_override else f"proj_{uuid.uuid4().hex[:4]}"

        new_project = {"project_id": project_id,"project_name": project_name,"lead_researcher_id": lead_researcher_id,"status": "proposed","start_date": datetime.now().strftime('%Y-%m-%d'),"end_date": None,"linked_articles": [], "funding_source_id": funding_source_id}
        data['projects'].append(new_project)
        return json.dumps({"success": True, "project": new_project})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "launch_project","description": "Creates a new research project.","parameters": {"type": "object","properties": {"project_name": {"type": "string","description": "The name of the new project."},"lead_researcher_id": {"type": "string","description": "The user ID of the lead researcher."},"funding_source_id": {"type": "string","description": "The ID of the project's funding source."},"project_id_override": {"type": "string", "description": "Optional. A specific ID to assign to the new project for predictable referencing."}},"required": ["project_name", "lead_researcher_id", "funding_source_id"]}}}
