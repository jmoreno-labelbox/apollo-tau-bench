from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetSceneByIdOrFilter(Tool):
    """Fetch scene(s) using id or filters."""

    @staticmethod
    def invoke(
        data: dict[str, Any], scene_id: str = "", filters: dict[str, Any] | None = None
    ) -> str:
        scenes = data.get("scenes", {}).values()
        if scene_id:
            result = [s for s in scenes.values() if s.get("id") == scene_id]
        elif filters:
            result = [
                s for s in scenes.values() if all(s.get(k) == v for k, v in filters.items())
            ]
        else:
            payload = {"error": "Either 'scene_id' or 'filters' must be provided"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = result
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSceneByIdOrFilter",
                "description": "Retrieve scene(s) by id or filter. If 'scene_id' is provided, returns the scene with that id. If 'filters' is provided, returns all scenes matching the filter.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "scene_id": {
                            "type": "string",
                            "description": "Scene id to retrieve (optional if using filters)",
                        },
                        "filters": {
                            "type": "object",
                            "description": "Key-value pairs to filter scenes (optional if using scene_id)",
                            "additionalProperties": True,
                        },
                    },
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }
