from tau_bench.envs.tool import Tool
import json
from datetime import date, datetime, time, timedelta, timezone
from typing import Any, Dict, List

class GetTotalAccountsCount(Tool):
    def invoke(data: Dict[str, Any], unexpected: Any = None) -> str:
        count = len(data.get("accounts", []))
        return json.dumps({"total_accounts": count})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "getTotalAccountsCount",
                        "description": "Returns the current total number of accounts in the system.",
                        "parameters": {"type": "object", "properties": {}},
                },
        }
