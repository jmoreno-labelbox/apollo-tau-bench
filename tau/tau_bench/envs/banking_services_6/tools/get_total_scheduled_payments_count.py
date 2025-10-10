# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetTotalScheduledPaymentsCount(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        count = len(data.get("scheduled_payments", []))
        return json.dumps({"total_scheduled_payments": count})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_total_scheduled_payments_count",
                        "description": "Returns the current total number of scheduled payments in the system.",
                        "parameters": {"type": "object", "properties": {}},
                },
        }
