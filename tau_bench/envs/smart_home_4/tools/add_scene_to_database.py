from tau_bench.envs.tool import Tool
import json
from typing import Any

class AddSceneToDatabase(Tool):
    """Introduce a new scene."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        scene: dict[str, Any] | None = None,
        threshold: dict[str, Any] | None = None,
    ) -> str:
        if not scene:
            payload = {"error": "'scene' parameter is required"}
            out = json.dumps(payload, indent=2)
            return out
        scenes = data.get("scenes", [])
        if any(s["id"] == scene.get("id") for s in scenes):
            payload = {"error": "Scene with this id already exists"}
            out = json.dumps(payload, indent=2)
            return out
        if not threshold:
            scenes.append(scene)
        else:
            for sensor in data.get("sensors", []):
                if sensor.get("id") == threshold.get("sensor_id"):
                    for param, limit in threshold.items():
                        current_value = sensor["state"].get(param)
                        if (
                            limit.get("operator") == "gt"
                            and current_value > limit.get("value")
                        ) or (
                            limit.get("operator") == "lt"
                            and current_value < limit.get("value")
                        ):
                            scenes.append(scene)
        payload = {"success": "Scene added", "scene": scene, "scenes": scenes}
        out = json.dumps(
            payload, indent=2
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddSceneToDatabase",
                "description": "Add a new scene. All fields must be provided in the 'scene' object.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "scene": {
                            "type": "object",
                            "description": "The full scene object to add (must include id, name, description, actions, scheduled_runs)",
                            "additionalProperties": True,
                        }
                    },
                    "required": ["scene"],
                    "additionalProperties": False,
                },
            },
        }
