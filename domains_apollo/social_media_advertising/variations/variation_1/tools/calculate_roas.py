from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class CalculateROAS(Tool):
    """Computes Return on Ad Spend (ROAS) based on revenue and expenditure."""

    @staticmethod
    def invoke(data: dict[str, Any], revenue: float = None, spend: float = None) -> str:
        if revenue is None or spend is None:
            payload = {"error": "revenue and spend are required parameters."}
            out = json.dumps(payload)
            return out

        if spend == 0:
            payload = {"error": "spend cannot be zero."}
            out = json.dumps(payload)
            return out

        roas = revenue / spend
        payload = {"roas": roas}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculateRoas",
                "description": "Calculates Return on Ad Spend (ROAS) from revenue and spend.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "revenue": {
                            "type": "number",
                            "description": "The revenue generated.",
                        },
                        "spend": {
                            "type": "number",
                            "description": "The amount spent.",
                        },
                    },
                    "required": ["revenue", "spend"],
                },
            },
        }
