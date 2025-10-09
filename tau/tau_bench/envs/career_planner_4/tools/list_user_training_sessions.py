from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ListUserTrainingSessions(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str) -> str:
        training_logs = data.get("team_training_log", {}).values()
        user_sessions = [log for log in training_logs.values() if log.get("user_id") == user_id]
        payload = {"training_sessions": user_sessions}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "listUserTrainingSessions",
                "description": "List training sessions for a user",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }
