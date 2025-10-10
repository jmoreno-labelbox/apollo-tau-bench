# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetPaymentBehavior(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Returns payment_behavior_id(s) for a given publisher_id.
        """
        publisher_id = kwargs["publisher_id"]
        behaviors = [pb["behavior_id"] for pb in data["payment_behavior"] if pb["publisher_id"] == publisher_id]
        return json.dumps(behaviors)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetPaymentBehavior",
                "description": "Retrieve payment_behavior_id(s) for a given publisher_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "publisher_id": {"type": "string", "description": "Publisher ID to fetch payment behavior"}
                    },
                    "required": ["publisher_id"],
                },
            },
        }
