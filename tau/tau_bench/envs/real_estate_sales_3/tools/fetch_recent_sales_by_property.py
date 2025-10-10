# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FetchRecentSalesByProperty(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        property_id = kwargs.get("property_id")
        limit = int(kwargs.get("limit", 3))
        sales = [s for s in data.get("sales", []) if s.get("property_id") == property_id]
        sales = sorted(sales, key=lambda s: s.get("sale_date") or "", reverse=True)[:limit]
        return json.dumps({"property_id": property_id, "sales": sales}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"fetch_recent_sales_by_property",
            "description":"Return up to N recent sales rows for a property.",
            "parameters":{"type":"object","properties":{"property_id":{"type":"string"},"limit":{"type":"integer"}},"required":["property_id"]}
        }}
