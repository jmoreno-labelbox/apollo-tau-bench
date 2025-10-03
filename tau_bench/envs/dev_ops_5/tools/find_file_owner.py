from tau_bench.envs.tool import Tool
import json
from typing import Any

class FindFileOwner(Tool):
    """Identifies the owner of a file according to the ownership map."""

    @staticmethod
    def invoke(data: dict[str, Any], file_path: str) -> str:
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
            payload = most_specific_owner
            out = json.dumps(payload)
            return out
        payload = {"info": f"Owner for file path '{file_path}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindFileOwner",
                "description": "Finds the owner of a file based on the ownership map.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "file_path": {
                            "type": "string",
                            "description": "The path to the file.",
                        }
                    },
                    "required": ["file_path"],
                },
            },
        }
