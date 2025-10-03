from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class CalculateSpendVariance(Tool):
    """Computes the percentage variance between projected and actual expenditure."""

    @staticmethod
    def invoke(data: dict[str, Any], planned_spend: float = None, actual_spend: float = None) -> str:
        if planned_spend is None or actual_spend is None:
            payload = {"error": "planned_spend and actual_spend are required parameters."}
            out = json.dumps(payload)
            return out

        if planned_spend == 0:
            payload = {"error": "planned_spend cannot be zero."}
            out = json.dumps(payload)
            return out

        variance_percent = ((actual_spend - planned_spend) / planned_spend) * 100
        payload = {"variance_percent": variance_percent}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateSpendVariance",
                "description": "Calculates the variance percentage between planned and actual spend.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "planned_spend": {
                            "type": "number",
                            "description": "The planned spend amount.",
                        },
                        "actual_spend": {
                            "type": "number",
                            "description": "The actual spend amount.",
                        },
                    },
                    "required": ["planned_spend", "actual_spend"],
                },
            },
        }
