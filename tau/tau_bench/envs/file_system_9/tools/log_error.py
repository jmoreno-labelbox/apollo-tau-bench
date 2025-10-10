# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LogError(Tool):
    """Logs an error message and returns the generated msg_id."""
    @staticmethod
    def invoke(data: Dict[str, Any], err_type, message, severity, task_id, user_id) -> str:
        error_messages = list(data.get("error_messages", {}).values())
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
        return json.dumps({"status": "success", "message": "Error message logged.", "msg_id": msg_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "log_error",
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
                    "required": ["err_type", "task_id", "user_id", "message", "severity"],
                },
            },
        }
