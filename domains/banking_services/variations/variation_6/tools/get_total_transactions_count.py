from tau_bench.envs.tool import Tool
import json
from datetime import date, datetime, time, timedelta, timezone
from typing import Any, Dict, List

class GetTotalTransactionsCount(Tool):
    def invoke(data: Dict[str, Any], unexpected: Any = None) -> str:
        count = len(data.get("transactions", []))
        return json.dumps({"total_transactions": count})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "getTotalTransactionsCount",
                        "description": "Returns the current total number of transactions in the system.",
                        "parameters": {"type": "object", "properties": {}},
                },
        }
