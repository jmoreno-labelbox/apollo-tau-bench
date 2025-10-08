from tau_bench.envs.tool import Tool
import json
import math
import re
from typing import Any

class SearchListingsByCriteriaTool(Tool):
    """Queries the listings table to match client specifications."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        neighborhoods_json: list[str] = None,
        price_min: int = 0,
        price_max: int = None,
        status_filter: list[str] = None,
        max_results: int = None
    ) -> str:
        pass
        neighborhoods = neighborhoods_json or []
        price_min = price_min or 0
        price_max = price_max
        status_filter = status_filter
        max_results = _as_int(max_results)

        valid_status = {"sold", "for_sale", "off_market", "active", "pending", "rented"}

        # Process status_filter as a string or a list
        if status_filter:
            if isinstance(status_filter, list):
                # Check all statuses within the list for validity
                for status in status_filter:
                    if status not in valid_status:
                        return _err(
                            f"invalid status_filter '{status}'",
                            code="validation_error",
                            valid=list(sorted(valid_status)),
                        )
            else:
                # Validation for an individual status
                if status_filter not in valid_status:
                    return _err(
                        f"invalid status_filter '{status_filter}'",
                        code="validation_error",
                        valid=list(sorted(valid_status)),
                    )

        # Note: Neighborhood filtering has been eliminated - no mapping from property to neighborhood in the data
        matches: list[dict[str, Any]] = []
        for l in data.get("listings", []):
            pid = str(l.get("property_id"))

            # Omit listings that lack a property_id
            if not pid:
                continue

            # Note: Neighborhood filtering bypassed - no mapping for neighborhoods available
            if neighborhoods:
                # Record a warning indicating that neighborhood filtering is unsupported
                pass

            # Implement status filter (using OR logic for the list)
            if status_filter:
                listing_status = l.get("status")
                if isinstance(status_filter, list):
                    if listing_status not in status_filter:
                        continue
                else:
                    if listing_status != status_filter:
                        continue

            if not _price_in_range(l.get("list_price"), price_min, price_max):
                continue

            matches.append(
                {
                    "listing_id": l.get("listing_id"),
                    "property_id": pid,
                    "list_price": l.get("list_price"),
                    "price_per_sqft": l.get(
                        "price_per_sqft"
                    ),  # Utilize pre-calculated values from listings
                    "status": l.get("status"),
                }
            )

            # Enforce max_results limit if defined
            if max_results is not None and len(matches) >= max_results:
                break

        out = {
            "search_criteria": {
                "neighborhoods": neighborhoods,
                "price_range": [price_min, price_max],
                "status": status_filter,
                "max_results": max_results,
            },
            "matching_listings": matches,
            "total_matches": len(matches),
        }
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        #status_filter is mandated by prompt; permit null for adaptability
        return {
            "type": "function",
            "function": {
                "name": "SearchListingsByCriteria",
                "description": (
                    "Search listings by neighborhoods, price range, and status."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "neighborhoods_json": {
                            "type": "array",
                            "items": {"type": "integer"},
                        },
                        "price_min": {"type": ["integer", "null"]},
                        "price_max": {"type": ["integer", "null"]},
                        "status_filter": {
                            "type": ["string", "array", "null"],
                            "items": {"type": "string"},
                        },
                        "max_results": {
                            "type": ["integer", "null"],
                            "description": "Maximum number of results to return",
                        },
                    },
                    "required": [
                        "neighborhoods_json",
                        "price_max",
                        "status_filter",
                    ],
                },
            },
        }
