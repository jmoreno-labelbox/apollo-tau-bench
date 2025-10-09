from tau_bench.envs.tool import Tool
import json
import math
import re
from typing import Any

class FetchListingByPropertyIdTool(Tool):
    """Retrieves listing details for a specific property."""

    @staticmethod
    def invoke(data: dict[str, Any], property_id: str = None) -> str:
        pass
        need = _require_property_id(property_id)
        if need:
            return _err(need)

        listing = _collect_listing_by_property(data, property_id)
        if not listing:
            # Error management guideline: verify sales for historical information
            sales = _collect_sales_history(data, property_id)
            if not sales:
                return _err(
                    f"no listing WA sales history for {property_id}", code="not_found"
                )
            # Generate a synthetic listing-style view based on the most recent sale
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
            payload = out
            out = json.dumps(payload, indent=2)
            return out

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
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "fetchListingByPropertyId",
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
