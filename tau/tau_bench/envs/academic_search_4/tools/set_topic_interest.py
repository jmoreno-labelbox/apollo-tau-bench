# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SetTopicInterest(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        user_id, topic, action = kwargs.get('user_id'), kwargs.get('topic'), kwargs.get('action')
        if not all([user_id, topic, action]):
            return json.dumps({"error": "user_id, topic, and action are required."})

        subscriptions = list(data.get('subscriptions', {}).values())
        if action.lower() == 'add':
            if any(s.get('user_id') == user_id and s.get('topic') == topic for s in subscriptions):
                return json.dumps({"success": False, "message": "User is already subscribed to this topic."})
            new_sub = {"subscription_id": f"sub_topic_{uuid.uuid4().hex[:4]}", "user_id": user_id, "topic": topic}
            subscriptions.append(new_sub)
            return json.dumps({"success": True, "subscription": new_sub})
        elif action.lower() == 'remove':
            initial_count = len(subscriptions)
            data['subscriptions'] = [s for s in subscriptions if not (s.get('user_id') == user_id and s.get('topic') == topic)]
            if len(data['subscriptions']) < initial_count:
                return json.dumps({"success": True, "message": f"Subscription to topic '{topic}' removed."})
            else:
                return json.dumps({"error": "Subscription not found to remove."})
        else:
            return json.dumps({"error": "Invalid action. Must be 'add' or 'remove'."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "set_topic_interest", "description": "Sets a user's interest in a topic by adding or removing a subscription.", "parameters": {"type": "object", "properties": {"user_id": {"type": "string", "description": "The user ID."}, "topic": {"type": "string", "description": "The research topic."}, "action": {"type": "string", "enum": ["add", "remove"], "description": "The action to perform."}}, "required": ["user_id", "topic", "action"]}}}
