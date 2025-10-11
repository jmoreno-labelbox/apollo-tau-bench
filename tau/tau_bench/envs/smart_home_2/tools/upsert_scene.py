# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _find






def _load(entity: str, data: Dict[str, Any]):
    """Return a *mutable copy* of a top-level collection list."""
    return [*data.get(entity, [])]

def _find(collection: List[Dict[str, Any]], entity_id: str):
    for idx, item in enumerate(collection):
        if item.get("id") == entity_id or item.get("reminder_id") == entity_id \
           or item.get("list_id") == entity_id or item.get("member_id") == entity_id:
            return idx, item
    return None, None

class UpsertScene(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], scene: Dict[str, Any]) -> str:
        if not scene:
            return json.dumps({"error": "scene object required"}, indent=2)
        scenes = _load("scenes", data)
        idx, _ = _find(scenes, scene["id"])
        if idx is not None:
            scenes[idx].update(scene)
            msg = "updated"
        else:
            scenes.append(scene)
            msg = "added"
            data["scenes"] = scenes
        return json.dumps({"success": f"scene {msg}", "scene": scene}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "upsert_scene",
                "description": "Create a new scene or update an existing one.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "scene": {
                            "type": "object",
                            "description": "Full or partial scene object.",
                            "additionalProperties": True
                        }
                    },
                    "required": ["scene"],
                    "additionalProperties": False
                }
            }
        }