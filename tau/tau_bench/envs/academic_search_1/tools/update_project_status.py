from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class UpdateProjectStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], project_id: Any = None, new_status: Any = None, new_end_date: Any = None) -> str:
        if not project_id or not new_status:
            payload = {"error": "project_id and new_status are required."}
            out = json.dumps(payload)
            return out

        for project in data.get("projects", []):
            if project["study_id"] == project_id:
                project["state"] = new_status
                if new_end_date is not None:
                    project["finish_date"] = new_end_date
                else:
                    project["finish_date"] = None
                payload = {"success": True, "project": project}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Project with ID '{project_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateProjectStatus",
                "description": "Updates the status of a project (e.g., 'active', 'completed') and can optionally update its end date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {
                            "type": "string",
                            "description": "The ID of the project to update.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new status to set for the project.",
                        },
                        "new_end_date": {
                            "type": "string",
                            "description": "Optional. The new end date for the project in YYYY-MM-DD format.",
                        },
                    },
                    "required": ["project_id", "new_status"],
                },
            },
        }
