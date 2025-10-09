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

class SearchProjects(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], name: str = None, needs_resources: bool = None) -> str:
        projects = data.get("projects", {}).values()
        results = []

        for project in projects.values():
            match = True

            if name and name.lower() not in project.get("name", "").lower():
                match = False

            if needs_resources is not None:
                if needs_resources and not project.get("needs_resources", False):
                    match = False
                elif not needs_resources and project.get("needs_resources", True):
                    match = False

            if match:
                results.append(project)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchProjects",
                "description": "Search for projects by name or resource needs",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Project name to search for",
                        },
                        "needs_resources": {
                            "type": "boolean",
                            "description": "Filter by projects needing resources",
                        },
                    },
                },
            },
        }
