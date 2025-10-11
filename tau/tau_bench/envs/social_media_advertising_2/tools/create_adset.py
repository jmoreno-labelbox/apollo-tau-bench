# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateAdset(Tool):
    """Create a new ad set inside a campaign."""

    @staticmethod
    def invoke(data: Dict[str, Any], bid_type, budget, campaign_id, name) -> str:
        all_adsets = list(data.get("adsets", {}).values())
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
        return json.dumps(new)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_adset",
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
