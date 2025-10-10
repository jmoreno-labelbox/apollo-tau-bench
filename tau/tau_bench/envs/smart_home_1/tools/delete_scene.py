# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DeleteScene(Tool):
    """Remove a scene permanently."""

    @staticmethod
    def invoke(data: Dict[str, Any], scene_id: str) -> str:
        scenes_doc: List[Dict[str, Any]] = list(data.get("scenes", {}).values())
        scenes = scenes_doc
        original_len = len(scenes)
        scenes_doc = [s for s in scenes if s.get("id") != scene_id]
        if len(scenes_doc) == original_len:
            return json.dumps({"error": "Scene not found"}, indent=2)
        return json.dumps({"success": True}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "delete_scene",
                "description": "Remove a scene permanently.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "scene_id": {"type": "string", "description": "Scene identifier."},
                    },
                    "required": ["scene_id"],
                    "additionalProperties": False,
                },
            },
        }
