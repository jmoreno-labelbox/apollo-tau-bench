from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any
from datetime import datetime, timedelta

class GetAccessRequestDetailsTool(Tool):
    """GetAccessRequest_details: enhanced alias for retrieving AR details."""

    @staticmethod
    def invoke(data: dict[str, Any],
    request_id: Any = None,
    ) -> str:
        return GetAccessRequestTool.invoke(data)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAccessRequestDetails",
                "description": "Return detailed access request info by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"request_id": {"type": "string"}},
                    "required": ["request_id"],
                },
            },
        }
