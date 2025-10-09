from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ListProjectsCatalog(Tool):
    """Retrieve all projects."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        payload = {"projects": data.get("projects", [])}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListProjectsCatalog",
                "description": "List projects.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }
