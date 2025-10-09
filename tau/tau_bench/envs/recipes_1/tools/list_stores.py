from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ListStores(Tool):
    """Retrieve all stores."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        return _json_dump(data.get("stores", {}))
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listStores",
                "description": "List available stores.",
                "parameters": {"type": "object", "properties": {}},
            },
        }
