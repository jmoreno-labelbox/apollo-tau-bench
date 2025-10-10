# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindFileOwner(Tool):
    """Finds the owner of a file based on the ownership map."""
    @staticmethod
    def invoke(data: Dict[str, Any], file_path) -> str:
        ownership_map = data.get("ownership_map", [])
        most_specific_owner = None
        longest_match = -1

        for ownership in ownership_map:
            owner_path = ownership.get("file_path")
            if file_path.startswith(owner_path):
                if len(owner_path) > longest_match:
                    longest_match = len(owner_path)
                    most_specific_owner = ownership
        
        if most_specific_owner:
            return json.dumps(most_specific_owner)
        return json.dumps({"info": f"Owner for file path '{file_path}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_file_owner",
                "description": "Finds the owner of a file based on the ownership map.",
                "parameters": {
                    "type": "object",
                    "properties": {"file_path": {"type": "string", "description": "The path to the file."}},
                    "required": ["file_path"],
                },
            },
        }
