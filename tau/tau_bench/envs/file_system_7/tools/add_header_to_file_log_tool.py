from tau_bench.envs.tool import Tool
import datetime
import hashlib
import json
from typing import Any

class AddHeaderToFileLogTool(Tool):
    """Adds a task_id as a header in the file check log."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddHeaderToFileLog",
                "description": "Adds a top-level 'task_id' key to the specified log file object.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "log_name": {
                            "type": "string",
                            "description": "The name of the log to modify.",
                        },
                        "task_id": {
                            "type": "string",
                            "description": "The task ID to add as a header.",
                        },
                    },
                    "required": ["log_name", "task_id"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], log_name: str, task_id: str) -> str:
        if log_name not in data:
            payload = {"error": f"Log '{log_name}' not found."}
            out = json.dumps(payload)
            return out
        # Encapsulate existing data within a 'data' key and include 'task_id' at the top level.
        log_data = data[log_name]["data"]
        data[log_name] = {"task_id": task_id, "data": log_data}
        payload = {"status": "success", "log_name": log_name, "header_added": "task_id"}
        out = json.dumps(payload)
        return out
