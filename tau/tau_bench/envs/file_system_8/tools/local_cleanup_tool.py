# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LocalCleanupTool(Tool):
    """Deletes local files, such as downloaded logs and checksums."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "local_cleanup",
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
    def invoke(data: Dict[str, Any], files_to_delete) -> str:
        deleted = [
            f_key
            for f_key in files_to_delete
            if data.pop(f_key, None) is not None
        ]
        return json.dumps({"deleted_local_files": deleted})
