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
    def invoke(data: dict[str, Any], project_id: str = None) -> str:
        if not project_id:
            payload = {"error": "project_id is required"}
            out = json.dumps(payload)
            return out

        projects = data.get("projects", {}).values()
        allocations = data.get("allocations", {}).values()
        allocated_hours = sum(
            allocation["hours_per_week"]
            for allocation in allocations.values() if allocation["project_id"] == project_id
        )
        for project in projects.values()):
            if project.get("project_id") == project_id:
                data = project.copy()
                data["allocated_hours"] = allocated_hours
                payload = data
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Project with ID '{project_id}' not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProjectDetails",
                "description": "Get details of a specific project",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {
                            "type": "string",
                            "description": "The project ID",
                        }
                    },
                    "required": ["project_id"],
                },
            },
        }
