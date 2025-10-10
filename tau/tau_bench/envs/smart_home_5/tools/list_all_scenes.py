# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListAllScenes(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any]) -> str:
        scenes = list(data.get('scenes', {}).values())
        scene_info = [{"id": s.get("id"), "name": s.get("name"), "description": s.get("description")} for s in scenes]
        return json.dumps(scene_info, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_all_scenes",
                "description": "List all available scenes."
            }
        }
