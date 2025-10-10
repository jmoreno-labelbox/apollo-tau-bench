# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FetchListingsByIdsTool(Tool):
    """Fetches listings for multiple property_ids, with sales fallback when missing."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        ids = kwargs.get("property_ids") or []
        if not isinstance(ids, list) or not ids:
            return _err("property_ids must be a non-empty array")

        listings_map = {str(l.get("property_id")): l for l in list(data.get("listings", {}).values())}
        out_items: List[Dict[str, Any]] = []
        for pid in [str(x) for x in ids]:
            l = listings_map.get(pid)
            if l:
                out_items.append(
                    {
                        "listing_id": l.get("listing_id"),
                        "property_id": pid,
                        "list_price": l.get("list_price"),
                        "price_per_sqft": l.get("price_per_sqft"),
                        "status": l.get("status"),
                        "listing_url": l.get("listing_url"),
                        "street_view_url": l.get("street_view_url"),
                        "listed_at": l.get("listed_at"),
                        "updated_at": l.get("updated_at"),
                    }
                )
            else:
                sales = _collect_sales_history(data, pid)
                if sales:
                    srec = _latest(sales, "sale_date") or sales[0]
                    out_items.append(
                        {
                            "listing_id": None,
                            "property_id": pid,
                            "list_price": srec.get("sale_price"),
                            "price_per_sqft": None,
                            "status": "off_market",
                            "listing_url": srec.get("source_url"),
                            "street_view_url": None,
                            "listed_at": srec.get("sale_date"),
                            "updated_at": srec.get("sale_date"),
                        }
                    )
                else:
                    out_items.append(
                        {"listing_id": None, "property_id": pid, "error": "not_found"}
                    )

        out = {"results": out_items, "requested": len(ids)}
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "fetch_listings_by_ids",
                "description": (
                    "Fetch multiple listings by property_ids; synthesize from sales when listing is missing."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "property_ids": {"type": "array", "items": {"type": "string"}}
                    },
                    "required": ["property_ids"],
                },
            },
        }
