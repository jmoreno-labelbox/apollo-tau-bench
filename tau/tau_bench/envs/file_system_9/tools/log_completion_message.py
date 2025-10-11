# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LogCompletionMessage(Tool):
    """Logs a completion message and returns the generated msg_id."""
    @staticmethod
    def invoke(data: Dict[str, Any], message, task_id, user_id) -> str:
        completion_messages = list(data.get("completion_messages", {}).values())
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
        return json.dumps({"status": "success", "message": "Completion message logged.", "msg_id": msg_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "log_completion_message",
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
