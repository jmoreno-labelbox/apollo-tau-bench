from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpsertScene(Tool):
    """Establish a new scene or modify an existing one."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        id: str,
        actions: list[dict[str, Any]],
        name: str = None,
        description: str = None
    ) -> str:
        scenes_doc: list[dict[str, Any]] = data.get("scenes", [])
        scenes = scenes_doc
        for scene in scenes:
            if scene.get("id") == id:
                scene.update(
                    {"name": name, "description": description, "actions": actions}
                )
                payload = {"success": "updated"}
                out = json.dumps(payload, indent=2)
                return out
        scenes.append(
            {"id": id, "name": name, "description": description, "actions": actions}
        )
        payload = {"success": "created"}
        out = json.dumps(payload, indent=2)
        return out
        pass
        scenes_doc: list[dict[str, Any]] = data.get("scenes", [])
        scenes = scenes_doc
        for scene in scenes:
            if scene.get("id") == id:
                scene.update(
                    {"name": name, "description": description, "actions": actions}
                )
                payload = {"success": "updated"}
                out = json.dumps(payload, indent=2)
                return out
        scenes.append(
            {"id": id, "name": name, "description": description, "actions": actions}
        )
        payload = {"success": "created"}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpsertScene",
                "description": "Create a new scene or update an existing one.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string", "description": "Scene identifier."},
                        "name": {"type": "string", "description": "Scene name."},
                        "description": {
                            "type": "string",
                            "description": "Scene description.",
                        },
                        "actions": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "device_id": {
                                        "type": "string",
                                        "description": "Device identifier.",
                                    },
                                    "update": {
                                        "type": "object",
                                        "description": "Key/value pairs of state to set.",
                                    },
                                },
                            },
                            "description": "List of actions to perform.",
                        },
                    },
                    "required": ["id", "actions"],
                    "additionalProperties": False,
                },
            },
        }
