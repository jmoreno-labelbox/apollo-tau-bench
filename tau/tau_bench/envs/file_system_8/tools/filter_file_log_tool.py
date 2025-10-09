from tau_bench.envs.tool import Tool
import datetime
import hashlib
import json
from typing import Any

class FilterFileLogTool(Tool):
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FilterFileLog",
                "description": "Filters a generated file log based on max size and a list of users.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "log_name": {
                            "type": "string",
                            "description": "Defaults to 'file_check_log.json'.",
                        },
                        "max_size": {"type": "integer"},
                        "users": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["max_size", "users"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], log_name: str = "file_check_log.json", max_size: int = None, users: list = None) -> str:
        if log_name not in data:
            payload = {"error": f"Log '{log_name}' not found."}
            out = json.dumps(payload)
            return out

        original_count = len(data[log_name]["data"])
        data[log_name]["data"] = [
            f
            for f in data[log_name]["data"]
            if f["size"] < max_size and f["user"] in users
        ]
        payload = {
                "status": "success",
                "original_count": original_count,
                "filtered_count": len(data[log_name]["data"]),
            }
        out = json.dumps(payload)
        return out
