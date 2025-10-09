from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class FindFullPathForFileName(Tool):
    """Locates the complete file path for a specified file name by querying the ownership map."""

    @staticmethod
    def invoke(data: dict[str, Any], file_name: str = None) -> str:
        ownership_map = data.get("ownership_map", {}).values()

        # Look for a file path that concludes with the specified file name.
        for ownership in ownership_map:
            if ownership.get("file_path", "").endswith(file_name):
                payload = {"file_path": ownership.get("file_path")}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Full path for file name '{file_name}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindFullPathForFileName",
                "description": "Finds the full file path for a given file name by searching the ownership map.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "file_name": {
                            "type": "string",
                            "description": "The name of the file (e.g., 'renderer.cpp').",
                        }
                    },
                    "required": ["file_name"],
                },
            },
        }
