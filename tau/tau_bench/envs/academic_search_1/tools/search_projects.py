from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class SearchProjects(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], *, project_name: Any = None, funding_source_id: Any = None, chief_researcher_id: Any = None) -> str:
        """
        Looks for research projects.
        - Filters based on 'project_name', 'funding_source_id', and/or 'chief_researcher_id'.
        - If no parameters are supplied, it returns all projects.
        """
        projects = data.get("projects", [])

        if not project_name and not funding_source_id and not chief_researcher_id:
            payload = projects
            out = json.dumps(payload, indent=2)
            return out

        results = [
            p
            for p in projects
            if (
                not project_name
                or project_name.lower() in p.get("project_name", "").lower()
            )
            and (
                not funding_source_id or p.get("funding_source_id") == funding_source_id
            )
            and (
                not chief_researcher_id or p.get("chief_researcher_id") == chief_researcher_id
            )
        ]
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        """
        Delivers the function schema for the language model's use.
        """
        pass
        return {
            "type": "function",
            "function": {
                "name": "SearchProjects",
                "description": "Searches for research projects by name, funding source ID, or chief researcher ID. If no parameters are provided, returns all projects.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_name": {
                            "type": "string",
                            "description": "The name of the project to search for.",
                        },
                        "funding_source_id": {
                            "type": "string",
                            "description": "The ID of the funding source to filter projects.",
                        },
                        "chief_researcher_id": {
                            "type": "string",
                            "description": "The ID of the chief researcher to filter projects.",
                        },
                    },
                },
            },
        }
