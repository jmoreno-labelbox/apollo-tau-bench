# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DeleteFile(Tool):
    """Deletes a file from the file system."""
    @staticmethod
    def invoke(data: Dict[str, Any], filepath) -> str:
        for server in list(data.get("file_system", {}).values()):
            for directory in server.get("directories", []):
                original_len = len(directory.get("files", []))
                directory["files"] = [f for f in directory.get("files", []) if f"{directory.get('path')}/{f.get('filename')}" != filepath]
                if len(directory.get("files", [])) < original_len:
                    return json.dumps({"status": "success", "message": f"File {filepath} deleted."})
        return json.dumps({"error": f"File not found: {filepath}"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_file",
                "description": "Deletes a file from the file system.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "filepath": {"type": "string", "description": "The full path of the file to delete."}
                    },
                    "required": ["filepath"],
                },
            },
        }
