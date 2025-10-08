from tau_bench.envs.tool import Tool
import copy
import json
from typing import Any

class UpdateAdsetStatus(Tool):
    """Specify adset status (active/paused) with a defined timestamp."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str, status: str, timestamp: str) -> str:
        req = ["adset_id", "status", "timestamp"]
        err = _require({"adset_id": adset_id, "status": status, "timestamp": timestamp}, req)
        if err:
            return _fail(err)
        adsets = _assert_table(data, "adsets")
        row = next(
            (r for r in adsets if str(r.get("adset_id")) == str(adset_id)),
            None,
        )
        if not row:
            return _fail("adset_not_found")
        row["status"] = status
        row["updated_at"] = timestamp
        payload = {
                "ok": True,
                "adset_id": str(adset_id),
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
                "name": "updateAdsetStatus",
                "description": "Activate/Pause an adset (explicit timestamp).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "status": {"type": "string"},
                        "timestamp": {"type": "string"},
                    },
                    "required": ["adset_id", "status", "timestamp"],
                },
            },
        }
