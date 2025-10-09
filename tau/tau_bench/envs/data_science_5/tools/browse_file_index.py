from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class BrowseFileIndex(Tool):
    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        payload = {"files": data.get("file_store", [])}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "browseFileIndex",
                "description": "List all file metadata rows.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }
