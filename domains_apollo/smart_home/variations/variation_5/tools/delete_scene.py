from tau_bench.envs.tool import Tool
import json
from typing import Any

class DeleteScene(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], scene_id: str) -> str:
        scenes = data.get("scenes", [])
        initial_len = len(scenes)
        scenes[:] = [s for s in scenes if s.get("id") != scene_id]

        if len(scenes) == initial_len:
            payload = {"error": f"Scene with ID '{scene_id}' not found."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = {"success": f"Scene '{scene_id}' deleted."}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DeleteScene",
                "description": "Delete a scene.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "scene_id": {
                            "type": "string",
                            "description": "The ID of the scene to delete.",
                        }
                    },
                    "required": ["scene_id"],
                    "additionalProperties": False,
                },
            },
        }
