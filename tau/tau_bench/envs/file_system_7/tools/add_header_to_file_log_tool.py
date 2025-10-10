# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddHeaderToFileLogTool(Tool):
    """Appends a task_id as a header to the file check log."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_header_to_file_log",
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
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        log_name, task_id = kwargs["log_name"], kwargs["task_id"]
        if log_name not in data:
            return json.dumps({"error": f"Log '{log_name}' not found."})
        # Encapsulate the current data within a 'data' key and introduce 'task_id' at the root level.
        log_data = data[log_name]["data"]
        data[log_name] = {"task_id": task_id, "data": log_data}
        return json.dumps(
            {"status": "success", "log_name": log_name, "header_added": "task_id"}
        )
