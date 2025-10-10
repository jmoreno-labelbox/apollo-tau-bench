# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateSceneInDatabase(Tool):
    """Update any field of a scene."""
    @staticmethod
    def invoke(data: Dict[str, Any], scene_id: str = "", updates: Optional[Dict[str, Any]] = None) -> str:
        if not scene_id or not updates:
            return json.dumps({"error": "'scene_id' and 'updates' parameters are required"}, indent=2)
        scenes = list(data.get('scenes', {}).values())
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
            return json.dumps({"error": "Scene not found"}, indent=2)
        return json.dumps({"success": "Scene updated", "scene_id": scene_id, "updates": updates, "scenes": scenes}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_scene_in_database",
                "description": "Update any field of a scene by id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "scene_id": {
                            "type": "string",
                            "description": "The id of the scene to update."
                        },
                        "updates": {
                            "type": "object",
                            "description": "Key-value pairs of fields to update.",
                            "additionalProperties": True
                        }
                    },
                    "required": ["scene_id", "updates"],
                    "additionalProperties": False
                }
            }
        }
