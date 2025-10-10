# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpsertScene(Tool):
    """Create a new scene or update an existing one."""

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        id: str,
        actions: List[Dict[str, Any]],
        name: str = None,
        description: str = None,
    ) -> str:
        scenes_doc: List[Dict[str, Any]] = list(data.get("scenes", {}).values())
        scenes = scenes_doc
        for scene in scenes:
            if scene.get("id") == id:
                scene.update({"name": name, "description": description, "actions": actions})
                return json.dumps({"success": "updated"}, indent=2)
        scenes.append({"id": id, "name": name, "description": description, "actions": actions})
        return json.dumps({"success": "created"}, indent=2)

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
                        "id": {"type": "string", "description": "Scene identifier."},
                        "name": {"type": "string", "description": "Scene name."},
                        "description": {"type": "string", "description": "Scene description."},
                        "actions": {"type": "array", "items": {"type": "object", "properties": {
                            "device_id": {"type": "string", "description": "Device identifier."},
                            "update": {"type": "object", "description": "Key/value pairs of state to set."},
                        }}, "description": "List of actions to perform."},
                    },
                    "required": ["id", "actions"],
                    "additionalProperties": False,
                },
            },
        }
