from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any, Dict
from datetime import timedelta

class GetProjectPublisher(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], name: str) -> str:
        record = next((pr for pr in data["pipeline_opportunities"]
                       if pr["project_title"] == name),
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
