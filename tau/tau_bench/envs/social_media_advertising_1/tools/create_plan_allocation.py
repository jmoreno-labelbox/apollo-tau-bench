# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreatePlanAllocation(Tool):
    """Creates a plan allocation for an ad set."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        adset_id = kwargs.get("adset_id")
        budget = kwargs.get("budget")
        bid_strategy = kwargs.get("bid_strategy")
        bid_amount = kwargs.get("bid_amount")
        creative_type = kwargs.get("creative_type")
        
        # This tool would typically be used in the context of creating a full plan
        # For now, we'll just return the allocation details
        allocation = {
            "adset_id": adset_id,
            "budget": budget,
            "bid_strategy": bid_strategy,
            "bid_amount": bid_amount,
            "creative_type": creative_type
        }
        
        return json.dumps({
            "status": "success",
            "allocation": allocation
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_plan_allocation",
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
                        }
                    },
                    "required": ["adset_id", "budget", "bid_strategy", "creative_type"],
                },
            },
        }
