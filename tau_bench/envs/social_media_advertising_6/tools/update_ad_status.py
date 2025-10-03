from tau_bench.envs.tool import Tool
import copy
import json
from typing import Any

class UpdateAdStatus(Tool):
    """Modify a single ad's status with specified end_date if pausing."""

    @staticmethod
    def invoke(data: dict[str, Any], ad_id: str, status: str, end_date: str = None, request_id: Any = None,
    timestamp: Any = None,
    ) -> str:
        req = ["ad_id", "status"]
        err = _require({"ad_id": ad_id, "status": status}, req)
        if err:
            return _fail(err)
        ads = _assert_table(data, "ads")
        row = next(
            (r for r in ads if str(r.get("ad_id")) == str(ad_id)), None
        )
        if not row:
            return _fail("ad_not_found")
        row["status"] = status
        if status == "paused" and end_date:
            row["end_date"] = end_date
        payload = {"ok": True, "ad_id": str(ad_id), "status": status}
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateAdStatus",
                "description": "Set an ad status (active/paused).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ad_id": {"type": "string"},
                        "status": {"type": "string"},
                        "end_date": {"type": ["string", "null"]},
                    },
                    "required": ["ad_id", "status"],
                },
            },
        }
