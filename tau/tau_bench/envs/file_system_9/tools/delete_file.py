from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class DeleteFile(Tool):
    """Removes a file from the file system."""

    @staticmethod
    def invoke(data: dict[str, Any], filepath: str) -> str:
        for server in data.get("file_system", {}).values():
            for directory in server.get("directories", []):
                original_len = len(directory.get("files", []))
                directory["files"] = [
                    f
                    for f in directory.get("files", [])
                    if f"{directory.get('path')}/{f.get('filename')}" != filepath
                ]
                if len(directory.get("files", [])) < original_len:
                    payload = {"status": "success", "message": f"File {filepath} deleted."}
                    out = json.dumps(payload)
                    return out
        payload = {"error": f"File not found: {filepath}"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DeleteFile",
                "description": "Deletes a file from the file system.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "filepath": {
                            "type": "string",
                            "description": "The full path of the file to delete.",
                        }
                    },
                    "required": ["filepath"],
                },
            },
        }
