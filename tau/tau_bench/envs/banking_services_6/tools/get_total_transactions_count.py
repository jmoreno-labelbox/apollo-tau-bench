# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetTotalTransactionsCount(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        count = len(list(data.get("transactions", {}).values()))
        return json.dumps({"total_transactions": count})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_total_transactions_count",
                        "description": "Returns the current total number of transactions in the system.",
                        "parameters": {"type": "object", "properties": {}},
                },
        }
