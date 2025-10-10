# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SceneManager(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        scenes = list(data.get('scenes', {}).values())
        action = kwargs.get('action', 'get')
        scene_id = kwargs.get('scene_id')
        scene_data = kwargs.get('scene_data', {})
        execute_time = kwargs.get('execute_time')

        if action == 'get':
            result = [s for s in scenes if (not scene_id or s['id'] == scene_id)]
            return json.dumps(result, indent=2)
        elif action == 'execute':
            if not scene_id:
                return json.dumps({"error": "scene_id required for execution"}, indent=2)
            for scene in scenes:
                if scene['id'] == scene_id:
                    return json.dumps({"success": f"Executed scene {scene_id}", "actions": scene['actions']}, indent=2)
        elif action == 'create':
            if not scene_data:
                return json.dumps({"error": "scene_data required"}, indent=2)
            scenes.append(scene_data)
            return json.dumps({"success": f"Created scene {scene_data.get('id')}"}, indent=2)
        elif action == 'schedule':
            if not scene_id or not execute_time:
                return json.dumps({"error": "scene_id and execute_time required"}, indent=2)
            for scene in scenes:
                if scene['id'] == scene_id:
                    scene['scheduled_runs'].append(execute_time)
                    return json.dumps({"success": f"Scheduled {scene_id} for {execute_time}"}, indent=2)
        elif action == 'delete':
            if not scene_id:
                return json.dumps({"error": "scene_id required"}, indent=2)
            scenes[:] = [s for s in scenes if s['id'] != scene_id]
            return json.dumps({"success": f"Deleted scene {scene_id}"}, indent=2)

        return json.dumps({"error": "Invalid action"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "scene_manager",
                "description": "Manage automation scenes - CRUD and execution",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "action": {"type": "string", "enum": ["get", "execute", "create", "schedule", "delete"]},
                        "scene_id": {"type": "string", "description": "Scene ID"},
                        "scene_data": {"type": "object", "description": "Scene data for creation"},
                        "execute_time": {"type": "string", "description": "Schedule execution time"}
                    },
                    "required": ["action"],
                    "additionalProperties": False
                }
            }
        }
