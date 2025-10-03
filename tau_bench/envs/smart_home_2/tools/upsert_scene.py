from tau_bench.envs.tool import Tool
import json
from typing import Any

class UpsertScene(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], scene: dict[str, Any]) -> str:
        if not scene:
            payload = {"error": "scene object required"}
            out = json.dumps(payload, indent=2)
            return out
        scenes = _load("scenes", data)
        idx, _ = _find(scenes, scene["id"])
        if idx is not None:
            scenes[idx].update(scene)
            msg = "updated"
        else:
            scenes.append(scene)
            msg = "added"
            data["scenes"] = scenes
        payload = {"success": f"scene {msg}", "scene": scene}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpsertScene",
                "description": "Create a new scene or update an existing one.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "scene": {
                            "type": "object",
                            "description": "Full or partial scene object.",
                            "additionalProperties": True,
                        }
                    },
                    "required": ["scene"],
                    "additionalProperties": False,
                },
            },
        }
