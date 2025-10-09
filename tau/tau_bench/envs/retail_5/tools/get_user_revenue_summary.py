from tau_bench.envs.tool import Tool
import json
import os
from typing import Any

class GetUserRevenueSummary(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None) -> str:
        if not user_id:
            payload = {"error": "user_id is required"}
            out = json.dumps(payload)
            return out

        orders = data["orders"]
        revenue_data = {"user_id": user_id, "total_revenue": 0.0, "order_count": 0}

        for order in orders:
            if order["user_id"] == user_id and order["status"] in [
                "delivered",
                "completed",
                "processed",
            ]:
                order_total = sum(item["price"] for item in order["items"])
                revenue_data["total_revenue"] += order_total
                revenue_data["order_count"] += 1

        revenue_data["average_order_value"] = revenue_data["total_revenue"] / max(
            1, revenue_data["order_count"]
        )
        payload = revenue_data
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getUserRevenueSummary",
                "description": "Get revenue summary for a specific user including total revenue, order count, and order details.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "User ID to get revenue summary for",
                        }
                    },
                    "required": ["user_id"],
                },
            },
        }
