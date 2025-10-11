# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateAd(Tool):
    """Create an ad record (status must be provided; no implicit now)."""

    @staticmethod
    def invoke(data: Dict[str, Any], adset_id, creative_type, end_date, name, start_date, status) -> str:
        req = ["adset_id", "name", "creative_type", "status", "start_date"]
        err = _require(kwargs, req)
        if err: return _fail(err)
        ads = _assert_table(data, "ads")
        new_id = _next_numeric_id(ads, "ad_id")
        rec = {
            "ad_id": new_id,
            "adset_id": str(adset_id),
            "name": name,
            "creative_type": creative_type,
            "status": status,
            "start_date": start_date,
            "end_date": end_date,
        }
        ads.append(rec)
        return json.dumps(rec)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_ad", "description": "Create an ad under an adset.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"adset_id": {"type": "string"},
                                                                               "name": {"type": "string"},
                                                                               "creative_type": {"type": "string"},
                                                                               "status": {"type": "string"},
                                                                               "start_date": {"type": "string"},
                                                                               "end_date": {
                                                                                   "type": ["string", "null"]}},
                                                                "required": ["adset_id", "name", "creative_type",
                                                                             "status", "start_date"]}}}
