from tau_bench.envs.tool import Tool
import copy
import json
from typing import Any

class GetAdsetDetailsByID(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str) -> str:
        err = _require({"adset_id": adset_id}, ["adset_id"])
        if err:
            return _fail(err)

        adset_id = str(adset_id)
        adsets_tbl = _assert_table(data, "adsets")
        row = _index(adsets_tbl, "adset_id").get(adset_id)
        if not row:
            payload = {"error": "adset_not_found"}
            out = json.dumps(payload)
            return out

        # Link ads using adset_id; handle absent ads table by returning an empty list
        try:
            ads_tbl = _assert_table(data, "ads")
        except Exception:
            ads_tbl = []

        ads_for_adset = [a for a in ads_tbl.values() if str(a.get("adset_id")) == adset_id]

        # Order: active first, followed by start_date (string-safe), then by name for consistency
        def sort_key(a: dict[str, Any]) -> tuple[Any, Any, Any]:
            status = a.get("status", "")
            start_date = a.get("start_date", "")  # retain as string to prevent parsing errors
            name = a.get("name", "")
            return (status != "active", str(start_date), str(name))

        ads_for_adset_sorted = sorted(ads_for_adset, key=sort_key)

        enriched = dict(row)
        enriched["ads"] = ads_for_adset_sorted
        payload = enriched
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAdsetDetailsById",
                "description": "Get a single adset by ID, including its ads.",
                "parameters": {
                    "type": "object",
                    "properties": {"adset_id": {"type": "string"}},
                    "required": ["adset_id"],
                },
            },
        }
