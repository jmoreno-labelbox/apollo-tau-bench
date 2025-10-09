from tau_bench.envs.tool import Tool
import json
from typing import Any

class ScheduleSceneRun(Tool):
    """Plan a scene to execute at a designated time."""

    @staticmethod
    def invoke(data: dict[str, Any], scene_id: str, timestamp: str) -> str:
        scenes_doc: list[dict[str, Any]] = data.get("scenes", [])
        scenes = scenes_doc
        for scene in scenes:
            if scene.get("id") == scene_id:
                scene.setdefault("scheduled_runs", []).append(timestamp)
                payload = {"success": True}
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": "Scene not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ScheduleSceneRun",
                "description": "Schedule a scene to run at a specific time.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "scene_id": {
                            "type": "string",
                            "description": "Scene identifier.",
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "Timestamp in ISO format.",
                        },
                    },
                    "required": ["scene_id", "timestamp"],
                    "additionalProperties": False,
                },
            },
        }
