# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _find


class GetEntity(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], entity_type: str, entity_id: Optional[str] = None) -> str:
        collection = data.get(entity_type)
        if collection is None:
            return json.dumps({"error": f"unknown entity_type '{entity_type}'"}, indent=2)
        if entity_id:
            _, item = _find(collection, entity_id)
            if not item:
                return json.dumps({"error": f"{entity_type} '{entity_id}' not found"}, indent=2)
        else:
            item = collection
        return json.dumps(item, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_entity",
                "description": "Fetch a single entity (device, sensor, room, scene, list, reminder, member) by id. If no id is provided, return all entities of the given type.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "entity_type": {
                            "type": "string",
                            "description": "One of: devices, sensors, rooms, scenes, custom_lists, reminders, members"
                        },
                        "entity_id": {
                            "type": "string",
                            "description": "ID of the entity to fetch"
                        }
                    },
                    "required": ["entity_type"],
                    "additionalProperties": False
                }
            }
        }
