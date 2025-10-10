# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAccessRequestDetailsTool(Tool):
    """get_access_request_details: richer alias for getting AR details."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        return GetAccessRequestTool.invoke(data, **kwargs)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_access_request_details",
                "description": "Return detailed access request info by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"request_id": {"type": "string"}},
                    "required": ["request_id"],
                },
            },
        }
