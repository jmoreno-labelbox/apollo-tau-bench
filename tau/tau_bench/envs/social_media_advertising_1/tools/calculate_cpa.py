from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class CalculateCPA(Tool):
    """Computes Cost Per Acquisition (CPA) using expenditure and purchases."""

    @staticmethod
    def invoke(data: dict[str, Any], spend: float = None, purchases: int = None) -> str:
        if spend is None or purchases is None:
            payload = {"error": "spend and purchases are required parameters."}
            out = json.dumps(payload)
            return out

        if purchases == 0:
            payload = {"error": "purchases cannot be zero."}
            out = json.dumps(payload)
            return out

        cpa = spend / purchases
        payload = {"cpa": cpa}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculateCpa",
                "description": "Calculates Cost Per Acquisition (CPA) from spend and purchases.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "spend": {
                            "type": "number",
                            "description": "The amount spent.",
                        },
                        "purchases": {
                            "type": "number",
                            "description": "The number of purchases.",
                        },
                    },
                    "required": ["spend", "purchases"],
                },
            },
        }
