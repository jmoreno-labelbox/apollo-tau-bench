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

class FetchPropertyDetailsTool(Tool):
    """Consolidate listing, sales history, and open house info for a property."""

    @staticmethod
    def invoke(data: Dict[str, Any], property_id) -> str:
        need = _require_property_id(property_id)
        if need:
            return _err(need)

        listing = _collect_listing_by_property(data, property_id)
        sales_history = _collect_sales_history(data, property_id)
        latest_sale = _latest(sales_history, "sale_date") if sales_history else None

        # Enable windows for this property.
        open_houses = [
            oh
            for oh in data.get("open_houses", [])
            if str(oh.get("property_id")) == str(property_id)
        ]
        open_houses_sorted = sorted(
            open_houses, key=lambda oh: (oh.get("start_at") or "")
        )

        if not listing and not sales_history:
            return _err(f"no data available for {property_id}", code="not_found")

        status = listing.get("status") if listing else "off_market"
        list_price = (listing or {}).get("list_price") or (
            (latest_sale or {}).get("sale_price")
        )
        ppsf = (listing or {}).get("price_per_sqft")
        listing_url = (listing or {}).get("listing_url") or (
            (latest_sale or {}).get("source_url")
        )
        street_view_url = (listing or {}).get("street_view_url")

        listing_out = None
        if listing:
            listing_out = {
                "listing_id": listing.get("listing_id"),
                "list_price": listing.get("list_price"),
                "price_per_sqft": listing.get("price_per_sqft"),
                "status": listing.get("status"),
                "listing_url": listing.get("listing_url"),
                "street_view_url": listing.get("street_view_url"),
                "listed_at": listing.get("listed_at"),
                "updated_at": listing.get("updated_at"),
            }

        out = {
            "property_id": property_id,
            "status": status,
            "list_price": list_price,
            "price_per_sqft": ppsf,
            "links": {"listing_url": listing_url, "street_view_url": street_view_url},
            "listing": listing_out,
            "latest_sale": latest_sale,
            "sales_history_count": len(sales_history),
            "open_house_windows": open_houses_sorted[:10],
        }
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "fetch_property_details",
                "description": (
                    "Get consolidated details (listing, sales, open houses) for a property."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {"property_id": {"type": "string"}},
                    "required": ["property_id"],
                },
            },
        }