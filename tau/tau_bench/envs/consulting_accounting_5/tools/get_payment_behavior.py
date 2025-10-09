from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any, Dict
from datetime import timedelta

class GetPaymentBehavior(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], publisher_id: str) -> str:
        """
        Returns payment_behavior_id(s) for a given publisher_id.
        """
        behaviors = [pb["behavior_id"] for pb in data["payment_behavior"].values() if pb["publisher_id"] == publisher_id]
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
