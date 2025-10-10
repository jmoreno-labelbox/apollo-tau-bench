# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddAdSet(Tool):
    """Adds a new ad set."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        adset_id = kwargs.get("adset_id")
        campaign_id = kwargs.get("campaign_id")
        name = kwargs.get("name")
        category = kwargs.get("category")
        daily_budget = kwargs.get("daily_budget")
        bid_strategy = kwargs.get("bid_strategy")
        bid_amount = kwargs.get("bid_amount")
        status = kwargs.get("status")
        updated_at = kwargs.get("updated_at")

        if not adset_id:
            return json.dumps({"error": "adset_id is a required parameter."})
        if not campaign_id:
            return json.dumps({"error": "campaign_id is a required parameter."})
        if not name:
            return json.dumps({"error": "name is a required parameter."})
        if not category:
            return json.dumps({"error": "category is a required parameter."})
        if not daily_budget:
            return json.dumps({"error": "daily_budget is a required parameter."})
        if not bid_strategy:
            return json.dumps({"error": "bid_strategy is a required parameter."})
        if not status:
            return json.dumps({"error": "status is a required parameter."})
        if not updated_at:
            return json.dumps({"error": "updated_at is a required parameter."})

        new_adset = {
            "adset_id": adset_id,
            "campaign_id": campaign_id,
            "name": name,
            "category": category,
            "daily_budget": daily_budget,
            "bid_strategy": bid_strategy,
            "bid_amount": bid_amount,
            "status": status,
            "updated_at": updated_at
        }
        data['adsets'] += [new_adset]

        return json.dumps(
            {
                "status": "success",
                "message": f"New ad set was added: {new_adset}",
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_adset",
                "description": "Adds a new ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {
                            "type": "string",
                            "description": "The unique ID of the new ad set.",
                        },
                        "campaign_id": {
                            "type": "string",
                            "description": "The ID of the campaign this ad set belongs to.",
                        },
                        "name": {
                            "type": "string",
                            "description": "The name of the ad set.",
                        },
                        "category": {
                            "type": "string",
                            "description": "The category of the ad set (e.g., Electronics, Apparel).",
                        },
                        "daily_budget": {
                            "type": "number",
                            "description": "The daily budget for the ad set.",
                        },
                        "bid_strategy": {
                            "type": "string",
                            "description": "The bid strategy (e.g., lowest_cost, cost_cap).",
                        },
                        "bid_amount": {
                            "type": "number",
                            "description": "The bid amount (if applicable).",
                        },
                        "status": {
                            "type": "string",
                            "description": "The status of the ad set (e.g., active, paused).",
                        },
                        "updated_at": {
                            "type": "string",
                            "description": "The last update timestamp (ISO format).",
                        }
                    },
                    "required": ["adset_id", "campaign_id", "name", "category", "daily_budget", "bid_strategy", "status", "updated_at"],
                },
            },
        }
