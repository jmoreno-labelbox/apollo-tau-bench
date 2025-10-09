from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetProjectDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], *, project_id: Any = None) -> str:
        project_id = project_id
        if not project_id:
            payload = {"error": "project_id is required."}
            out = json.dumps(payload)
            return out

        projects = data.get("projects", {}).values()
        for p in projects.values():
            if p.get("study_id") == project_id:
                payload = p
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Project with ID '{project_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProjectDetails",
                "description": "Retrieves the full details for a single project by its unique ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {
                            "type": "string",
                            "description": "The unique ID of the project to retrieve.",
                        }
                    },
                    "required": ["project_id"],
                },
            },
        }
