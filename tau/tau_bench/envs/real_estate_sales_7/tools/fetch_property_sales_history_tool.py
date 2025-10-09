from tau_bench.envs.tool import Tool
import json
import math
import re
from typing import Any

class FetchPropertySalesHistoryTool(Tool):
    """Retrieves historical sales information for the property."""

    @staticmethod
    def invoke(data: dict[str, Any], property_id: str = None) -> str:
        need = _require_property_id(property_id)
        if need:
            return _err(need)

        sales = _collect_sales_history(data, property_id)
        out = {
            "property_id": property_id,
            "sales_history": sales or [],
            "total_sales": len(sales),
        }
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FetchPropertySalesHistory",
                "description": "Gets historical sales data for a property.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "property_id": {"type": "string"},
                    },
                    "required": ["property_id"],
                },
            },
        }
