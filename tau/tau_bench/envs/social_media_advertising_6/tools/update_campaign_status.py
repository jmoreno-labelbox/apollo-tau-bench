# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool










def _require(kwargs: Dict[str, Any], names: List[str]) -> Optional[str]:
    for n in names:
        if n not in kwargs:
            return f"missing_arg:{n}"
    return None

def _fail(msg: str) -> str:
    return json.dumps({"error": msg})

def _assert_table(data: Dict[str, Any], key: str) -> List[Dict[str, Any]]:
    if key not in data:
        raise ValueError(f"missing_table:{key}")
    tbl = data[key]
    if not isinstance(tbl, list):
        raise ValueError(f"invalid_table:{key}")
    return tbl

def _append_change(tbl: List[Dict[str, Any]], rec: Dict[str, Any]) -> None:
    tbl.append(rec)

class UpdateCampaignStatus(Tool):
    """Update campaign status with explicit timestamp and request_id (logged in automation_runs)."""

    @staticmethod
    def invoke(data: Dict[str, Any], campaign_id, request_id, status, timestamp) -> str:
        err = _require(kwargs, ["campaign_id", "status", "timestamp", "request_id"])
        if err: return _fail(err)
        rows = _assert_table(data, "campaigns")
        row = next((r for r in rows if str(r.get("campaign_id")) == str(campaign_id)), None)
        if not row: return _fail("campaign_not_found")
        row["status"] = status
        row["updated_at"] = timestamp
        # optional: record in automation_runs
        runs = _assert_table(data, "automation_runs")
        _append_change(runs, {"run_type": "campaign_status_update", "started_at": timestamp,
                              "ended_at": timestamp, "status": "completed",
                              "input_ref": str(campaign_id),
                              "outputs_json": {"new_status": status, "request_id": request_id},
                              "errors_json": None})
        return json.dumps({"ok": True, "campaign_id": str(campaign_id), "status": status})

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