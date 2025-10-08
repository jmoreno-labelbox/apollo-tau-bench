from tau_bench.envs.tool import Tool
import json
import os
from datetime import datetime, timedelta
from typing import Any, Dict

class UpdateAccountPreferencesTool(Tool):
    """
    Tool to update customer account preferences such as notification settings and language.

    It searches all accounts linked to the specified customer and applies the given
    preferences, ensuring the input is valid and structured as a dictionary.

    Methods:
        invoke(data: Dict[str, Any], **kwargs) -> str:
            Updates account preferences for the customer if found.

        get_info() -> Dict[str, Any]:
            Describes the tool’s function and accepted parameters, including types.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, preferences: Dict[str, Any] = None, notifications_enabled: bool = None) -> str:
        # Support both preferences dict and direct parameters
        if preferences is None:
            preferences = {}
        if notifications_enabled is not None:
            preferences["notifications_enabled"] = notifications_enabled
            
        if not customer_id or not isinstance(preferences, dict):
            return json.dumps(
                {"error": "customer_id and preferences (dict) are required"}, indent=2
            )

        accounts = load_json("accounts.json")
        updated = False
        updated_prefs = {}

        for acc in accounts:
            if acc["customer_id"] == customer_id:
                acc["preferences"] = preferences
                updated_prefs = acc["preferences"]
                updated = True

        if not updated:
            return json.dumps({"error": "Customer account not found"}, indent=2)

        return json.dumps({"status": "updated", "preferences": updated_prefs}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAccountPreferences",
                "description": "Update the customer's notification, language, or communication preferences.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Customer ID"},
                        "preferences": {
                            "type": "object",
                            "properties": {
                                "notifications": {"type": "boolean"},
                                "language": {"type": "string"},
                            },
                            "required": ["notifications", "language"],
                        },
                    },
                    "required": ["customer_id", "preferences"],
                },
            },
        }
