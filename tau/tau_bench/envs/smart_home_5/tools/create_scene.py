from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CreateScene(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], new_scene_id: str = None, new_scene_name: str = None,
    new_scene: Any = None,
    ) -> str:
        scenes = data.get("scenes", [])
        if not new_scene_id:
            payload = {"error": "New scene must have an 'id'."}
            out = json.dumps(payload, indent=2)
            return out
        if any(s.get("id") == new_scene_id for s in scenes):
            payload = {"error": f"Scene with ID '{new_scene_id}' already exists."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        new_scene = {"id": new_scene_id, "name": new_scene_name} if new_scene_name else {"id": new_scene_id}
        scenes.append(new_scene)
        payload = {"success": f"Scene '{new_scene.get('name', new_scene_id)}' created."}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateScene",
                "description": "Create a new scene.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "new_scene": {
                            "type": "object",
                            "description": "A dictionary representing the new scene.",
                            "properties": {
                                "id": {"type": "string"},
                                "name": {"type": "string"},
                                "description": {"type": "string"},
                                "actions": {
                                    "type": "array",
                                    "items": {"type": "object"},
                                },
                            },
                            "required": ["id", "name", "actions"],
                            "additionalProperties": True,
                        }
                    },
                    "required": ["new_scene"],
                    "additionalProperties": False,
                },
            },
        }
