from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class CalculatePercentageChange(Tool):
    """Computes the percentage difference in revenue between two amounts."""

    @staticmethod
    def invoke(data: dict[str, Any], current_value: float = None, previous_value: float = None) -> str:
        if current_value is None or previous_value is None:
            payload = {"error": "current_value and previous_value are required parameters."}
            out = json.dumps(payload)
            return out

        if previous_value == 0:
            payload = {"error": "previous_value cannot be zero."}
            out = json.dumps(payload)
            return out

        change_percent = ((current_value - previous_value) / previous_value) * 100
        payload = {"change_percent": change_percent}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculatePercentageChange",
                "description": "Calculates the percentage change between two values.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "current_value": {
                            "type": "number",
                            "description": "The current value.",
                        },
                        "previous_value": {
                            "type": "number",
                            "description": "The previous value.",
                        },
                    },
                    "required": ["current_value", "previous_value"],
                },
            },
        }
