# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCustomerInfo(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get("customer_id")
        customers = list(data.get("customers", {}).values())
        result = [item for item in customers if item["customer_id"] == customer_id]
        if result:
            return json.dumps(result[0])
        return json.dumps({"error": f"Customer {customer_id} not found"})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_customer_info", "parameters": {"customer_id": {"type": "string"}}, "required": ["customer_id"]}}
