# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetProjectByName(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], project_name) -> str:
        """
        Returns project_id for a given project_title.
        """
        project_title = project_name
        project = next((p for p in data["projects"] if p["project_title"] == project_title), None)
        return json.dumps(project["project_id"] if project else None)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProjectByName",
                "description": "Retrieve project_id for a given project name/title.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_name": {"type": "string", "description": "Exact project title to look up"}
                    },
                    "required": ["project_name"],
                },
            },
        }
