# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class update_team_training_log(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        training_session_id: str,
        user_id: str,
        status: str,
        completion_date: str,
        skills_gained: list,
    ) -> str:
        log_entry = {
            "training_session_id": training_session_id,
            "user_id": user_id,
            "status": status,
            "completion_date": completion_date,
            "skills_gained": skills_gained,
        }
        data.setdefault("team_training_log", []).append(log_entry)
        return json.dumps({"success": f"Training log updated for {user_id}"}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "update_team_training_log",
                "description": "Update team training log",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "training_session_id": {"type": "string"},
                        "user_id": {"type": "string"},
                        "status": {"type": "string"},
                        "completion_date": {"type": "string"},
                        "skills_gained": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": [
                        "training_session_id",
                        "user_id",
                        "status",
                        "completion_date",
                        "skills_gained",
                    ],
                },
            },
        }
