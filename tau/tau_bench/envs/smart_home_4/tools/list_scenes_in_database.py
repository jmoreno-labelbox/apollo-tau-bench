# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListScenesInDatabase(Tool):
    """List all scenes, with optional filters."""
    @staticmethod
    def invoke(data: Dict[str, Any], filters: Optional[Dict[str, Any]] = None) -> str:
        scenes = list(data.get('scenes', {}).values())
        if filters:
            result = [s for s in scenes if all(s.get(k) == v for k, v in filters.items())]
        else:
            result = scenes
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_scenes_in_database",
                "description": "List all scenes, or filter by any field.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "filters": {
                            "type": "object",
                            "description": "Key-value pairs to filter scenes (optional)",
                            "additionalProperties": True
                        }
                    },
                    "required": [],
                    "additionalProperties": False
                }
            }
        }
