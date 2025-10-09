from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetEntity(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], entity_type: str, entity_id: str | None = None
    ) -> str:
        collection = data.get(entity_type)
        if collection is None:
            payload = {"error": f"unknown entity_type '{entity_type}'"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        if entity_id:
            _, item = _find(collection, entity_id)
            if not item:
                payload = {"error": f"{entity_type} '{entity_id}' not found"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
        else:
            item = collection
        payload = item
        out = json.dumps(payload, indent=2)
        return out
    

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetEntity",
                "description": "Fetch a single entity (device, sensor, room, scene, list, reminder, member) by id. If no id is provided, return all entities of the given type.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "entity_type": {
                            "type": "string",
                            "description": "One of: devices, sensors, rooms, scenes, custom_lists, reminders, members",
                        },
                        "entity_id": {
                            "type": "string",
                            "description": "ID of the entity to fetch",
                        },
                    },
                    "required": ["entity_type"],
                    "additionalProperties": False,
                },
            },
        }
