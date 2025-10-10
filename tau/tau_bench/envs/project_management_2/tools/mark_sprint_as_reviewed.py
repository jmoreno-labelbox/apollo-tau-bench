# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class MarkSprintAsReviewed(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], sprint_id) -> str:

        if not sprint_id:
            return json.dumps(
                {"error": "sprint_id is a required parameter"}
            )

        sprints = list(data.get("sprints", {}).values())

        for sprint in sprints:
            if sprint.get("sprint_id") == sprint_id:
                sprint["reviewed"] = "True"
                return json.dumps({"success": True})

        return json.dumps({"error": f"It wasn't found any sprint with the if {sprint_id}"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "mark_sprint_as_reviewed",
                "description": "Mark sprint as reviewed",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sprint_id": {
                            "type": "string",
                            "description": "Id of the sprint",
                        },
                    },
                    "required": ["sprint_id",],
                },
            },
        }
