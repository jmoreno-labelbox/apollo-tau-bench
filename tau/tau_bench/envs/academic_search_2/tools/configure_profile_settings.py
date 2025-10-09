from tau_bench.envs.tool import Tool
import json
import uuid
from collections import Counter
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ConfigureProfileSettings(Tool):
    """Sets up a user's profile preferences."""

    @staticmethod
    def invoke(data: dict[str, Any], *, user_id: Any = None, notification_channel: Any = None, ui_theme: Any = None) -> str:
        user_id = user_id
        notification_channel = notification_channel
        ui_theme = ui_theme

        if not user_id:
            payload = {"error": "user_id is required to configure settings."}
            out = json.dumps(payload)
            return out

        if not notification_channel and not ui_theme:
            payload = {
                    "error": "At least one setting (notification_channel or ui_theme) must be provided."
                }
            out = json.dumps(
                payload)
            return out

        preferences = data.get("user_preferences", [])

        user_pref = next(
            (pref for pref in preferences if pref.get("user_id") == user_id), None
        )

        if user_pref:
            if notification_channel:
                user_pref["notification_channel"] = notification_channel
            if ui_theme:
                user_pref["ui_theme"] = ui_theme
            payload = {"success": True, "configured_settings": user_pref}
            out = json.dumps(payload)
            return out
        else:
            new_pref = {
                "preference_id": f"pref_{uuid.uuid4().hex[:4]}",  #Generate a unique ID
                "user_id": user_id,
                "notification_channel": notification_channel,
                "ui_theme": ui_theme,
            }
            if not notification_channel:
                del new_pref["notification_channel"]
            if not ui_theme:
                del new_pref["ui_theme"]

            preferences.append(new_pref)
            data["user_preferences"] = (
                preferences  #Ensures that the updated list is saved back to 'data'
            )
            payload = {"success": True, "configured_settings": new_pref}
            out = json.dumps(payload)
            return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ConfigureProfileSettings",
                "description": "Configures a user's profile settings, such as notification channel or UI theme. Creates a new preference entry if one does not exist for the user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the user whose settings are being configured.",
                        },
                        "notification_channel": {
                            "type": "string",
                            "description": "The new notification channel (e.g., 'email', 'in_app').",
                        },
                        "ui_theme": {
                            "type": "string",
                            "description": "The new UI theme (e.g., 'dark', 'light').",
                        },
                    },
                    "required": ["user_id"],
                },
            },
        }
