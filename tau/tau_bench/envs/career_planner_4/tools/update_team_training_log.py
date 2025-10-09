from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class UpdateTeamTrainingLog(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
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
        payload = {"success": f"Training log updated for {user_id}"}
        out = json.dumps(payload, indent=2)
        return out
        return out

    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "updateTeamTrainingLog",
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
