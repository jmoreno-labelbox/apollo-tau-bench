# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUserSessions(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], user_id) -> str:
        user_sessions = [
                s for s in data.get('sessions', []) if s.get('user_id') == user_id
        ]
        user_sessions.sort(key=lambda x: x['start_time'], reverse=True)
        return json.dumps({"sessions": user_sessions})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_user_sessions",
                        "description": "Retrieves recent session information for a user.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "user_id": {"type": "string"}
                                },
                                "required": ["user_id"]
                        }
                }
        }
