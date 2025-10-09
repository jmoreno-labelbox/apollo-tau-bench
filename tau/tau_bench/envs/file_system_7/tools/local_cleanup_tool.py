from tau_bench.envs.tool import Tool
import datetime
import hashlib
import json
from typing import Any

class LocalCleanupTool(Tool):
    """Removes local files, including downloaded logs and checksums."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LocalCleanup",
                "description": "Deletes specified files from the local environment simulation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "files_to_delete": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of local file keys to delete (e.g., 'local_file_check_log.json').",
                        }
                    },
                    "required": ["files_to_delete"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], files_to_delete: list[str]) -> str:
        deleted = [
            f_key
            for f_key in files_to_delete
            if data.pop(f_key, None) is not None
        ]
        payload = {"deleted_local_files": deleted}
        out = json.dumps(payload)
        return out
