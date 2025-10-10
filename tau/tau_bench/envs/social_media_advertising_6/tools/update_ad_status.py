# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateAdStatus(Tool):
    """Update a single ad's status with explicit end_date if pausing."""

    @staticmethod
    def invoke(data: Dict[str, Any], ad_id, end_date, status) -> str:
        req = ["ad_id", "status"]
        err = _require(kwargs, req)
        if err: return _fail(err)
        ads = _assert_table(data, "ads")
        row = next((r for r in ads if str(r.get("ad_id")) == str(ad_id)), None)
        if not row: return _fail("ad_not_found")
        row["status"] = status
        if status == "paused" and end_date:
            row["end_date"] = end_date
        return json.dumps({"ok": True, "ad_id": str(ad_id), "status": status})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "update_ad_status", "description": "Set an ad status (active/paused).",
                             "parameters": {"type": "object",
                                            "properties": {"ad_id": {"type": "string"}, "status": {"type": "string"},
                                                           "end_date": {"type": ["string", "null"]}},
                                            "required": ["ad_id", "status"]}}}
