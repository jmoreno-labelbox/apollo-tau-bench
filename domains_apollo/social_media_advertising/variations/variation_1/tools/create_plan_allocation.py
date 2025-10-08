from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class CreatePlanAllocation(Tool):
    """Establishes a plan allocation for an ad set."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None, budget: float = None, bid_strategy: str = None, bid_amount: float = None, creative_type: str = None) -> str:
        # This tool is generally utilized for developing a complete plan
        # Currently, we will only provide the allocation information
        allocation = {
            "adset_id": adset_id,
            "budget": budget,
            "bid_strategy": bid_strategy,
            "bid_amount": bid_amount,
            "creative_type": creative_type,
        }
        payload = {"status": "success", "allocation": allocation}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createPlanAllocation",
                "description": "Creates a plan allocation for an ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {
                            "type": "string",
                            "description": "The ID of the ad set.",
                        },
                        "budget": {
                            "type": "number",
                            "description": "The allocated budget.",
                        },
                        "bid_strategy": {
                            "type": "string",
                            "description": "The bid strategy.",
                        },
                        "bid_amount": {
                            "type": "number",
                            "description": "The bid amount.",
                        },
                        "creative_type": {
                            "type": "string",
                            "description": "The creative type.",
                        },
                    },
                    "required": ["adset_id", "budget", "bid_strategy", "creative_type"],
                },
            },
        }
