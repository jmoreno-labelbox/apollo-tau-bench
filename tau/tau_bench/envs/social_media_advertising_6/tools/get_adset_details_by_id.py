# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAdsetDetailsByID(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        err = _require(kwargs, ["adset_id"])
        if err:
            return _fail(err)

        adset_id = str(kwargs["adset_id"])
        adsets_tbl = _assert_table(data, "adsets")
        row = _index(adsets_tbl, "adset_id").get(adset_id)
        if not row:
            return json.dumps({"error": "adset_not_found"})

        # Perform a join on adset_id with the ads table; handle the absence of the ads table by returning an empty array.
        try:
            ads_tbl = _assert_table(data, "ads")
        except Exception:
            ads_tbl = []

        ads_for_adset = [a for a in ads_tbl if str(a.get("adset_id")) == adset_id]

        # Order by active status first, followed by start_date (string-safe), and then by name for consistency.
        def sort_key(a: Dict[str, Any]) -> Tuple[Any, Any, Any]:
            status = a.get("status", "")
            start_date = a.get("start_date", "")  # retain as a string to prevent parsing issues
            name = a.get("name", "")
            return (status != "active", str(start_date), str(name))

        ads_for_adset_sorted = sorted(ads_for_adset, key=sort_key)

        enriched = dict(row)
        enriched["ads"] = ads_for_adset_sorted
        return json.dumps(enriched)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_adset_details_by_id",
                "description": "Get a single adset by ID, including its ads.",
                "parameters": {
                    "type": "object",
                    "properties": {"adset_id": {"type": "string"}},
                    "required": ["adset_id"]
                }
            }
        }
