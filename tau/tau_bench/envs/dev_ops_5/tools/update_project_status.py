from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateProjectStatus(Tool):
    """Modifies the active status of a project."""

    def invoke(
        data: dict[str, Any],
        id: Any = None,
        is_active: bool = None,
        project_id: str = None
    ) -> str:
        projects = data.get("projects", {}).values()
        for p in projects.values():
            if p.get("id") == project_id:
                p["is_active"] = is_active
                payload = {
                    "status": "success",
                    "message": f"Project '{project_id}' active status set to {is_active}.",
                }
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
                "name": "updateProjectStatus",
                "description": "Updates the active status of a project.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "is_active": {"type": "boolean"},
                    },
                    "required": ["id", "is_active"],
                },
            },
        }
