from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CaV2FindProjectByIsbn(Tool):
    """Locate project using ISBN."""

    @staticmethod
    def invoke(data: dict[str, Any], isbn: str = None) -> str:
        if not isbn:
            return _error("isbn is required.")
        projects = data.get("projects", {}).values()
        project = _find_one(list(projects.values()), "isbn", isbn)
        return (
            json.dumps(project)
            if project
            else _error(f"Project with ISBN '{isbn}' not found.")
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2FindProjectByIsbn",
                "description": "Find a project by its ISBN code.",
                "parameters": {
                    "type": "object",
                    "properties": {"isbn": {"type": "string"}},
                    "required": ["isbn"],
                },
            },
        }
