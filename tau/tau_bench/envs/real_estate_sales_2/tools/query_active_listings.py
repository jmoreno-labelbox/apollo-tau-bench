# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class QueryActiveListings(Tool):
    """Filter and return active listings by given constraints."""

    @staticmethod
    def _by_key(rows: List[Dict[str, Any]], key: str) -> Dict[Any, Dict[str, Any]]:
        return {r.get(key): r for r in rows or []}

    @staticmethod
    def invoke(data: Dict[str, Any], baths, beds, neighborhood_ids, price_max, price_min, property_type, sqft_max, sqft_min, limit = 15) -> str:
        price_min: Optional[float] = price_min
        price_max: Optional[float] = price_max
        beds: Optional[int] = beds
        baths: Optional[int] = baths
        sqft_min: Optional[int] = sqft_min
        sqft_max: Optional[int] = sqft_max
        property_type: Optional[str] = property_type
        limit: int = limit

        neighborhoods = set(neighborhood_ids or [])
        props = QueryActiveListings._by_key(list(data.get("properties", {}).values()), "property_id")
        listings = (data.get("listings") or [])

        def within(val: Optional[float], lo: Optional[float], hi: Optional[float]) -> bool:
            v = 0 if val is None else val
            if lo is not None and v < lo:
                return False
            if hi is not None and v > hi:
                return False
            return True

        def matches(pr: Dict[str, Any], lst: Dict[str, Any]) -> bool:
            return (
                lst.get("status") == "active"
                and (not neighborhoods or pr.get("neighborhood_id") in neighborhoods)
                and (property_type is None or pr.get("property_type") == property_type)
                and (beds is None or pr.get("beds") == beds)
                and (baths is None or pr.get("baths") == baths)
                and within(lst.get("list_price", 0), price_min, price_max)
                and within(pr.get("sqft", 0), sqft_min, sqft_max)
            )

        result_iter = (
            {
                "listing_id": lst.get("listing_id"),
                "property_id": pr.get("property_id"),
                "neighborhood_id": pr.get("neighborhood_id"),
                "list_price": lst.get("list_price"),
                "property_type": pr.get("property_type"),
                "beds": pr.get("beds"),
                "baths": pr.get("baths"),
                "sqft": pr.get("sqft"),
                "listing_url": lst.get("listing_url"),
                "street_view_url": lst.get("street_view_url"),
            }
            for lst in listings
            if (pr := props.get(lst.get("property_id"))) is not None and matches(pr, lst)
        )

        results = list(islice(result_iter, limit))
        return json.dumps({"results": results}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "query_active_listings",
                "description": "Search active listings by neighborhood(s) and criteria.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "neighborhood_ids": {"type": "array", "items": {"type": "integer"}},
                        "price_min": {"type": "integer"},
                        "price_max": {"type": "integer"},
                        "beds": {"type": "integer"},
                        "baths": {"type": "integer"},
                        "sqft_min": {"type": "integer"},
                        "sqft_max": {"type": "integer"},
                        "property_type": {"type": "string"},
                        "limit": {"type": "integer"},
                    },
                    "required": [],
                },
            },
        }
