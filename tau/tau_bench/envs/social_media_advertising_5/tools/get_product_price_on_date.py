# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetProductPriceOnDate(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], date, product_id) -> str:
        pid = product_id
        d = date
        for r in list(data.get("f_price", {}).values()):
            if r.get("product_id") == pid and r.get("date") == d:
                return json.dumps(r)
        return json.dumps({"error": "price_not_found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "get_product_price_on_date", "description": "Gets product price on a date.",
                             "parameters": {"type": "object", "properties": {"product_id": {"type": "string"},
                                                                             "date": {"type": "string"}},
                                            "required": ["product_id", "date"]}}}
