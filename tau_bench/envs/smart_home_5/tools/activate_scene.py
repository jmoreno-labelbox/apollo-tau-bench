from tau_bench.envs.tool import Tool
import json
from typing import Any

class ActivateScene(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], scenes: list = None, devices: list = None, scene_id: str = None) -> str:
        scenes = scenes if scenes is not None else data.get("scenes", [])
        devices = devices if devices is not None else data.get("devices", [])
        scene_found = False
        for scene in scenes:
            if scene.get("id") == scene_id:
                scene_found = True
                for action in scene.get("actions", []):
                    device_id = action.get("device_id")
                    update = action.get("update")
                    for device in devices:
                        if device.get("id") == device_id:
                            device["state"].update(update)
                            device["state"]["last_updated"] = _now_iso()
                break

        if not scene_found:
            payload = {"error": f"Scene with ID '{scene_id}' not found."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = {"success": f"Scene '{scene_id}' activated."}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ActivateScene",
                "description": "Activate a specific scene, applying its actions to devices.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "scene_id": {
                            "type": "string",
                            "description": "The ID of the scene to activate.",
                        }
                    },
                    "required": ["scene_id"],
                    "additionalProperties": False,
                },
            },
        }
