# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddHeaderToFileLogTool(Tool):
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
                        "log_name": {"type": "string", "description": "Defaults to 'file_check_log.json'."},
                        "task_id": {"type": "string"},
                    },
                    "required": ["task_id"],
                },
            },
        }

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        log_name = kwargs.get("log_name", "file_check_log.json")
        task_id = kwargs["task_id"]
        if log_name not in data:
            return json.dumps({"error": f"Log '{log_name}' not found."})
        # Enclose the current data within a 'data' key and include 'task_id' at the root level.
        log_data = data[log_name]["data"]
        data[log_name] = {"task_id": task_id, "data": log_data}
        return json.dumps(
            {"status": "success", "log_name": log_name, "header_added": "task_id"}
        )
