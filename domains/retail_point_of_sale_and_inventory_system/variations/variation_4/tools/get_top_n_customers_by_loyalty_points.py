from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetTopNCustomersByLoyaltyPoints(Tool):  #VIEW
    @staticmethod
    def invoke(data: dict[str, Any], n: int) -> str:
        customers = data["customers"]
        # Order by loyalty_points from highest to lowest
        sorted_customers = sorted(
            customers, key=lambda c: c["loyalty_points"], reverse=True
        )
        top_customers = sorted_customers[:n]
        payload = top_customers
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTopNCustomersByLoyaltyPoints",
                "description": "Get the top N customers sorted by loyalty points in descending order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "n": {
                            "type": "integer",
                            "description": "Number of top customers to return.",
                        }
                    },
                    "required": ["n"],
                },
            },
        }
