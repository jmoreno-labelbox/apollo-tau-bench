from tau_bench.envs.tool import Tool
import ast
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CreateAdset(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        campaign_id: str = None,
        name: str = None,
        category: str = None,
        daily_budget: float = None,
        bid_strategy: str = None,
        bid_amount: float = None,
        updated_at: str = None
,
    request_id: Any = None,
    status: Any = None,
    ) -> str:
        adsets = data.get("adsets", {}).values()
        nid = max((int(a["adset_id"]) for a in adsets.values()), default=100) + 1
        rec = {
            "adset_id": str(nid),
            "campaign_id": campaign_id,
            "name": name,
            "category": category,
            "daily_budget": daily_budget,
            "bid_strategy": bid_strategy,
            "bid_amount": bid_amount,
            "status": "paused",
            "updated_at": updated_at,
        }
        data["adsets"][rec["adset_id"]] = rec
        data["adsets"] = adsets
        payload = rec
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createAdset",
                "description": "Creates a paused ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "campaign_id": {"type": "string"},
                        "name": {"type": "string"},
                        "category": {"type": "string"},
                        "daily_budget": {"type": "number"},
                        "bid_strategy": {"type": "string"},
                        "bid_amount": {"type": "number"},
                        "updated_at": {"type": "string"},
                    },
                    "required": [
                        "campaign_id",
                        "name",
                        "category",
                        "daily_budget",
                        "bid_strategy",
                        "updated_at",
                    ],
                },
            },
        }
