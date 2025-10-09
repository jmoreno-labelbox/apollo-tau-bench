from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class LogCompletionMessage(Tool):
    """Records a completion message and provides the generated msg_id."""

    @staticmethod
    def invoke(data: dict[str, Any], task_id: str = None, user_id: str = None, message: str = None) -> str:
        completion_messages = data.get("completion_messages", {}).values()
        max_id = 0
        if completion_messages:
            for msg in completion_messages:
                try:
                    current_id_num = int(msg.get("msg_id", "comp_000").split("_")[1])
                    if current_id_num > max_id:
                        max_id = current_id_num
                except (IndexError, ValueError):
                    continue
        new_id_num = max_id + 1
        msg_id = f"comp_{new_id_num:03d}"

        new_log = {
            "msg_id": msg_id,
            "task_id": task_id,
            "user_id": user_id,
            "msg": message,
        }
        data["completion_messages"].append(new_log)
        payload = {
                "status": "success",
                "message": "Completion message logged.",
                "msg_id": msg_id,
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LogCompletionMessage",
                "description": "Logs a completion message and returns the generated msg_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task_id": {"type": "string"},
                        "user_id": {"type": "string"},
                        "message": {"type": "string"},
                    },
                    "required": ["task_id", "user_id", "message"],
                },
            },
        }
