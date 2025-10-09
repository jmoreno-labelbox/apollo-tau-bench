from tau_bench.envs.tool import Tool
import json
from datetime import date, datetime, time, timedelta, timezone
from typing import Any, Dict, List

class GetTotalSupportTicketsCount(Tool):
    def invoke(data: Dict[str, Any], unexpected: Any = None) -> str:
        count = len(data.get("support_tickets", []))
        return json.dumps({"total_support_tickets": count})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "getTotalSupportTicketsCount",
                        "description": "Returns the current total number of support tickets in the system.",
                        "parameters": {"type": "object", "properties": {}},
                },
        }
