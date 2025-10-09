from tau_bench.envs.tool import Tool
import json
from typing import Any

class UpdateSceneInDatabase(Tool):
    """Modify any attribute of a scene."""

    @staticmethod
    def invoke(
        data: dict[str, Any], scene_id: str = "", updates: dict[str, Any] | None = None
    ) -> str:
        if not scene_id or not updates:
            payload = {"error": "'scene_id' and 'updates' parameters are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        scenes = data.get("scenes", [])
        found = False
        for s in scenes:
            if s["id"] == scene_id:
                for k, v in updates.items():
                    if k == "actions":
                        s["actions"] + v
                    else:
                        s[k] = v
                found = True
                break
        if not found:
            payload = {"error": "Scene not found"}
            out = json.dumps(payload, indent=2)
            return out
        payload = {
                "success": "Scene updated",
                "scene_id": scene_id,
                "updates": updates,
                "scenes": scenes,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateSceneInDatabase",
                "description": "Update any field of a scene by id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "scene_id": {
                            "type": "string",
                            "description": "The id of the scene to update.",
                        },
                        "updates": {
                            "type": "object",
                            "description": "Key-value pairs of fields to update.",
                            "additionalProperties": True,
                        },
                    },
                    "required": ["scene_id", "updates"],
                    "additionalProperties": False,
                },
            },
        }
