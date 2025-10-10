# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetSceneByIdOrFilter(Tool):
    """Retrieve scene(s) by id or filter."""
    @staticmethod
    def invoke(data: Dict[str, Any], scene_id: str = "", filters: Optional[Dict[str, Any]] = None) -> str:
        scenes = list(data.get('scenes', {}).values())
        if scene_id:
            result = [s for s in scenes if s.get("id") == scene_id]
        elif filters:
            result = [s for s in scenes if all(s.get(k) == v for k, v in filters.items())]
        else:
            return json.dumps({"error": "Either 'scene_id' or 'filters' must be provided"}, indent=2)
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_scene_by_id_or_filter",
                "description": "Retrieve scene(s) by id or filter. If 'scene_id' is provided, returns the scene with that id. If 'filters' is provided, returns all scenes matching the filter.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "scene_id": {
                            "type": "string",
                            "description": "Scene id to retrieve (optional if using filters)"
                        },
                        "filters": {
                            "type": "object",
                            "description": "Key-value pairs to filter scenes (optional if using scene_id)",
                            "additionalProperties": True
                        }
                    },
                    "required": [],
                    "additionalProperties": False
                }
            }
        }
