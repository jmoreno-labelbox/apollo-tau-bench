from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class AddAdSet(Tool):
    """Creates a new ad set."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        adset_id: str = None,
        campaign_id: str = None,
        name: str = None,
        category: str = None,
        daily_budget: float = None,
        bid_strategy: str = None,
        bid_amount: float = None,
        status: str = None,
        updated_at: str = None
    ) -> str:
        if not adset_id:
            payload = {"error": "adset_id is a required parameter."}
            out = json.dumps(payload)
            return out
        if not campaign_id:
            payload = {"error": "campaign_id is a required parameter."}
            out = json.dumps(payload)
            return out
        if not name:
            payload = {"error": "name is a required parameter."}
            out = json.dumps(payload)
            return out
        if not category:
            payload = {"error": "category is a required parameter."}
            out = json.dumps(payload)
            return out
        if not daily_budget:
            payload = {"error": "daily_budget is a required parameter."}
            out = json.dumps(payload)
            return out
        if not bid_strategy:
            payload = {"error": "bid_strategy is a required parameter."}
            out = json.dumps(payload)
            return out
        if not status:
            payload = {"error": "status is a required parameter."}
            out = json.dumps(payload)
            return out
        if not updated_at:
            payload = {"error": "updated_at is a required parameter."}
            out = json.dumps(payload)
            return out

        new_adset = {
            "adset_id": adset_id,
            "campaign_id": campaign_id,
            "name": name,
            "category": category,
            "daily_budget": daily_budget,
            "bid_strategy": bid_strategy,
            "bid_amount": bid_amount,
            "status": status,
            "updated_at": updated_at,
        }
        data["adsets"] += [new_adset]
        payload = {
            "status": "success",
            "message": f"New ad set was added: {new_adset}",
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddAdset",
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
                        },
                    },
                    "required": [
                        "adset_id",
                        "campaign_id",
                        "name",
                        "category",
                        "daily_budget",
                        "bid_strategy",
                        "status",
                        "updated_at",
                    ],
                },
            },
        }
