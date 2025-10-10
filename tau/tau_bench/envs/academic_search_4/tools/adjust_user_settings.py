# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AdjustUserSettings(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get('user_id')
        if not user_id:
            return json.dumps({"error": "user_id is required."})

        notification_channel = kwargs.get('notification_channel')
        ui_theme = kwargs.get('ui_theme')
        research_field = kwargs.get('research_field')

        if not notification_channel and not ui_theme and not research_field:
            return json.dumps({"error": "At least one setting (notification_channel, ui_theme, or research_field) must be provided."})

        preferences = data.get('user_preferences', [])

        pref_found = False
        for pref in preferences:
            if pref.get('user_id') == user_id:
                if notification_channel:
                    pref['notification_channel'] = notification_channel
                if ui_theme:
                    pref['ui_theme'] = ui_theme
                pref_found = True
                break

        if not pref_found:
            new_pref = {
                "preference_id": f"pref_{uuid.uuid4().hex[:4]}",
                "user_id": user_id,
                "notification_channel": notification_channel if notification_channel else "none", # Default value
                "preferred_email": "", # Assuming an empty default
                "ui_theme": ui_theme if ui_theme else "light" # Default value
            }
            data['user_preferences'].append(new_pref)
            pref = new_pref
            pref_found = True

        user_obj = None
        for user in list(data.get('users', {}).values()):
            if user.get('user_id') == user_id:
                if research_field:
                    user['research_field'] = research_field
                user_obj = user
                break

        if pref_found or user_obj:
            if research_field and user_obj: # Se research_field foi modificado, retorna o objeto user
                return json.dumps({"success": True, "user": user_obj})
            elif pref_found: # Senão, retorna as preferências (se foram modificadas/criadas)
                return json.dumps({"success": True, "settings": pref})

        return json.dumps({"error": f"Settings for user ID '{user_id}' not found and could not be created."})


    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "adjust_user_settings","description": "Adjusts a user's personal settings.","parameters": {"type": "object","properties": {"user_id": {"type": "string","description": "The user ID for whom to adjust settings."}, "notification_channel": {"type": "string","description": "The new notification channel (e.g., 'email', 'in_app', 'none')."}, "ui_theme": {"type": "string","description": "The new UI theme (e.g., 'dark', 'light')."}, "research_field": {"type": "string", "description": "The new primary research field for the user."}},"required": ["user_id"]}}}
