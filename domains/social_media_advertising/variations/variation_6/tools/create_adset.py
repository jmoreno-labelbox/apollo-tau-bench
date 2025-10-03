from tau_bench.envs.tool import Tool
import copy
import json
from typing import Any

class CreateAdset(Tool):
    """Generate an adset with specified created_at; requires campaign to exist."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        campaign_id: str,
        name: str,
        daily_budget: float,
        bid_strategy: str,
        status: str,
        created_at: str,
        bid_amount: float = None,
        start_date: str = None,
        end_date: str = None
,
    request_id: Any = None,
    ) -> str:
        req = [
            "campaign_id",
            "name",
            "daily_budget",
            "bid_strategy",
            "status",
            "created_at",
        ]
        err = _require(locals(), req)
        if err:
            return _fail(err)
        _assert_table(data, "campaigns")  # verify the existence of the table
        adsets = _assert_table(data, "adsets")
        new_id = _next_numeric_id(adsets, "adset_id")
        rec = {
            "adset_id": new_id,
            "campaign_id": str(campaign_id),
            "name": name,
            "daily_budget": float(daily_budget),
            "bid_strategy": bid_strategy,
            "bid_amount": bid_amount,
            "start_date": start_date,
            "end_date": end_date,
            "status": status,
            "updated_at": created_at,
        }
        adsets.append(rec)
        payload = rec
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createAdset",
                "description": "Create an adset (deterministic; explicit created_at).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "campaign_id": {"type": "string"},
                        "name": {"type": "string"},
                        "daily_budget": {"type": "number"},
                        "bid_strategy": {"type": "string"},
                        "bid_amount": {"type": ["number", "null"]},
                        "start_date": {"type": ["string", "null"]},
                        "end_date": {"type": ["string", "null"]},
                        "status": {"type": "string"},
                        "created_at": {"type": "string"},
                    },
                    "required": [
                        "campaign_id",
                        "name",
                        "daily_budget",
                        "bid_strategy",
                        "status",
                        "created_at",
                    ],
                },
            },
        }
