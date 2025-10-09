from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class CheckNoPurchases(Tool):
    """Verifies if a list of purchase counts consists solely of zeros."""

    @staticmethod
    def invoke(data: dict[str, Any], purchases_list: list[int] = None) -> str:
        if purchases_list is None:
            payload = {"error": "purchases_list is a required parameter."}
            out = json.dumps(payload)
            return out

        all_zeros = all(purchase == 0 for purchase in purchases_list.values()
        payload = {"all_zeros": all_zeros}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "checkNoPurchases",
                "description": "Checks if a list of purchase counts contains only zeros.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "purchases_list": {
                            "type": "array",
                            "description": "List of purchase counts.",
                            "items": {"type": "number"},
                        }
                    },
                    "required": ["purchases_list"],
                },
            },
        }
