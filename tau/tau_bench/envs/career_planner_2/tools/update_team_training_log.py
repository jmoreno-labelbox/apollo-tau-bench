# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateTeamTrainingLog(Tool):
    """Add entry to team training log."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        tid = kwargs.get("team_id")
        entry = kwargs.get("entry")
        logs = data.setdefault("team_training_logs", [])
        logs.append(
            {
                "team_id": tid,
                "entry": entry,
                "date": datetime.utcnow().date().isoformat(),
            }
        )
        return json.dumps({"success": f"Log entry added for {tid}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_team_training_log",
                "description": "Add training log entry.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {"type": "string"},
                        "entry": {"type": "string"},
                    },
                    "required": ["team_id", "entry"],
                },
            },
        }
