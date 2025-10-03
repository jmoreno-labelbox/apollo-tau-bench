from tau_bench.envs.tool import Tool
import json
from typing import Any

class UpdateDirectoryOperationStatus(Tool):
    """Modifies the status of an individual file within a file organization task."""

    @staticmethod
    def invoke(data: dict[str, Any], file_id: str = None, status: str = None) -> str:
        for file in data.get("file_lists", []):
            if file.get("file_id") == file_id:
                file["status"] = status
                payload = {"status": "success", "updated_file": file}
                out = json.dumps(payload)
                return out
        payload = {
                "status": "failure",
                "error": f"File ID '{file_id}' not found in any directory operation.",
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateDirectoryOperationStatus",
                "description": "Updates the status of an individual file within a file organization task.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "file_id": {"type": "string"},
                        "status": {
                            "type": "string",
                            "enum": ["completed", "failed", "in_progress"],
                        },
                    },
                    "required": ["file_id", "status"],
                },
            },
        }
