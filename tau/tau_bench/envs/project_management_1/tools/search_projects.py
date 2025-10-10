# Copyright Sierra Technologies

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchProjects(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], name, needs_resources) -> str:

        projects = list(data.get("projects", {}).values())
        results = []

        for project in projects:
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

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_projects",
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
