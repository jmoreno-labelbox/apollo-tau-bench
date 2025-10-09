from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class BrowseFileStore(Tool):
    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        payload = {"files": data.get("file_store", {}).values()}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listFileStore",
                "description": "List all files in the file store.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }
