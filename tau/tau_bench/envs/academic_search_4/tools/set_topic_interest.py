from tau_bench.envs.tool import Tool
import json
import re
import uuid
from collections import Counter
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class SetTopicInterest(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, topic: str = None, action: str = None) -> str:
        if not all([user_id, topic, action]):
            payload = {"error": "user_id, topic, and action are required."}
            out = json.dumps(payload)
            return out

        subscriptions = data.get("subscriptions", [])
        if action.lower() == "add":
            if any(
                s.get("person_id") == user_id and s.get("topic") == topic
                for s in subscriptions
            ):
                payload = {
                        "success": False,
                        "message": "User is already subscribed to this topic.",
                    }
                out = json.dumps(
                    payload)
                return out
            new_sub = {
                "subscription_id": f"sub_topic_{uuid.uuid4().hex[:4]}",
                "user_id": user_id,
                "topic": topic,
            }
            subscriptions.append(new_sub)
            payload = {"success": True, "subscription": new_sub}
            out = json.dumps(payload)
            return out
        elif action.lower() == "remove":
            initial_count = len(subscriptions)
            data["subscriptions"] = [
                s
                for s in subscriptions
                if not (s.get("person_id") == user_id and s.get("topic") == topic)
            ]
            if len(data["subscriptions"]) < initial_count:
                payload = {
                        "success": True,
                        "message": f"Subscription to topic '{topic}' removed.",
                    }
                out = json.dumps(
                    payload)
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
                "name": "SetTopicInterest",
                "description": "Sets a user's interest in a topic by adding or removing a subscription.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "The user ID."},
                        "topic": {
                            "type": "string",
                            "description": "The research topic.",
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
