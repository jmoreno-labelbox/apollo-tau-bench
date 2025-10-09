from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class RetrieveFileEntry(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], file_id: str = None, path: str = None) -> str:
        files = data.get("file_store", {}).values() or []
        row = None
        if file_id is not None:
            row = next((f for f in files.values() if str(f.get("file_id")) == str(file_id)), None)
        elif path:
            row = next((f for f in files.values() if f.get("path") == path), None)
        payload = row or {"error": "File not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RetrieveFileEntry",
                "description": "Read a file metadata record by id or path.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "file_id": {"type": "string"},
                        "path": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }
