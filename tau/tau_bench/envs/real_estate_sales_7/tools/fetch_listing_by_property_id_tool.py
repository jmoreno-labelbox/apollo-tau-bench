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

def _latest(records: List[Dict[str, Any]], ts_key: str) -> Optional[Dict[str, Any]]:
    if not records:
        return None
    return max(records, key=lambda r: r.get(ts_key) or "")

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

def _collect_listing_by_property(
    data: Dict[str, Any], property_id: str
) -> Optional[Dict[str, Any]]:
    candidates = [
        l for l in data.get("listings", []) if str(l.get("property_id")) == property_id
    ]
    return _latest(candidates, "updated_at") or (candidates[0] if candidates else None)

class FetchListingByPropertyIdTool(Tool):
    """Gets listing information for specific property."""

    @staticmethod
    def invoke(data: Dict[str, Any], property_id) -> str:
        need = _require_property_id(property_id)
        if need:
            return _err(need)

        listing = _collect_listing_by_property(data, property_id)
        if not listing:
            # Validation rule for errors: verify sales against historical records.
            sales = _collect_sales_history(data, property_id)
            if not sales:
                return _err(
                    f"no listing or sales history for {property_id}", code="not_found"
                )
            # Generate a synthetic overview similar to a listing based on the most recent sale.
            srec = _latest(sales, "sale_date") or sales[0]
            out = {
                "listing_id": None,
                "property_id": property_id,
                "list_price": srec.get("sale_price"),
                "price_per_sqft": None,
                "status": "off_market",
                "listing_url": srec.get("source_url"),
                "street_view_url": None,
                "listed_at": srec.get("sale_date"),
                "updated_at": srec.get("sale_date"),
            }
            return json.dumps(out, indent=2)

        out = {
            "listing_id": listing.get("listing_id"),
            "property_id": property_id,
            "list_price": listing.get("list_price"),
            "price_per_sqft": listing.get("price_per_sqft"),
            "status": listing.get("status"),
            "listing_url": listing.get("listing_url"),
            "street_view_url": listing.get("street_view_url"),
            "listed_at": listing.get("listed_at"),
            "updated_at": listing.get("updated_at"),
        }
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "fetch_listing_by_property_id",
                "description": "Gets listing information for a property (HTX###).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "property_id": {"type": "string"},
                    },
                    "required": ["property_id"],
                },
            },
        }