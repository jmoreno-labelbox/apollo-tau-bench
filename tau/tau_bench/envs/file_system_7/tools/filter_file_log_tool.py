# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FilterFileLogTool(Tool):
    """Filters a file log based on size and user, simulating jq."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "filter_file_log",
                "description": "Filters a generated file log based on max size and a list of users.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "log_name": {
                            "type": "string",
                            "description": "The name of the log to filter in the database.",
                        },
                        "max_size": {
                            "type": "integer",
                            "description": "The maximum file size to include.",
                        },
                        "users": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of users to include.",
                        },
                    },
                    "required": ["log_name", "max_size", "users"],
                },
            },
        }

    @staticmethod
    def invoke(data: Dict[str, Any], log_name, max_size, users) -> str:
        log_name, max_size, users = (
            log_name,
            max_size,
            users,
        )
        if log_name not in data:
            return json.dumps({"error": f"Log '{log_name}' not found."})

        original_count = len(data[log_name]["data"])
        data[log_name]["data"] = [
            f
            for f in data[log_name]["data"]
            if f["size"] < max_size and f["user"] in users
        ]
        return json.dumps(
            {
                "status": "success",
                "original_count": original_count,
                "filtered_count": len(data[log_name]["data"]),
            }
        )
