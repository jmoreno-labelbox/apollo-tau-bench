# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetTotalAccountsCount(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        count = len(list(data.get("accounts", {}).values()))
        return json.dumps({"total_accounts": count})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_total_accounts_count",
                        "description": "Returns the current total number of accounts in the system.",
                        "parameters": {"type": "object", "properties": {}},
                },
        }
