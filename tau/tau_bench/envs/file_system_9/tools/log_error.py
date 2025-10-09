from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class LogError(Tool):
    """Records an error message and returns the generated msg_id."""

    @staticmethod
    def invoke(data: dict[str, Any], err_type: str = None, task_id: str = None, user_id: str = None, message: str = None, severity: str = None) -> str:
        error_messages = data.get("error_messages", [])
        max_id = 0
        if error_messages:
            for msg in error_messages:
                try:
                    current_id_num = int(msg.get("msg_id", "err_msg_000").split("_")[2])
                    if current_id_num > max_id:
                        max_id = current_id_num
                except (IndexError, ValueError):
                    continue
        new_id_num = max_id + 1
        msg_id = f"err_msg_{new_id_num:03d}"

        new_error = {
            "msg_id": msg_id,
            "err_type": err_type,
            "task_id": task_id,
            "user_id": user_id,
            "msg": message,
            "severity": severity,
        }
        data["error_messages"].append(new_error)
        payload = {"status": "success", "message": "Error message logged.", "msg_id": msg_id}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "logError",
                "description": "Logs an error message and returns the generated msg_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "err_type": {"type": "string"},
                        "task_id": {"type": "string"},
                        "user_id": {"type": "string"},
                        "message": {"type": "string"},
                        "severity": {"type": "string"},
                    },
                    "required": [
                        "err_type",
                        "task_id",
                        "user_id",
                        "message",
                        "severity",
                    ],
                },
            },
        }
