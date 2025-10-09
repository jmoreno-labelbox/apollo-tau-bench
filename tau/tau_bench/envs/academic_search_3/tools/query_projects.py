from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class QueryProjects(Tool):
    """Utility for querying projects using ID or name."""

    @staticmethod
    def invoke(data: dict[str, Any], project_id: str = None, project_name: str = None, funding_source_id: str = None) -> str:
        projects = data.get("projects", {}).values()
        results = []
        for proj in projects.values():
            match = True
            if project_id and project_id != proj.get("project_id"):
                match = False
            if project_name and project_name.lower() not in proj.get("project_name", "").lower():
                match = False
            if funding_source_id and funding_source_id != proj.get("funding_source_id"):
                match = False
            if match:
                results.append(proj)
        payload = results
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "QueryProjects",
                "description": "Queries research projects by ID, name, or funding source ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {
                            "type": "string",
                            "description": "The project's ID.",
                        },
                        "project_name": {
                            "type": "string",
                            "description": "The project's name.",
                        },
                        "funding_source_id": {
                            "type": "string",
                            "description": "The funding source ID to filter projects.",
                        },
                    },
                    "required": [],
                },
            },
        }
