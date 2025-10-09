from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class ManageUserSubscriptions(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: Any = None, topic: Any = None, action: Any = None) -> str:
        """
        Modifies a user's subscription to a topic by adding or removing it.
        - Needs user_id, topic, and action ('add' or 'remove').
        """
        if not all([user_id, topic, action]):
            payload = {"error": "user_id, topic, and action are required."}
            out = json.dumps(payload)
            return out

        subscriptions = data.get("subscriptions", [])

        if action.lower() == "add":
            already_subscribed = any(
                sub.get("person_id") == user_id and sub.get("subject") == topic
                for sub in subscriptions
            )
            if already_subscribed:
                payload = {
                    "success": False,
                    "message": "User is already subscribed to this topic.",
                }
                out = json.dumps(payload)
                return out

            new_sub_id = f"sub_topic_{uuid.uuid4().hex[:6]}"
            new_subscription = {
                "membership_id": new_sub_id,
                "person_id": user_id,
                "subject": topic,
            }
            subscriptions.append(new_subscription)
            payload = {"success": True, "subscription": new_subscription}
            out = json.dumps(payload)
            return out

        elif action.lower() == "remove":
            initial_count = len(subscriptions)
            # Generate a new list that omits the subscription intended for removal.
            data["subscriptions"] = [
                sub
                for sub in subscriptions
                if not (sub.get("person_id") == user_id and sub.get("subject") == topic)
            ]

            if len(data["subscriptions"]) < initial_count:
                payload = {
                    "success": True,
                    "message": f"Subscription to topic '{topic}' for user '{user_id}' removed.",
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
        """
        Provides the function schema intended for the language model.
        """
        pass
        return {
            "type": "function",
            "function": {
                "name": "ManageUserSubscriptions",
                "description": "Adds or removes a user's subscription to a specific topic.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the user.",
                        },
                        "topic": {
                            "type": "string",
                            "description": "The topic to subscribe to or unsubscribe from.",
                        },
                        "action": {
                            "type": "string",
                            "enum": ["add", "remove"],
                            "description": "The action to perform: 'add' or 'remove' the subscription.",
                        },
                    },
                    "required": ["user_id", "topic", "action"],
                },
            },
        }
