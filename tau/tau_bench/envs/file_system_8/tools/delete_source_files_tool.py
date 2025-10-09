from tau_bench.envs.tool import Tool
import datetime
import hashlib
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class DeleteSourceFilesTool(Tool):
    """Removes the original source files once they have been processed successfully."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "deleteSourceFiles",
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
    def invoke(data: dict[str, Any], file_paths: list[str]) -> str:
        paths_to_delete = set(file_paths)
        original_count = len(data.get("remote_files", {}))
        data["remote_files"] = [
            f for f in data.get("remote_files", {}).values() if f["path"] not in paths_to_delete
        ]
        payload = {
            "status": "success",
            "deleted_count": original_count - len(data["remote_files"]),
        }
        out = json.dumps(payload)
        return out
