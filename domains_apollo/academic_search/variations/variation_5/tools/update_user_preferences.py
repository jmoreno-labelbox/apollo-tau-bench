from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class UpdateUserPreferences(Tool):
    """Utility for modifying a user's preferences."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: Any = None, notification_channel: Any = None, ui_theme: Any = None) -> str:
        user_id = user_id
        notification_channel = notification_channel
        ui_theme = ui_theme
        if not user_id or not (notification_channel or ui_theme):
            payload = {"error": "user_id and at least one preference to update are required."}
            out = json.dumps(payload)
            return out

        preferences = data.get("user_preferences", [])
        for pref in preferences:
            if pref.get("user_id") == user_id:
                if notification_channel:
                    pref["notification_channel"] = notification_channel
                if ui_theme:
                    pref["ui_theme"] = ui_theme
                payload = {"success": True, "updated_preferences": pref}
                out = json.dumps(payload)
                return out

        # Create one if no preferences are detected
        new_pref = {"preference_id": f"pref_{uuid.uuid4().hex[:4]}", "user_id": user_id}
        if notification_channel:
            new_pref["notification_channel"] = notification_channel
        if ui_theme:
            new_pref["ui_theme"] = ui_theme
        preferences.append(new_pref)
        payload = {"success": True, "created_preferences": new_pref}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateUserPreferences",
                "description": "Updates a user's preferences, such as notification channel or UI theme.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The user ID whose preferences to update.",
                        },
                        "notification_channel": {
                            "type": "string",
                            "description": "The preferred notification channel (e.g., 'email', 'in_app', 'none').",
                        },
                        "ui_theme": {
                            "type": "string",
                            "description": "The preferred UI theme (e.g., 'light', 'dark').",
                        },
                    },
                    "required": ["user_id"],
                },
            },
        }
