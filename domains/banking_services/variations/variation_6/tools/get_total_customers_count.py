from tau_bench.envs.tool import Tool
import json
from datetime import date, datetime, time, timedelta, timezone
from typing import Any, Dict, List

class GetTotalCustomersCount(Tool):
    def invoke(data: Dict[str, Any], unexpected: Any = None) -> str:
        count = len(data.get("customers", []))
        return json.dumps({"total_customers": count})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "getTotalCustomersCount",
                        "description": "Returns the current total number of customers in the system.",
                        "parameters": {"type": "object", "properties": {}},
                },
        }
