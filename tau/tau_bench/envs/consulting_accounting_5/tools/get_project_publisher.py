# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetProjectPublisher(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        record = next((pr for pr in data["pipeline_opportunities"]
                       if pr["project_title"] == kwargs["name"]),
                      None)

        return json.dumps(record["publisher_id"])

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProjectPublisher",
                "description": "Get project publisher from project's name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                    },
                    "required": ["name"],
                },
            },
        }
