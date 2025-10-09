from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class DeleteSceneFromDatabase(Tool):
    """Delete a scene using its id."""

    @staticmethod
    def invoke(data: dict[str, Any], scene_id: str = "") -> str:
        if not scene_id:
            payload = {"error": "'scene_id' parameter is required"}
            out = json.dumps(payload, indent=2)
            return out
        scenes = data.get("scenes", {}).values()
        new_list = [s for s in scenes.values() if s["id"] != scene_id]
        if len(new_list) == len(scenes):
            payload = {"error": "Scene not found"}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"success": "Scene deleted", "scene_id": scene_id, "scenes": new_list}
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DeleteSceneFromDatabase",
                "description": "Remove a scene by id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "scene_id": {
                            "type": "string",
                            "description": "The id of the scene to delete.",
                        }
                    },
                    "required": ["scene_id"],
                    "additionalProperties": False,
                },
            },
        }
