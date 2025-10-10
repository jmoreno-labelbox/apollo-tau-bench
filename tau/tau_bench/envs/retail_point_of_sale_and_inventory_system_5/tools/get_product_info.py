# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetProductInfo(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        sku = kwargs.get("sku")
        products = list(data.get("products", {}).values())
        result = [item for item in products if item["sku"] == sku]
        if result:
            return json.dumps(result[0])
        return json.dumps({"error": f"Product {sku} not found"})
    @staticmethod
    def get_info() -> Dict[str, Any]:
