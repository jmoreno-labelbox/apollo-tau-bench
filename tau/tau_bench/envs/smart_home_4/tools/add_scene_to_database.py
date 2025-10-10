# Copyright Sierra Technologies

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddSceneToDatabase(Tool):
    """Add a new scene."""
    @staticmethod
    def invoke(data: Dict[str, Any], scene: Optional[Dict[str, Any]] = None, threshold: Optional[Dict[str, Any]] = None) -> str:
        if not scene:
            return json.dumps({"error": "'scene' parameter is required"}, indent=2)
        scenes = list(data.get('scenes', {}).values())
        if any(s["id"] == scene.get("id") for s in scenes):
            return json.dumps({"error": "Scene with this id already exists"}, indent=2)
        if not threshold:
            scenes.append(scene)
        else:
            for sensor in data.get('sensors', []):
                if sensor.get("id") == threshold.get("sensor_id"):
                    for param, limit in threshold.items():
                        current_value = sensor['state'].get(param)
                        if (limit.get('operator') == 'gt' and current_value > limit.get('value')) or (limit.get('operator') == 'lt' and current_value < limit.get('value')):
                            scenes.append(scene)
        return json.dumps({"success": "Scene added", "scene": scene, "scenes": scenes}, indent=2)




    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_scene_to_database",
                "description": "Add a new scene. All fields must be provided in the 'scene' object.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "scene": {
                            "type": "object",
                            "description": "The full scene object to add (must include id, name, description, actions, scheduled_runs)",
                            "additionalProperties": True
                        }
                    },
                    "required": ["scene"],
                    "additionalProperties": False
                }
            }
        }
