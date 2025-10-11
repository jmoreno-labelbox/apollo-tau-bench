# Copyright Sierra

import requests
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateAccessRequest(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], justification, requested_role_id, resource_id, user_id) -> str:
        requests = data.get('access_requests', [])
        new_id_num = max((int(r['request_id'][3:]) for r in requests), default=0) + 1
        new_request_id = f"AR-{new_id_num:03d}"
        new_request = {
                "request_id": new_request_id,
                "user_id": user_id,
                "resource_id": resource_id,
                "requested_role_id": requested_role_id,
                "justification": justification,
                "status": "PENDING",
                "submitted_at": NOW.strftime(DT_STR_FORMAT)
        }
        requests.append(new_request)
        data['access_requests'] = requests
        return json.dumps(new_request)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "create_access_request",
                        "description": "Creates a new access request.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "user_id": {"type": "string"},
                                        "resource_id": {"type": "string"},
                                        "requested_role_id": {"type": "string"},
                                        "justification": {"type": "string"}
                                },
                                "required": ["user_id", "requested_role_id", "justification"]
                        }
                }
        }
