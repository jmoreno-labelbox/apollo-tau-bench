# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateTopicSubscription(Tool):
    """Updates a user's subscription to a research topic."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get('user_id')
        topic = kwargs.get('topic')
        action = kwargs.get('action')

        if not all([user_id, topic, action]):
            return json.dumps({"error": "user_id, topic, and action are required."})

        subscriptions = list(data.get('subscriptions', {}).values())

        if action.lower() == 'add':
            if any(sub.get('user_id') == user_id and sub.get('topic') == topic for sub in subscriptions):
                return json.dumps({"success": False, "message": "User is already subscribed to this topic."})

            new_sub_id = f"sub_topic_{uuid.uuid4().hex[:6]}"
            new_subscription = {"subscription_id": new_sub_id, "user_id": user_id, "topic": topic}
            subscriptions.append(new_subscription)
            return json.dumps({"success": True, "subscription": new_subscription})

        elif action.lower() == 'remove':
            initial_count = len(subscriptions)
            data['subscriptions'] = [sub for sub in subscriptions if not (sub.get('user_id') == user_id and sub.get('topic') == topic)]

            if len(data['subscriptions']) < initial_count:
                return json.dumps({"success": True, "message": f"Subscription to '{topic}' for user '{user_id}' removed."})
            else:
                return json.dumps({"error": "Subscription not found to remove."})

        else:
            return json.dumps({"error": "Invalid action. Must be 'add' or 'remove'."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_topic_subscription",
                "description": "Updates a user's subscription to a research topic (adds or removes).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "The ID of the user."},
                        "topic": {"type": "string", "description": "The research topic to subscribe to or unsubscribe from."},
                        "action": {"type": "string", "enum": ["add", "remove"], "description": "The action to perform."}
                    },
                    "required": ["user_id", "topic", "action"]
                }
            }
        }
