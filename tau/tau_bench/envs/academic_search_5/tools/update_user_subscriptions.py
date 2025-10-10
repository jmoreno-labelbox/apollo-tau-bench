# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateUserSubscriptions(Tool):
    """Tool to add or remove a topic subscription for a user."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id = kwargs.get('user_id')
        topic = kwargs.get('topic')
        action = kwargs.get('action', 'add')  # 'include' or 'exclude'
        if not user_id or not topic:
            return json.dumps({"error": "user_id and topic are required."})

        subscriptions = list(data.get('subscriptions', {}).values())
        if action.lower() == 'add':
            # Verify if the subscription is already present.
            for sub in subscriptions:
                if sub.get('user_id') == user_id and sub.get('topic', '').lower() == topic.lower():
                    return json.dumps({"success": True, "message": "User is already subscribed to this topic."})
            new_sub = {
                "subscription_id": f"sub_topic_{uuid.uuid4().hex[:4]}",
                "user_id": user_id,
                "topic": topic
            }
            subscriptions.append(new_sub)
            return json.dumps({"success": True, "subscription": new_sub})
        elif action.lower() == 'remove':
            initial_len = len(subscriptions)
            data['subscriptions'] = [
                sub for sub in subscriptions
                if not (sub.get('user_id') == user_id and sub.get('topic', '').lower() == topic.lower())
            ]
            if len(data['subscriptions']) < initial_len:
                return json.dumps({"success": True, "message": f"Subscription to topic '{topic}' removed for user {user_id}."})
            else:
                return json.dumps({"error": "Subscription not found."})
        else:
            return json.dumps({"error": "Invalid action. Must be 'add' or 'remove'."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_user_subscriptions",
                "description": "Adds or removes a topic subscription for a user.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "The user ID to update."},
                        "topic": {"type": "string", "description": "The topic to subscribe or unsubscribe from (e.g., 'AI')."},
                        "action": {"type": "string", "description": "The action to perform: 'add' or 'remove'. Defaults to 'add'."}
                    },
                    "required": ["user_id", "topic"]
                }
            }
        }
