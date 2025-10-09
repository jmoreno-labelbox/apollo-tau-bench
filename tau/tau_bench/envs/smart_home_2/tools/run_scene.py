from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class RunScene(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], scene_id: str) -> str:
        _, scene = _find(data.get("scenes", []), scene_id)
        if not scene:
            payload = {"error": f"scene '{scene_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out
        results = []
        for act in scene.get("actions", []):
            res = ModifyDeviceState.invoke(
                data, device_id=act["device_id"], update=act["update"]
            )
            results.append(json.loads(res))
        payload = {"success": f"scene '{scene_id}' executed", "results": results}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RunScene",
                "description": "Execute the actions of a scene immediately.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "scene_id": {"type": "string", "description": "Scene id to run"}
                    },
                    "required": ["scene_id"],
                    "additionalProperties": False,
                },
            },
        }
