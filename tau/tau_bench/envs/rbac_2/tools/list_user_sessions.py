# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListUserSessions(Tool):
    """ Find all recent login sessions for a specific user. """

    @staticmethod
    def invoke(data: Dict[str, Any], user_id) -> str:
        user_id_to_find = user_id
        try:
            all_sessions = data.get('sessions', [])
        except:
            all_sessions = []

        user_sessions = [
            session for session in all_sessions
            if session.get("user_id") == user_id_to_find
        ]

        return json.dumps(user_sessions)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_user_sessions",
                "description": "Retrieves a list of all recent login sessions for a specific user by their user ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The unique ID of the user whose sessions are to be retrieved."
                        }
                    },
                    "required": ["user_id"]
                }
            }
        }
