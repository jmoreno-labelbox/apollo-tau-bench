from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class QueryEntities(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], entity_type: str, filters: dict[str, Any]) -> str:
        collection = data.get(entity_type, {}).values()
        matches: list[dict[str, Any]] = []
        for item in collection:
            ok = True
            for k, v in filters.items():
                if item.get(k) != v:
                    ok = False
                    break
            if ok:
                matches.append(item)
        payload = {"count": len(matches), "results": matches}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "QueryEntities",
                "description": "Return all entities of a given type that match simple equality filters (top-level keys).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "entity_type": {
                            "type": "string",
                            "description": "Collection to search: devices, sensors, rooms, scenes, custom_lists, reminders, members",
                        },
                        "filters": {
                            "type": "object",
                            "description": "Key/value pairs that must match (equality) on each entity.",
                            "additionalProperties": True,
                        },
                    },
                    "required": ["entity_type"],
                    "additionalProperties": False,
                },
            },
        }
