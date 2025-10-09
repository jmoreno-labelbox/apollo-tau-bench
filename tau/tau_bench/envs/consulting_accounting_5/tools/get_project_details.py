from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any, Dict
from datetime import timedelta

class GetProjectDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], project_id: str) -> str:
        """
        Retrieves the full details for a given project_id.
        """
        project = next((p for p in data["projects"] if p["project_id"] == project_id), None)
        return json.dumps(project)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function", "function": {
                "name": "GetProjectDetails",
                "description": "Retrieve full details for a given project ID.",
                "parameters": {
                    "type": "object", "properties": {
                        "project_id": {"type": "string", "description": "The ID of the project to retrieve"}
                    },
                    "required": ["project_id"],
                },
            },
        }
