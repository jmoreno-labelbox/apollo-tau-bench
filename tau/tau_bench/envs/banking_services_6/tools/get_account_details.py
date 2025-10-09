from tau_bench.envs.tool import Tool
import json
from datetime import date, datetime, time, timedelta, timezone
from typing import Any, Dict, List

class GetAccountDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None) -> str:
        account = next((a for a in data['accounts'] if a['account_id'] == account_id), None)
        if account:
            return json.dumps(account)
        return json.dumps({"error": "Account not found"})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "GetAccountDetails",
                        "description": "Retrieves full details for a specific account.",
                        "parameters": {
                                "type": "object",
                                "properties": {"account_id": {"type": "string"}},
                                "required": ["account_id"]
                        }
                }
        }
