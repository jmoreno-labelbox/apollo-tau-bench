from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CreateRelease(Tool):
    """Generates a new release for a project."""

    @staticmethod
    def invoke(data: dict[str, Any], project_id: str = None, version: str = None, notes: str = None, created_by: str = None) -> str:
        releases = data.get("releases", {}).values()
        new_id_num = max([int(r["id"].split("_")[1]) for r in releases]) + 1
        new_id = f"release_{new_id_num:03d}"

        new_release = {
            "id": new_id,
            "project_id": project_id,
            "version": version,
            "notes": notes,
            "created_at": "2025-01-28T00:00:00Z",
            "created_by": created_by,
        }
        data["releases"][new_release["release_id"]] = new_release
        payload = new_release
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createRelease",
                "description": "Creates a new release for a project.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string"},
                        "version": {"type": "string"},
                        "notes": {"type": "string"},
                        "created_by": {"type": "string"},
                    },
                    "required": ["project_id", "version", "notes", "created_by"],
                },
            },
        }
