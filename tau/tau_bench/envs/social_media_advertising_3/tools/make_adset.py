from tau_bench.envs.tool import Tool
import csv
import json
import re
from datetime import datetime
from typing import Any

class MakeAdset(Tool):
    """Establish a new ad set within a campaign."""

    @staticmethod
    def invoke(data: dict[str, Any], campaign_id: str = None, name: str = None, budget: float = None, bid_type: str = None,
    status: Any = None,
    ) -> str:
        all_adsets = data.get("adsets", [])
        new_id = str(max((int(a["adset_id"]) for a in all_adsets), default=100) + 1)
        new = {
            "adset_id": new_id,
            "campaign_id": campaign_id,
            "name": name,
            "budget": budget,
            "bid_type": bid_type,
            "status": "paused",
        }
        all_adsets.append(new)
        data["adsets"] = all_adsets
        payload = new
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "makeAdset",
                "description": "Create a new ad set in a campaign.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "campaign_id": {"type": "string"},
                        "name": {"type": "string"},
                        "budget": {"type": "number"},
                        "bid_type": {"type": "string"},
                    },
                    "required": ["campaign_id", "name", "budget", "bid_type"],
                },
            },
        }
