# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetStoreInfo(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], store_id) -> str:
        stores = data.get("stores", [])
        result = [item for item in stores if item["store_id"] == store_id]
        if result:
            return json.dumps(result[0])
        return json.dumps({"error": f"Store {store_id} not found"})
    @staticmethod
    def get_info() -> Dict[str, Any]:

        return {
            "type": "function",
            "function": {
                "name": "get_store_info",
                "description": "Tool function: get_store_info",
                "parameters": {
                    "type": "object",
                    "properties": {}
                }
            }
        }
