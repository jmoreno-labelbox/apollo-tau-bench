# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListStoreEmployees(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        store_id = kwargs.get("store_id")
        employees = list(data.get("employees", {}).values())
        result = [item for item in employees if item["store_id"] == store_id]
        return json.dumps(result, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:

        return {
            "type": "function",
            "function": {
                "name": "list_store_employees",
                "description": "Tool function: list_store_employees",
                "parameters": {
                    "type": "object",
                    "properties": {}
                }
            }
        }
