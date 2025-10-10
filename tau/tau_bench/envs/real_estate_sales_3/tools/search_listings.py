# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchListings(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], baths, beds, neighborhood_ids, price_max, price_min, property_type, sqft_max, sqft_min, limit = 15) -> str:

        props = _index_by(list(data.get("properties", {}).values()), "property_id")
        results: List[Dict[str, Any]] = []
        for lst in list(data.get("listings", {}).values()) or []:
            if lst.get("status") != "active":
                continue
            pr = props.get(lst.get("property_id"))
            if not pr:
                continue
            if neighborhood_ids and pr.get("neighborhood_id") not in set(neighborhood_ids):
                continue
            if property_type and pr.get("property_type") != property_type:
                continue
            if beds is not None and pr.get("beds") != beds:
                continue
            if baths is not None and pr.get("baths") != baths:
                continue
            if price_min is not None and lst.get("list_price", 0) < price_min:
                continue
            if price_max is not None and lst.get("list_price", 0) > price_max:
                continue
            if sqft_min is not None and pr.get("sqft", 0) < sqft_min:
                continue
            if sqft_max is not None and pr.get("sqft", 0) > sqft_max:
                continue
            results.append({
                "listing_id": lst.get("listing_id"),
                "property_id": pr.get("property_id"),
                "neighborhood_id": pr.get("neighborhood_id"),
                "list_price": lst.get("list_price"),
                "property_type": pr.get("property_type"),
                "beds": pr.get("beds"), "baths": pr.get("baths"), "sqft": pr.get("sqft"),
                "listing_url": lst.get("listing_url"), "street_view_url": lst.get("street_view_url"),
            })
            if len(results) >= limit:
                break
        return json.dumps({"results": results}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"search_listings",
            "description":"Search active listings by neighborhood(s) and criteria.",
            "parameters":{
                "type":"object","properties":{
                    "neighborhood_ids":{"type":"array","items":{"type":"integer"}},
                    "price_min":{"type":"integer"},"price_max":{"type":"integer"},
                    "beds":{"type":"integer"},"baths":{"type":"integer"},
                    "sqft_min":{"type":"integer"},"sqft_max":{"type":"integer"},
                    "property_type":{"type":"string"},"limit":{"type":"integer"}
                },"required":[]
            }
        }}
