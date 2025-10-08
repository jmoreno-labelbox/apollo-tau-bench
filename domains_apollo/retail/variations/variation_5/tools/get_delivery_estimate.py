from tau_bench.envs.tool import Tool
import json
import os
from typing import Any

class GetDeliveryEstimate(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], destination_country: str, delivery_option: str = "standard") -> str:
        if not destination_country:
            payload = {"error": "destination_country is required"}
            out = json.dumps(payload)
            return out

        couriers = data["couriers"]

        available_couriers = [
            c for c in couriers if destination_country in c["coverage_area"]
        ]

        if not available_couriers:
            payload = {"error": f"No delivery available to {destination_country}"}
            out = json.dumps(
                payload)
            return out

        delivery_estimates = {
            "express": {"min_days": 1, "max_days": 3, "cost_multiplier": 2.5},
            "standard": {"min_days": 3, "max_days": 7, "cost_multiplier": 1.0},
            "economy": {"min_days": 7, "max_days": 14, "cost_multiplier": 0.7},
        }

        estimate = delivery_estimates.get(
            delivery_option, delivery_estimates["standard"]
        )
        payload = {
                "destination_country": destination_country,
                "delivery_option": delivery_option,
                "estimated_days": f"{estimate['min_days']}-{estimate['max_days']}",
                "available_couriers": len(available_couriers),
                "cost_multiplier": estimate["cost_multiplier"],
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getDeliveryEstimate",
                "description": "Get delivery time estimates and available couriers for a destination.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "destination_country": {
                            "type": "string",
                            "description": "Country to deliver to",
                        },
                        "delivery_option": {
                            "type": "string",
                            "description": "Delivery speed option",
                            "enum": ["express", "standard", "economy"],
                            "default": "standard",
                        },
                    },
                    "required": ["destination_country"],
                },
            },
        }
