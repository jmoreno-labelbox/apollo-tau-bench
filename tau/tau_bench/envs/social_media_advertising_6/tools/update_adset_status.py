# Copyright by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateAdsetStatus(Tool):
    """Set adset status (active/paused) with explicit timestamp."""

    @staticmethod
    def invoke(data: Dict[str, Any], adset_id, status, timestamp) -> str:
        req = ["adset_id", "status", "timestamp"]
        err = _require(kwargs, req)
        if err: return _fail(err)
        adsets = _assert_table(data, "adsets")
        row = next((r for r in adsets if str(r.get("adset_id")) == str(adset_id)), None)
        if not row: return _fail("adset_not_found")
        row["status"] = status
        row["updated_at"] = timestamp
        return json.dumps({"ok": True, "adset_id": str(adset_id), "status": status})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_adset_status",
                                                 "description": "Activate/Pause an adset (explicit timestamp).",
                                                 "parameters": {"type": "object",
                                                                "properties": {"adset_id": {"type": "string"},
                                                                               "status": {"type": "string"},
                                                                               "timestamp": {"type": "string"}},
                                                                "required": ["adset_id", "status", "timestamp"]}}}
