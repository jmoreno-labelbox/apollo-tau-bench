from tau_bench.envs.tool import Tool
import copy
import json
from typing import Any

class CreateAd(Tool):
    """Generate an ad record (status must be specified; no implicit now)."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        adset_id: str,
        name: str,
        creative_type: str,
        status: str,
        start_date: str,
        end_date: str = None,
        request_id: str = None
    ) -> str:
        req = ["adset_id", "name", "creative_type", "status", "start_date"]
        err = _require(locals(), req)
        if err:
            return _fail(err)
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
        payload = rec
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateAd",
                "description": "Create an ad under an adset.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "name": {"type": "string"},
                        "creative_type": {"type": "string"},
                        "status": {"type": "string"},
                        "start_date": {"type": "string"},
                        "end_date": {"type": ["string", "null"]},
                    },
                    "required": [
                        "adset_id",
                        "name",
                        "creative_type",
                        "status",
                        "start_date",
                    ],
                },
            },
        }
