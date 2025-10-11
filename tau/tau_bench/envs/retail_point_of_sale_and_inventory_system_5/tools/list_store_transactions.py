# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListStoreTransactions(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], store_id) -> str:
        transactions = list(data.get("transactions", {}).values())
        result = [item for item in transactions if item["store_id"] == store_id]
        return json.dumps(result, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:

        return {
            "type": "function",
            "function": {
                "name": "list_store_transactions",
                "description": "Tool function: list_store_transactions",
                "parameters": {
                    "type": "object",
                    "properties": {}
                }
            }
        }
