from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any

class CaV2FindProjectByIsbn(Tool):
    """Locate project using ISBN."""

    @staticmethod
    def invoke(data: dict[str, Any], isbn: str = None) -> str:
        if not isbn:
            return _error("isbn is required.")
        projects = data.get("projects", [])
        project = _find_one(projects, "isbn", isbn)
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
