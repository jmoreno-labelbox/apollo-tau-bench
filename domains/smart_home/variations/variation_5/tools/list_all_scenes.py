from tau_bench.envs.tool import Tool
import json
from typing import Any

class ListAllScenes(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], scenes: list[dict[str, Any]] = []) -> str:
        scene_info = [
            {
                "id": s.get("id"),
                "name": s.get("name"),
                "description": s.get("description"),
            }
            for s in scenes
        ]
        payload = scene_info
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListAllScenes",
                "description": "List all available scenes.",
            },
        }
