from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class UpdateUserTrainingProgress(Tool):
    @staticmethod
    def invoke(data: dict, user_id: str, training_session_id: str, progress: int) -> str:
        record = {
            "user_id": user_id,
            "training_session_id": training_session_id,
            "progress": progress,
        }
        data.setdefault("user_training_progress", []).append(record)
        payload = {
            "success": f"Training progress for {user_id} on session {training_session_id} set to {progress}"
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "updateUserTrainingProgress",
                "description": "Update the training progress for a given user and training session.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "training_session_id": {"type": "string"},
                        "progress": {"type": "integer"},
                    },
                    "required": ["user_id", "training_session_id", "progress"],
                },
            },
        }
