# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class QueryEntities(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], entity_type: str, filters: Optional[Dict[str, Any]] = None) -> str:
        collection = data.get(entity_type, [])
        matches: List[Dict[str, Any]] = []
        
        # If no filters, return all items
        if filters is None or not filters:
            matches = collection if isinstance(collection, list) else list(collection.values()) if isinstance(collection, dict) else []
        else:
            for item in collection:
                ok = True
                for k, v in filters.items():
                    if item.get(k) != v:
                        ok = False
                        break
                if ok:
                    matches.append(item)
        return json.dumps({"count": len(matches), "results": matches}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "query_entities",
                "description": "Return all entities of a given type that match simple equality filters (top-level keys).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "entity_type": {
                            "type": "string",
                            "description": "Collection to search: devices, sensors, rooms, scenes, custom_lists, reminders, members"
                        },
                        "filters": {
                            "type": "object",
                            "description": "Key/value pairs that must match (equality) on each entity.",
                            "additionalProperties": True
                        }
                    },
                    "required": ["entity_type"],
                    "additionalProperties": False
                }
            }
        }
