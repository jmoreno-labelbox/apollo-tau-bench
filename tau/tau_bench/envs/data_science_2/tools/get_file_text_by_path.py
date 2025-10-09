from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetFileTextByPath(Tool):
    """Provides file content and metadata from file_store using the specified path."""

    @staticmethod
    def invoke(data: dict[str, Any], path: str) -> str:
        rows = data.get("file_store", {}).values()
        for row in rows:
            paths = row.get("paths", [])
            if path in paths:
                i = paths.index(path)
                out = {
                    "path": path,
                    "file_contents_text": (
                        row.get("file_contents_text", [None] * len(paths))[i]
                        if i < len(row.get("file_contents_text", []))
                        else None
                    ),
                    "file_mime_types": (
                        row.get("file_mime_types", [None] * len(paths))[i]
                        if i < len(row.get("file_mime_types", []))
                        else None
                    ),
                    "char_counts": (
                        row.get("char_counts", [None] * len(paths))[i]
                        if i < len(row.get("char_counts", []))
                        else None
                    ),
                }
                payload = out
                out = json.dumps(payload)
                return out
        payload = {"error": "file not found", "path": path}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetFileTextByPath",
                "description": "Returns file text and metadata from file_store by path.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "path": {
                            "type": "string",
                            "description": "Exact file path stored in file_store.paths.",
                        }
                    },
                    "required": ["path"],
                },
            },
        }
