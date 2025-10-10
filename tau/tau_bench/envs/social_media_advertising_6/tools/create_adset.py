# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateAdset(Tool):
    """Create an adset with explicit created_at; requires campaign exists."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        req = ["campaign_id", "name", "daily_budget", "bid_strategy", "status", "created_at"]
        err = _require(kwargs, req)
        if err: return _fail(err)
        _assert_table(data, "campaigns")  # ensure table exists
        adsets = _assert_table(data, "adsets")
        new_id = _next_numeric_id(adsets, "adset_id")
        rec = {
            "adset_id": new_id,
            "campaign_id": str(kwargs["campaign_id"]),
            "name": kwargs["name"],
            "daily_budget": float(kwargs["daily_budget"]),
            "bid_strategy": kwargs["bid_strategy"],
            "bid_amount": kwargs.get("bid_amount"),
            "start_date": kwargs.get("start_date"),
            "end_date": kwargs.get("end_date"),
            "status": kwargs["status"],
            "updated_at": kwargs["created_at"],
        }
        adsets.append(rec)
        return json.dumps(rec)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_adset",
                                                 "description": "Create an adset (deterministic; explicit created_at).",
                                                 "parameters": {"type": "object",
                                                                "properties": {"campaign_id": {"type": "string"},
                                                                               "name": {"type": "string"},
                                                                               "daily_budget": {"type": "number"},
                                                                               "bid_strategy": {"type": "string"},
                                                                               "bid_amount": {
                                                                                   "type": ["number", "null"]},
                                                                               "start_date": {
                                                                                   "type": ["string", "null"]},
                                                                               "end_date": {"type": ["string", "null"]},
                                                                               "status": {"type": "string"},
                                                                               "created_at": {"type": "string"}},
                                                                "required": ["campaign_id", "name", "daily_budget",
                                                                             "bid_strategy", "status", "created_at"]}}}
