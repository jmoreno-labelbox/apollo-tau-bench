from tau_bench.envs.tool import Tool
import json
from datetime import date, datetime, time, timedelta, timezone
from typing import Any, Dict, List

class GetTotalLoansCount(Tool):
    def invoke(data: Dict[str, Any], unexpected: Any = None) -> str:
        count = len(data.get("loans", []))
        return json.dumps({"total_loans": count})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "getTotalLoansCount",
                        "description": "Returns the current total number of loans in the system.",
                        "parameters": {"type": "object", "properties": {}},
                },
        }
