from tau_bench.envs.tool import Tool
import datetime
import hashlib
import json
from typing import Any

class CleanOriginalDirectoryTool(Tool):
    """Emulates removing all original files following a successful copy and verification process."""

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CleanOriginalDirectory",
                "description": "Deletes the original files that have been successfully moved and returns the count of cleaned files.",
                "parameters": {
                    "type": "object",
                    "properties": {"target_directory": {"type": "string"}},
                    "required": ["target_directory"],
                },
            },
        }

    @staticmethod
    def invoke(data: dict[str, Any], target_directory: str) -> str:
        cleaned_count = 0

        # Count files present in the file_list (these are the ones being cleaned)
        if "file_list" in data:
            cleaned_count = len(data["file_list"])

        # Save the count of cleaned files for output
        data["cleaned_files_count"] = cleaned_count
        payload = {"status": "success", "cleaned_files_count": cleaned_count}
        out = json.dumps(payload)
        return out
