# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ConfigureProfileSettings(Tool):
    """Configures a user's profile settings."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get('user_id')
        notification_channel = kwargs.get('notification_channel')
        ui_theme = kwargs.get('ui_theme')

        if not user_id:
            return json.dumps({"error": "user_id is required to configure settings."})

        if not notification_channel and not ui_theme:
            return json.dumps({"error": "At least one setting (notification_channel or ui_theme) must be provided."})

        preferences = data.get('user_preferences', [])

        user_pref = next((pref for pref in preferences if pref.get('user_id') == user_id), None)

        if user_pref:
            if notification_channel:
                user_pref['notification_channel'] = notification_channel
            if ui_theme:
                user_pref['ui_theme'] = ui_theme
            return json.dumps({"success": True, "configured_settings": user_pref})
        else:
            new_pref = {
                "preference_id": f"pref_{uuid.uuid4().hex[:4]}", # Gera um ID único
                "user_id": user_id,
                "notification_channel": notification_channel,
                "ui_theme": ui_theme
            }
            if not notification_channel:
                del new_pref['notification_channel']
            if not ui_theme:
                del new_pref['ui_theme']

            preferences.append(new_pref)
            data['user_preferences'] = preferences # Garante que a lista atualizada seja salva de volta no 'data'
            return json.dumps({"success": True, "configured_settings": new_pref})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "configure_profile_settings",
                "description": "Configures a user's profile settings, such as notification channel or UI theme. Creates a new preference entry if one does not exist for the user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "The ID of the user whose settings are being configured."},
                        "notification_channel": {"type": "string", "description": "The new notification channel (e.g., 'email', 'in_app')."},
                        "ui_theme": {"type": "string", "description": "The new UI theme (e.g., 'dark', 'light')."}
                    },
                    "required": ["user_id"]
                }
            }
        }
