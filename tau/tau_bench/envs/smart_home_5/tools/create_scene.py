# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateScene(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], new_scene: Dict[str, Any]) -> str:
        scenes = list(data.get('scenes', {}).values())
        if 'id' not in new_scene:
            return json.dumps({"error": "New scene must have an 'id'."}, indent=2)
        if any(s.get('id') == new_scene['id'] for s in scenes):
            return json.dumps({"error": f"Scene with ID '{new_scene['id']}' already exists."}, indent=2)

        scenes.append(new_scene)
        return json.dumps({"success": f"Scene '{new_scene.get('name', new_scene['id'])}' created."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_scene",
                "description": "Create a new scene.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "new_scene": {
                            "type": "object",
                            "description": "A dictionary representing the new scene.",
                             "properties": {
                                "id": {"type": "string"},
                                "name": {"type": "string"},
                                "description": {"type": "string"},
                                "actions": {"type": "array", "items": {"type": "object"}}
                            },
                            "required": ["id", "name", "actions"],
                            "additionalProperties": True
                        }
                    },
                    "required": ["new_scene"],
                    "additionalProperties": False
                }
            }
        }
