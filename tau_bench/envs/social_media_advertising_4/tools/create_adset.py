from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class CreateAdset(Tool):
    """Initiates a new ad set inside a campaign."""

    @staticmethod
    def invoke(data: dict[str, Any], campaign_id: str = None, name: str = None, category: str = None, 
               daily_budget: float = None, bid_strategy: str = None, bid_amount: float = None,
               request_id: Any = None,
               status: Any = None,
               ) -> str:
        adsets = data.get("adsets", [])
        new_id = max((int(a["adset_id"]) for a in adsets), default=100) + 1
        new_adset = {
            "adset_id": str(new_id),
            "campaign_id": campaign_id,
            "name": name,
            "category": category,
            "daily_budget": daily_budget,
            "bid_strategy": bid_strategy,
            "bid_amount": bid_amount,
            "status": "paused",
            "updated_at": "2025-08-15T00:00:00Z",
        }
        adsets.append(new_adset)
        data["adsets"] = adsets
        payload = new_adset
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateAdset",
                "description": "Creates a new ad set within a specified campaign.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "campaign_id": {"type": "string"},
                        "name": {"type": "string"},
                        "category": {"type": "string"},
                        "daily_budget": {"type": "number"},
                        "bid_strategy": {"type": "string"},
                        "bid_amount": {"type": "number"},
                    },
                    "required": [
                        "campaign_id",
                        "name",
                        "category",
                        "daily_budget",
                        "bid_strategy",
                    ],
                },
            },
        }
