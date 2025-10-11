# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CheckNoPurchases(Tool):
    """Checks if a list of purchase counts contains only zeros."""

    @staticmethod
    def invoke(data: Dict[str, Any], purchases_list) -> str:
        
        if purchases_list is None:
            return json.dumps({"error": "purchases_list is a required parameter."})
        
        all_zeros = all(purchase == 0 for purchase in purchases_list)
        return json.dumps({"all_zeros": all_zeros})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "check_no_purchases",
                "description": "Checks if a list of purchase counts contains only zeros.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "purchases_list": {
                            "type": "array",
                            "description": "List of purchase counts.",
                            "items": {
                                "type": "number"
                            }
                        }
                    },
                    "required": ["purchases_list"],
                },
            },
        }
