# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CleanOriginalDirectoryTool(Tool):
    """Simulates deleting all original files after a successful copy and verify operation."""

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "clean_original_directory",
                "description": "Deletes the original files that have been successfully moved and returns the count of cleaned files.",
                "parameters": {
                    "type": "object",
                    "properties": {"target_directory": {"type": "string"}},
                    "required": ["target_directory"],
                },
            },
        }

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        target_directory = kwargs["target_directory"]
        cleaned_count = 0

        # Count files that were in the file_list (these are the ones being cleaned)
        if "file_list" in data:
            cleaned_count = len(data["file_list"])

        # Store the cleaned files count for output
        data["cleaned_files_count"] = cleaned_count

        return json.dumps({"status": "success", "cleaned_files_count": cleaned_count})
