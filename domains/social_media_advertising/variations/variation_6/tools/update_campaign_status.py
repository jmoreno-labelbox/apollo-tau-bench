from tau_bench.envs.tool import Tool
import copy
import json
from typing import Any

class UpdateCampaignStatus(Tool):
    """Modify campaign status with specified timestamp and request_id (recorded in automation_runs)."""

    @staticmethod
    def invoke(data: dict[str, Any], campaign_id: str, status: str, timestamp: str, request_id: str) -> str:
        err = _require({"campaign_id": campaign_id, "status": status, "timestamp": timestamp, "request_id": request_id}, ["campaign_id", "status", "timestamp", "request_id"])
        if err:
            return _fail(err)
        rows = _assert_table(data, "campaigns")
        row = next(
            (
                r
                for r in rows
                if str(r.get("campaign_id")) == str(campaign_id)
            ),
            None,
        )
        if not row:
            return _fail("campaign_not_found")
        row["status"] = status
        row["updated_at"] = timestamp
        #optional: record in automation_runs
        runs = _assert_table(data, "automation_runs")
        _append_change(
            runs,
            {
                "run_type": "campaign_status_update",
                "started_at": timestamp,
                "ended_at": timestamp,
                "status": "completed",
                "input_ref": str(campaign_id),
                "outputs_json": {
                    "new_status": status,
                    "request_id": request_id,
                },
                "errors_json": None,
            },
        )
        payload = {
                "ok": True,
                "campaign_id": str(campaign_id),
                "status": status,
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateCampaignStatus",
                "description": "Set campaign status with explicit timestamp.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "campaign_id": {"type": "string"},
                        "status": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "request_id": {"type": "string"},
                    },
                    "required": ["campaign_id", "status", "timestamp", "request_id"],
                },
            },
        }
