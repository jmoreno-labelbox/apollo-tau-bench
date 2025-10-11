# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetTopNCustomersByLoyaltyPoints(Tool): # READ DATA
    @staticmethod
    def invoke(data: Dict[str, Any], n: int) -> str:
        customers = data["customers"]
        # Order by loyalty_points in descending fashion.
        sorted_customers = sorted(customers, key=lambda c: c["loyalty_points"], reverse=True)
        top_customers = sorted_customers[:n]
        return json.dumps(top_customers)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_top_n_customers_by_loyalty_points",
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
