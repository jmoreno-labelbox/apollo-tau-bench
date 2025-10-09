from tau_bench.envs.tool import Tool
import json
from itertools import islice
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class QueryActiveListings(Tool):
    """Select and provide active listings based on specified criteria."""

    @staticmethod
    def _by_key(rows: list[dict[str, Any]], key: str) -> dict[Any, dict[str, Any]]:
        pass
        return {r.get(key): r for r in rows or []}

    @staticmethod
    def invoke(
        data: dict[str, Any],
        neighborhood_ids: list[int] = None,
        price_min: float = None,
        price_max: float = None,
        beds: int = None,
        baths: int = None,
        sqft_min: int = None,
        sqft_max: int = None,
        property_type: str = None,
        limit: int = 15
    ) -> str:
        neighborhoods = set(neighborhood_ids or [])
        props = QueryActiveListings._by_key(data.get("properties", {}).values(), "property_id")
        listings = data.get("listings") or []

        def within(val: float | None, lo: float | None, hi: float | None) -> bool:
            v = 0 if val is None else val
            if lo is not None and v < lo:
                return False
            if hi is not None and v > hi:
                return False
            return True

        def matches(pr: dict[str, Any], lst: dict[str, Any]) -> bool:
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
            for lst in listings.values() if (pr := props.get(lst.get("property_id"))) is not None
            and matches(pr, lst)
        )

        results = list(islice(result_iter, limit))
        payload = {"results": results}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "QueryActiveListings",
                "description": "Search active listings by neighborhood(s) and criteria.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "neighborhood_ids": {
                            "type": "array",
                            "items": {"type": "integer"},
                        },
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
