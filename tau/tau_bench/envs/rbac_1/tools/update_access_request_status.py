# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateAccessRequestStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], request_id, reviewed_by, status) -> str:
        new_status = status
        for req in data.get('access_requests', []):
            if req.get('request_id') == request_id:
                req['status'] = new_status
                req['reviewed_by'] = reviewed_by
                req['decision_at'] = NOW.strftime(DT_STR_FORMAT)
                return json.dumps(req)
        return json.dumps({"error": "Access request not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "update_access_request_status",
                        "description": "Updates the status of an access request.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "request_id": {"type": "string"},
                                        "status": {"type": "string"},
                                        "reviewed_by": {"type": "string"}
                                },
                                "required": ["request_id", "status", "reviewed_by"]
                        }
                }
        }
