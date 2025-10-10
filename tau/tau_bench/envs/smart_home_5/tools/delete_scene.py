# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DeleteScene(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], scene_id: str) -> str:
        scenes = list(data.get('scenes', {}).values())
        initial_len = len(scenes)
        scenes[:] = [s for s in scenes if s.get('id') != scene_id]

        if len(scenes) == initial_len:
            return json.dumps({"error": f"Scene with ID '{scene_id}' not found."}, indent=2)

        return json.dumps({"success": f"Scene '{scene_id}' deleted."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_scene",
                "description": "Delete a scene.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "scene_id": {
                            "type": "string",
                            "description": "The ID of the scene to delete."
                        }
                    },
                    "required": ["scene_id"],
                    "additionalProperties": False
                }
            }
        }
