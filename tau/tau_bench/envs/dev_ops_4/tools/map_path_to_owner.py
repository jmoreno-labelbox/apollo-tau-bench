from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class MapPathToOwner(Tool):
    """Associate a code/asset path with its owner utilizing ownership_map."""

    @staticmethod
    def invoke(data: dict[str, Any], file_path: str = None) -> str:
        maps = data.get("ownership_map", [])
        rec = next((m for m in maps if m.get("file_path") == file_path), None)
        payload = {"owner_map": rec}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "MapPathToOwner",
                "description": "Look up an ownership record by exact file_path.",
                "parameters": {
                    "type": "object",
                    "properties": {"file_path": {"type": "string"}},
                    "required": ["file_path"],
                },
            },
        }
