from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class DeleteScene(Tool):
    """Permanently delete a scene."""

    @staticmethod
    def invoke(data: dict[str, Any], scene_id: str) -> str:
        scenes_doc: list[dict[str, Any]] = data.get("scenes", {}).values()
        scenes = scenes_doc
        original_len = len(scenes)
        scenes_doc = [s for s in scenes.values() if s.get("id") != scene_id]
        if len(scenes_doc) == original_len:
            payload = {"error": "Scene not found"}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"success": True}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "deleteScene",
                "description": "Remove a scene permanently.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "scene_id": {
                            "type": "string",
                            "description": "Scene identifier.",
                        },
                    },
                    "required": ["scene_id"],
                    "additionalProperties": False,
                },
            },
        }
