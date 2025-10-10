# Sierra copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListInactiveUsers(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        inactive_since_str = kwargs.get("inactive_since")
        inactive_since_dt = datetime.strptime(inactive_since_str, DT_STR_FORMAT)

        active_user_ids = {session['user_id'] for session in data.get('user_sessions', []) if datetime.strptime(session['end_time'], DT_STR_FORMAT) >= inactive_since_dt}

        all_user_ids = {user['user_id'] for user in list(data.get('users', {}).values())}
        inactive_user_ids = list(all_user_ids - active_user_ids)

        return json.dumps({"inactive_users": inactive_user_ids})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "list_inactive_users",
                        "description": "Lists users who have not had a session since the specified date.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "inactive_since": {"type": "string", "description": "The date in ISO 8601 format (e.g., '2025-05-01T00:00:00Z')."}
                                },
                                "required": ["inactive_since"]
                        }
                }
        }
