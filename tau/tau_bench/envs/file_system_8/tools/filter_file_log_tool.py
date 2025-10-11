# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FilterFileLogTool(Tool):
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
                        "log_name": {"type": "string", "description": "Defaults to 'file_check_log.json'."},
                        "max_size": {"type": "integer"},
                        "users": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["max_size", "users"],
                },
            },
        }

    @staticmethod
    def invoke(data: Dict[str, Any], max_size, users, log_name = "file_check_log.json") -> str:
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
