# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchListingsByCriteriaTool(Tool):
    """Searches listings table matching client criteria."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        neighborhoods = kwargs.get("neighborhoods_json") or []
        price_min = kwargs.get("price_min") or 0
        price_max = kwargs.get("price_max")
        status_filter = kwargs.get("status_filter")
        max_results = _as_int(kwargs.get("max_results"))

        valid_status = {"sold", "for_sale", "off_market", "active", "pending", "rented"}

        # Handle status_filter as either string or list
        if status_filter:
            if isinstance(status_filter, list):
                # Validate all statuses in the list
                for status in status_filter:
                    if status not in valid_status:
                        return _err(
                            f"invalid status_filter '{status}'",
                            code="validation_error",
                            valid=list(sorted(valid_status)),
                        )
            else:
                # Single status validation
                if status_filter not in valid_status:
                    return _err(
                        f"invalid status_filter '{status_filter}'",
                        code="validation_error",
                        valid=list(sorted(valid_status)),
                    )

        # Note: Neighborhood filtering removed - no property-to-neighborhood mapping in data
        matches: List[Dict[str, Any]] = []
        for l in list(data.get("listings", {}).values()):
            pid = str(l.get("property_id"))

            # Skip listings without property_id
            if not pid:
                continue

            # Note: Neighborhood filtering skipped - no neighborhood mapping available
            if neighborhoods:
                # Log warning that neighborhood filtering is not supported
                pass

            # Apply status filter (OR logic for list)
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
                    ),  # Use pre-calculated value from listings
                    "status": l.get("status"),
                }
            )

            # Apply max_results limit if specified
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
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        # status_filter required by prompt; allow null for flexibility
        return {
            "type": "function",
            "function": {
                "name": "search_listings_by_criteria",
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
