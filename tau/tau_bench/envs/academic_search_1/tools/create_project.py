from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class CreateProject(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], *, project_name: Any = None, lead_researcher_id: Any = None, project_id_override: Any = None, linked_articles: list = None, funding_source_id: Any = None) -> str:
        project_name = project_name
        lead_researcher_id = lead_researcher_id
        if not all([project_name, lead_researcher_id]):
            payload = {"error": "project_name and lead_researcher_id are required."}
            out = json.dumps(
                payload)
            return out

        project_id_override = project_id_override
        new_id = (
            project_id_override
            if project_id_override
            else f"proj_{uuid.uuid4().hex[:4]}"
        )

        if any(p["study_id"] == new_id for p in data.get("projects", [])):
            payload = {"error": f"Project with ID '{new_id}' already exists."}
            out = json.dumps(payload)
            return out

        new_project = {
            "study_id": new_id,
            "study_name": project_name,
            "chief_researcher_id": lead_researcher_id,
            "state": "active",
            "begin_date": datetime.now().strftime("%Y-%m-%d"),
            "finish_date": None,
            "connected_papers": linked_articles or [],
            "sponsor_id": funding_source_id,
        }
        data["projects"].append(new_project)
        payload = {"success": True, "project": new_project}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateProject",
                "description": "Creates a new research project.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_name": {
                            "type": "string",
                            "description": "The name of the new project.",
                        },
                        "lead_researcher_id": {
                            "type": "string",
                            "description": "The user ID of the lead researcher.",
                        },
                        "project_id_override": {
                            "type": "string",
                            "description": "Optional. A specific ID to assign to the new project.",
                        },
                        "linked_articles": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Optional. A list of article IDs to link to the project.",
                        },
                        "funding_source_id": {
                            "type": "string",
                            "description": "Optional. The ID of the funding source for the project.",
                        },
                    },
                    "required": ["project_name", "lead_researcher_id"],
                },
            },
        }
