# Sierra Copyright

import uuid
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateUserPreferences(Tool):
    """Tool to update a user's preferences."""
    @staticmethod
    def invoke(data: Dict[str, Any], notification_channel, ui_theme, user_id) -> str:
        if not user_id or not (notification_channel or ui_theme):
            return json.dumps({"error": "user_id and at least one preference to update are required."})

        preferences = data.get('user_preferences', [])
        for pref in preferences:
            if pref.get('user_id') == user_id:
                if notification_channel:
                    pref['notification_channel'] = notification_channel
                if ui_theme:
                    pref['ui_theme'] = ui_theme
                return json.dumps({"success": True, "updated_preferences": pref})

        # If no preferences exist, generate a new one.
        new_pref = {"preference_id": f"pref_{uuid.uuid4().hex[:4]}", "user_id": user_id}
        if notification_channel:
            new_pref['notification_channel'] = notification_channel
        if ui_theme:
            new_pref['ui_theme'] = ui_theme
        preferences.append(new_pref)
        return json.dumps({"success": True, "created_preferences": new_pref})


    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_user_preferences",
                "description": "Updates a user's preferences, such as notification channel or UI theme.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "The user ID whose preferences to update."},
                        "notification_channel": {"type": "string", "description": "The preferred notification channel (e.g., 'email', 'in_app', 'none')."},
                        "ui_theme": {"type": "string", "description": "The preferred UI theme (e.g., 'light', 'dark')."}
                    },
                    "required": ["user_id"]
                }
            }
        }
