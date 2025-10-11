# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListStoreSKUs(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], store_id) -> str:
        inventory = list(data.get("inventory", {}).values())
        result = [item["sku"] for item in inventory if item["store_id"] == store_id]
        return json.dumps(result, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:

        return {
            "type": "function",
            "function": {
                "name": "list_store_sk_us",
                "description": "Tool function: list_store_sk_us",
                "parameters": {
                    "type": "object",
                    "properties": {}
                }
            }
        }
