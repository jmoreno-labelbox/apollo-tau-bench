# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RunScene(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], scene_id: str) -> str:
        _, scene = _find(list(data.get("scenes", {}).values()), scene_id)
        if not scene:
            return json.dumps({"error": f"scene '{scene_id}' not found"}, indent=2)
        results = []
        for act in scene.get("actions", []):
            res = ModifyDeviceState.invoke(data, device_id=act["device_id"], update=act["update"])
            results.append(json.loads(res))
        return json.dumps({"success": f"scene '{scene_id}' executed", "results": results}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "run_scene",
                "description": "Execute the actions of a scene immediately.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "scene_id": {"type": "string", "description": "Scene id to run"}
                    },
                    "required": ["scene_id"],
                    "additionalProperties": False
                }
            }
        }
