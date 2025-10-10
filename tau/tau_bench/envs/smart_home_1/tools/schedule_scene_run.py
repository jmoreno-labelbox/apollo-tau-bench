# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ScheduleSceneRun(Tool):
    """Schedule a scene to run at a specific time."""

    @staticmethod
    def invoke(data: Dict[str, Any], scene_id: str, timestamp: str) -> str:
        scenes_doc: List[Dict[str, Any]] = list(data.get("scenes", {}).values())
        scenes = scenes_doc
        for scene in scenes:
            if scene.get("id") == scene_id:
                scene.setdefault("scheduled_runs", []).append(timestamp)
                return json.dumps({"success": True}, indent=2)
        return json.dumps({"error": "Scene not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "schedule_scene_run",
                "description": "Schedule a scene to run at a specific time.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "scene_id": {"type": "string", "description": "Scene identifier."},
                        "timestamp": {"type": "string", "description": "Timestamp in ISO format."},
                    },
                    "required": ["scene_id", "timestamp"],
                    "additionalProperties": False,
                },
            },
        }
