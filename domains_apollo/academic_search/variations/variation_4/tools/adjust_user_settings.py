from tau_bench.envs.tool import Tool
import json
import re
import uuid
from collections import Counter
from datetime import datetime
from typing import Any

class AdjustUserSettings(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], *, user_id: Any = None, notification_channel: Any = None, ui_theme: Any = None, research_field: Any = None) -> str:
        user_id = user_id
        if not user_id:
            payload = {"error": "user_id is required."}
            out = json.dumps(payload)
            return out

        notification_channel = notification_channel
        ui_theme = ui_theme
        research_field = research_field

        if not notification_channel and not ui_theme and not research_field:
            payload = {
                    "error": "At least one setting (notification_channel, ui_theme, or research_field) must be provided."
                }
            out = json.dumps(
                payload)
            return out

        preferences = data.get("user_preferences", [])

        pref_found = False
        for pref in preferences:
            if pref.get("person_id") == user_id:
                if notification_channel:
                    pref["notification_channel"] = notification_channel
                if ui_theme:
                    pref["ui_theme"] = ui_theme
                pref_found = True
                break

        if not pref_found:
            new_pref = {
                "preference_id": f"pref_{uuid.uuid4().hex[:4]}",
                "user_id": user_id,
                "notification_channel": (
                    notification_channel if notification_channel else "none"
                ),  #Initial value
                "preferred_email": "",  #Presuming a blank default
                "ui_theme": ui_theme if ui_theme else "light",  #Initial value
            }
            if "user_preferences" not in data:
                data["user_preferences"] = []
            data["user_preferences"].append(new_pref)
            pref = new_pref
            pref_found = True

        user_obj = None
        for user in data.get("users", []):
            if user.get("person_id") == user_id:
                if research_field:
                    user["research_field"] = research_field
                user_obj = user
                break

        if pref_found or user_obj:
            if (
                research_field and user_obj
            ):  #If research_field has been changed, return the user object
                payload = {"success": True, "user": user_obj}
                out = json.dumps(payload)
                return out
            elif (
                pref_found
            ):  #Otherwise, return the preferences (if they have been altered/created)
                payload = {"success": True, "settings": pref}
                out = json.dumps(payload)
                return out
        payload = {
                "error": f"Settings for user ID '{user_id}' not found and could not be created."
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AdjustUserSettings",
                "description": "Adjusts a user's personal settings.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The user ID for whom to adjust settings.",
                        },
                        "notification_channel": {
                            "type": "string",
                            "description": "The new notification channel (e.g., 'email', 'in_app', 'none').",
                        },
                        "ui_theme": {
                            "type": "string",
                            "description": "The new UI theme (e.g., 'dark', 'light').",
                        },
                        "research_field": {
                            "type": "string",
                            "description": "The new primary research field for the user.",
                        },
                    },
                    "required": ["user_id"],
                },
            },
        }
