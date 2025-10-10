# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchListingsInNeighborhoods(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], neighborhood_ids) -> str:
        neighborhood_ids = neighborhood_ids or []
        return SearchListings.invoke(data, **kwargs)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"search_listings_in_neighborhoods",
            "description":"Search listings within the provided neighborhoods.",
            "parameters":{
                "type":"object","properties":{
                    "neighborhood_ids":{"type":"array","items":{"type":"integer"}},
                    "price_min":{"type":"integer"},"price_max":{"type":"integer"},
                    "beds":{"type":"integer"},"baths":{"type":"integer"},"limit":{"type":"integer"}
                },"required":["neighborhood_ids"]
            }
        }}
