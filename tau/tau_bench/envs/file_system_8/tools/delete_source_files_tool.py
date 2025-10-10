# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DeleteSourceFilesTool(Tool):
    """Deletes the original source files after they have been successfully processed."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_source_files",
                "description": "Deletes the original source files after they have been successfully archived and transferred.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "file_paths": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of original file paths to delete.",
                        }
                    },
                    "required": ["file_paths"],
                },
            },
        }

    @staticmethod
    def invoke(data: Dict[str, Any], file_paths) -> str:
        paths_to_delete = set(file_paths)
        original_count = len(data.get("remote_files", []))
        data["remote_files"] = [
            f for f in data.get("remote_files", []) if f["path"] not in paths_to_delete
        ]
        return json.dumps(
            {
                "status": "success",
                "deleted_count": original_count - len(data["remote_files"]),
            }
        )
