# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateCampaignStatus(Tool):
    """Update campaign status with explicit timestamp and request_id (logged in automation_runs)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        err = _require(kwargs, ["campaign_id", "status", "timestamp", "request_id"])
        if err: return _fail(err)
        rows = _assert_table(data, "campaigns")
        row = next((r for r in rows if str(r.get("campaign_id")) == str(kwargs["campaign_id"])), None)
        if not row: return _fail("campaign_not_found")
        row["status"] = kwargs["status"]
        row["updated_at"] = kwargs["timestamp"]
        # optional: log to automation_runs
        runs = _assert_table(data, "automation_runs")
        _append_change(runs, {"run_type": "campaign_status_update", "started_at": kwargs["timestamp"],
                              "ended_at": kwargs["timestamp"], "status": "completed",
                              "input_ref": str(kwargs["campaign_id"]),
                              "outputs_json": {"new_status": kwargs["status"], "request_id": kwargs["request_id"]},
                              "errors_json": None})
        return json.dumps({"ok": True, "campaign_id": str(kwargs["campaign_id"]), "status": kwargs["status"]})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_campaign_status",
                                                 "description": "Set campaign status with explicit timestamp.",
                                                 "parameters": {"type": "object",
                                                                "properties": {"campaign_id": {"type": "string"},
                                                                               "status": {"type": "string"},
                                                                               "timestamp": {"type": "string"},
                                                                               "request_id": {"type": "string"}},
                                                                "required": ["campaign_id", "status", "timestamp",
                                                                             "request_id"]}}}
