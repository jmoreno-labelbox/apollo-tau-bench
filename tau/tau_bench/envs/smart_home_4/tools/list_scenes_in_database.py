from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ListScenesInDatabase(Tool):
    """Display all scenes, with optional filtering."""

    @staticmethod
    def invoke(data: dict[str, Any], filters: dict[str, Any] | None = None) -> str:
        scenes = data.get("scenes", [])
        if filters:
            result = [
                s for s in scenes if all(s.get(k) == v for k, v in filters.items())
            ]
        else:
            result = scenes
        payload = result
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listScenesInDatabase",
                "description": "List all scenes, or filter by any field.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "filters": {
                            "type": "object",
                            "description": "Key-value pairs to filter scenes (optional)",
                            "additionalProperties": True,
                        }
                    },
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }
