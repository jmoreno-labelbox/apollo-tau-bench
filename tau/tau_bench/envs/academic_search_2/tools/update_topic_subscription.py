from tau_bench.envs.tool import Tool
import json
import uuid
from collections import Counter
from datetime import datetime
from typing import Any

class UpdateTopicSubscription(Tool):
    """Modifies a user's subscription to a research area."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: Any = None, topic: Any = None, action: Any = None) -> str:
        if not all([user_id, topic, action]):
            payload = {"error": "user_id, topic, and action are required."}
            out = json.dumps(payload)
            return out

        subscriptions = data.get("subscriptions", [])

        if action.lower() == "add":
            if any(
                sub.get("user_id") == user_id and sub.get("topic") == topic
                for sub in subscriptions
            ):
                payload = {
                    "success": False,
                    "message": "User is already subscribed to this topic.",
                }
                out = json.dumps(payload)
                return out

            new_sub_id = f"sub_topic_{uuid.uuid4().hex[:6]}"
            new_subscription = {
                "subscription_id": new_sub_id,
                "user_id": user_id,
                "topic": topic,
            }
            subscriptions.append(new_subscription)
            payload = {"success": True, "subscription": new_subscription}
            out = json.dumps(payload)
            return out

        elif action.lower() == "remove":
            initial_count = len(subscriptions)
            data["subscriptions"] = [
                sub
                for sub in subscriptions
                if not (sub.get("user_id") == user_id and sub.get("topic") == topic)
            ]

            if len(data["subscriptions"]) < initial_count:
                payload = {
                    "success": True,
                    "message": f"Subscription to '{topic}' for user '{user_id}' removed.",
                }
                out = json.dumps(payload)
                return out
            else:
                payload = {"error": "Subscription not found to remove."}
                out = json.dumps(payload)
                return out

        else:
            payload = {"error": "Invalid action. Must be 'add' or 'remove'."}
            out = json.dumps(payload)
            return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateTopicSubscription",
                "description": "Updates a user's subscription to a research topic (adds or removes).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the user.",
                        },
                        "topic": {
                            "type": "string",
                            "description": "The research topic to subscribe to or unsubscribe from.",
                        },
                        "action": {
                            "type": "string",
                            "enum": ["add", "remove"],
                            "description": "The action to perform.",
                        },
                    },
                    "required": ["user_id", "topic", "action"],
                },
            },
        }
