# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class get_team_training_log(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], team_id: str) -> str:
        training_logs = data.get("team_training_log", [])
        team_logs = [log for log in training_logs if log.get("team_id") == team_id]
        return json.dumps({"training_logs": team_logs}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "get_team_training_log",
                "description": "Get training logs for a team",
                "parameters": {
                    "type": "object",
                    "properties": {"team_id": {"type": "string"}},
                    "required": ["team_id"],
                },
            },
        }
