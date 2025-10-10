# Copyright by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateAdsetStatus(Tool):
    """Set adset status (active/paused) with explicit timestamp."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        req = ["adset_id", "status", "timestamp"]
        err = _require(kwargs, req)
        if err: return _fail(err)
        adsets = _assert_table(data, "adsets")
        row = next((r for r in adsets if str(r.get("adset_id")) == str(kwargs["adset_id"])), None)
        if not row: return _fail("adset_not_found")
        row["status"] = kwargs["status"]
        row["updated_at"] = kwargs["timestamp"]
        return json.dumps({"ok": True, "adset_id": str(kwargs["adset_id"]), "status": kwargs["status"]})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_adset_status",
                                                 "description": "Activate/Pause an adset (explicit timestamp).",
                                                 "parameters": {"type": "object",
                                                                "properties": {"adset_id": {"type": "string"},
                                                                               "status": {"type": "string"},
                                                                               "timestamp": {"type": "string"}},
                                                                "required": ["adset_id", "status", "timestamp"]}}}
