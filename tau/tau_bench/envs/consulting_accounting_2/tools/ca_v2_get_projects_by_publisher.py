from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CaV2GetProjectsByPublisher(Tool):
    """Retrieve all projects associated with a specific publisher."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        active_only: bool = True,
        publisher_id: str = None
    ) -> str:
        if not publisher_id:
            return _error("publisher_id is required.")

        projects = data.get("projects", [])
        publisher_projects = _find_all(projects, "publisher_id", publisher_id)

        if active_only:
            publisher_projects = [
                p for p in publisher_projects if p.get("is_active", True)
            ]
        payload = publisher_projects
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2GetProjectsByPublisher",
                "description": "Get all projects for a specific publisher, optionally filtering to active projects only.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "publisher_id": {"type": "string"},
                        "active_only": {"type": "boolean", "default": True},
                    },
                    "required": ["publisher_id"],
                },
            },
        }
