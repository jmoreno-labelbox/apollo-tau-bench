# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetTeamTrainingLog(Tool):
    """Get team training log entries."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        tid = kwargs.get("team_id")
        logs = [
            log
            for log in data.get("team_training_logs", [])
            if log.get("team_id") == tid
        ]
        return json.dumps(logs, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_team_training_log",
                "description": "Get team training log.",
                "parameters": {
                    "type": "object",
                    "properties": {"team_id": {"type": "string"}},
                    "required": ["team_id"],
                },
            },
        }
