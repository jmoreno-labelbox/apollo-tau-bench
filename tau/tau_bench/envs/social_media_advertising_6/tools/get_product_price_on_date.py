# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetProductPriceOnDate(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], date, product_id) -> str:
        req = ["product_id", "date"]
        err = _require(kwargs, req)
        if err: return _fail(err)
        rows = _assert_table(data, "f_price")
        out = next((r for r in rows if
                    str(r.get("product_id")) == str(product_id) and r.get("date") == date), None)
        return json.dumps(out or {"error": "price_not_found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_product_price_on_date",
                                                 "description": "Read f_price for a product on a date.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"product_id": {"type": "string"},
                                                                               "date": {"type": "string"}},
                                                                "required": ["product_id", "date"]}}}
