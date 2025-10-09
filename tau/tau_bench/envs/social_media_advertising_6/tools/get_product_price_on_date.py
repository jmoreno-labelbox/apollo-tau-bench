from tau_bench.envs.tool import Tool
import copy
import json
from typing import Any

class GetProductPriceOnDate(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], product_id: str, date: str) -> str:
        req = ["product_id", "date"]
        err = _require({"product_id": product_id, "date": date}, req)
        if err:
            return _fail(err)
        rows = _assert_table(data, "f_price")
        out = next(
            (
                r
                for r in rows
                if str(r.get("product_id")) == str(product_id)
                and r.get("date") == date
            ),
            None,
        )
        payload = out or {"error": "price_not_found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getProductPriceOnDate",
                "description": "Read f_price for a product on a date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {"type": "string"},
                        "date": {"type": "string"},
                    },
                    "required": ["product_id", "date"],
                },
            },
        }
