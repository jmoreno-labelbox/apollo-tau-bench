# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUserSubscriptions(Tool):
    """Tool to get a user's topic subscriptions."""
    @staticmethod
    def invoke(data: Dict[str, Any], user_id) -> str:
        if not user_id:
            return json.dumps({"error": "user_id is required."})

        subscriptions = list(data.get('subscriptions', {}).values())
        user_subs = [sub for sub in subscriptions if sub.get('user_id') == user_id]
        return json.dumps(user_subs, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_user_subscriptions",
                "description": "Retrieves the list of topics a specific user is subscribed to.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "The ID of the user whose subscriptions to retrieve."}
                    },
                    "required": ["user_id"]
                }
            }
        }
