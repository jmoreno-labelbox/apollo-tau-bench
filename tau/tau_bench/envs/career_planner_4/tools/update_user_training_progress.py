# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class update_user_training_progress(Tool):
    @staticmethod
    def invoke(data, user_id: str, training_session_id: str, progress: int) -> str:
        record = {
            "user_id": user_id,
            "training_session_id": training_session_id,
            "progress": progress,
        }
        data.setdefault("user_training_progress", []).append(record)
        return json.dumps(
            {
                "success": f"Training progress for {user_id} on session {training_session_id} set to {progress}"
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "update_user_training_progress",
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
