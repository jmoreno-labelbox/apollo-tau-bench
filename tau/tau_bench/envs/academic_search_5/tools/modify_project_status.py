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

class ModifyProjectStatus(Tool):
    """Utility for modifying the status and/or end date of a research project."""

    @staticmethod
    def invoke(data: dict[str, Any], *, project_id: Any = None, new_status: Any = None, end_date: Any = None) -> str:
        project_id = project_id
        new_status = new_status
        end_date = end_date  # Access the newly added optional parameter

        if not project_id or not (new_status or end_date):
            payload = {"error": "project_id and either new_status or end_date are required."}
            out = json.dumps(payload)
            return out

        projects = data.get("projects", {}).values()
        for project in projects.values():
            if project.get("project_id") == project_id:
                if new_status:
                    project["status"] = new_status
                if end_date:  # Update if an end_date is supplied
                    project["end_date"] = end_date
                updated_fields = {}
                if new_status:
                    updated_fields["new_status"] = new_status
                if end_date:
                    updated_fields["end_date"] = end_date
                payload = {
                    "success": True,
                    "project_id": project_id,
                    "updated_fields": updated_fields,
                }
                out = json.dumps(payload)
                return out
        payload = {"error": "Project not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ModifyProjectStatus",
                "description": "Updates the status and/or end date of a research project (e.g., 'active', 'completed', 'on_hold').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {
                            "type": "string",
                            "description": "The ID of the project to update.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new status for the project.",
                        },
                        #Incorporate end_date into the schema
                        "end_date": {
                            "type": "string",
                            "description": "The new end date for the project (e.g., 'YYYY-MM-DD').",
                        },
                    },
                    "required": ["project_id"],
                },
            },
        }
