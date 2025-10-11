# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetSprintDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], sprint_id) -> str:

        if not sprint_id:
            return json.dumps({"error": "sprint_id is required"})

        sprints = list(data.get("sprints", {}).values())

        for sprint in sprints:
            if sprint.get("sprint_id") == sprint_id:
                return json.dumps(sprint, indent=2)

        return json.dumps({"error": f"Sprint '{sprint_id}' not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_sprint_details",
                "description": "Get details of a specific sprint",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sprint_id": {"type": "string", "description": "The sprint ID"}
                    },
                    "required": ["sprint_id"],
                },
            },
        }
