from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class SceneManager(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], action: str = "get", scene_id: str = None, scene_data: dict = {}, execute_time: str = None) -> str:
        scenes = data.get("scenes", [])

        if action == "get":
            result = [s for s in scenes if (not scene_id or s["id"] == scene_id)]
            payload = result
            out = json.dumps(payload, indent=2)
            return out
        elif action == "execute":
            if not scene_id:
                payload = {"error": "scene_id required for execution"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
            for scene in scenes:
                if scene["id"] == scene_id:
                    payload = {
                            "success": f"Executed scene {scene_id}",
                            "actions": scene["actions"],
                        }
                    out = json.dumps(
                        payload, indent=2,
                    )
                    return out
        elif action == "create":
            if not scene_data:
                payload = {"error": "scene_data required"}
                out = json.dumps(payload, indent=2)
                return out
            scenes.append(scene_data)
            payload = {"success": f"Created scene {scene_data.get('id')}"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        elif action == "schedule":
            if not scene_id or not execute_time:
                payload = {"error": "scene_id and execute_time required"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
            for scene in scenes:
                if scene["id"] == scene_id:
                    scene["scheduled_runs"].append(execute_time)
                    payload = {"success": f"Scheduled {scene_id} for {execute_time}"}
                    out = json.dumps(
                        payload, indent=2,
                    )
                    return out
        elif action == "delete":
            if not scene_id:
                payload = {"error": "scene_id required"}
                out = json.dumps(payload, indent=2)
                return out
            scenes[:] = [s for s in scenes if s["id"] != scene_id]
            payload = {"success": f"Deleted scene {scene_id}"}
            out = json.dumps(payload, indent=2)
            return out
        payload = {"error": "Invalid action"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SceneManager",
                "description": "Manage automation scenes - CRUD and execution",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action": {
                            "type": "string",
                            "enum": ["get", "execute", "create", "schedule", "delete"],
                        },
                        "scene_id": {"type": "string", "description": "Scene ID"},
                        "scene_data": {
                            "type": "object",
                            "description": "Scene data for creation",
                        },
                        "execute_time": {
                            "type": "string",
                            "description": "Schedule execution time",
                        },
                    },
                    "required": ["action"],
                    "additionalProperties": False,
                },
            },
        }
