from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetProjectByName(Tool):
    """Fetches a project using its precise name."""

    @staticmethod
    def invoke(data: dict[str, Any], name: str = None) -> str:
        project_name = name
        projects = data.get("projects", [])

        for project in projects:
            if project.get("name") == project_name:
                payload = project
                out = json.dumps(payload)
                return out
        payload = {"error": f"Project with name '{project_name}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProjectByName",
                "description": "Retrieves a project by its exact name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "The exact name of the project.",
                        }
                    },
                    "required": ["name"],
                },
            },
        }
