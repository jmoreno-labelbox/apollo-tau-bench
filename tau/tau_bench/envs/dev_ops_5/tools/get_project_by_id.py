from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetProjectById(Tool):
    """Fetches a project using its ID."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        id: Any = None,
        project_id: str = None
    ) -> str:
        projects = data.get("projects", {}).values()
        for p in projects.values():
            if p.get("id") == project_id:
                payload = p
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
                "name": "GetProjectById",
                "description": "Retrieves a project by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"id": {"type": "string"}},
                    "required": ["id"],
                },
            },
        }
