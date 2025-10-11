# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _now_iso




def _now_iso() -> str:
    # return datetime.now(timezone.utc).isoformat()
    return "deterministic placeholder for current time"

class ActivateScene(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], scene_id: str) -> str:
        scenes = list(data.get('scenes', {}).values())
        devices = list(data.get('devices', {}).values())
        scene_found = False
        for scene in scenes:
            if scene.get('id') == scene_id:
                scene_found = True
                for action in scene.get('actions', []):
                    device_id = action.get('device_id')
                    update = action.get('update')
                    for device in devices:
                        if device.get('id') == device_id:
                            device['state'].update(update)
                            device['state']['last_updated'] = _now_iso()
                break

        if not scene_found:
            return json.dumps({"error": f"Scene with ID '{scene_id}' not found."}, indent=2)

        return json.dumps({"success": f"Scene '{scene_id}' activated."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "activate_scene",
                "description": "Activate a specific scene, applying its actions to devices.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "scene_id": {
                            "type": "string",
                            "description": "The ID of the scene to activate."
                        }
                    },
                    "required": ["scene_id"],
                    "additionalProperties": False
                }
            }
        }