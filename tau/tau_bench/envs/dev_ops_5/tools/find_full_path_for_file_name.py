# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindFullPathForFileName(Tool):
    """Finds the full file path for a given file name by searching the ownership map."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        file_name = kwargs.get("file_name")
        ownership_map = data.get("ownership_map", [])
        
        # Locate a file path that concludes with the specified file name.
        for ownership in ownership_map:
            if ownership.get("file_path", "").endswith(file_name):
                return json.dumps({"file_path": ownership.get("file_path")})
        
        return json.dumps({"error": f"Full path for file name '{file_name}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_full_path_for_file_name",
                "description": "Finds the full file path for a given file name by searching the ownership map.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "file_name": {
                            "type": "string",
                            "description": "The name of the file (e.g., 'renderer.cpp')."
                        }
                    },
                    "required": ["file_name"]
                }
            }
        }
