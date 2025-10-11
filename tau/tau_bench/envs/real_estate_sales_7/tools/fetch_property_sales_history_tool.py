# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool








def _require_property_id(pid: str) -> Optional[str]:
    if not pid:
        return "property_id is required"
    if not HTX_RE.match(str(pid)):
        return f"property_id must match HTX### format, got {pid}"
    return None

def _err(msg: str, code: str = "bad_request", **extra) -> str:
    out = {"error": msg, "code": code}
    if extra:
        out.update(extra)
    return json.dumps(out, indent=2)

def _collect_sales_history(
    data: Dict[str, Any], property_id: str
) -> List[Dict[str, Any]]:
    return [
        s for s in data.get("sales", []) if str(s.get("property_id")) == property_id
    ]

class FetchPropertySalesHistoryTool(Tool):
    """Gets historical sales data for property."""

    @staticmethod
    def invoke(data: Dict[str, Any], property_id) -> str:
        need = _require_property_id(property_id)
        if need:
            return _err(need)

        sales = _collect_sales_history(data, property_id)
        out = {
            "property_id": property_id,
            "sales_history": sales or [],
            "total_sales": len(sales),
        }
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "fetch_property_sales_history",
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