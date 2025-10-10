# Sierra copyright notice

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DeleteSceneFromDatabase(Tool):
    """Remove a scene by id."""
    @staticmethod
    def invoke(data: Dict[str, Any], scene_id: str = "") -> str:
        if not scene_id:
            return json.dumps({"error": "'scene_id' parameter is required"}, indent=2)
        scenes = list(data.get('scenes', {}).values())
        new_list = [s for s in scenes if s["id"] != scene_id]
        if len(new_list) == len(scenes):
            return json.dumps({"error": "Scene not found"}, indent=2)
        return json.dumps({"success": "Scene deleted", "scene_id": scene_id, "scenes": new_list}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_scene_from_database",
                "description": "Remove a scene by id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "scene_id": {
                            "type": "string",
                            "description": "The id of the scene to delete."
                        }
                    },
                    "required": ["scene_id"],
                    "additionalProperties": False
                }
            }
        }
