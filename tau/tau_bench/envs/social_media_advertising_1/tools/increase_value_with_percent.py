from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class IncreaseValueWithPercent(Tool):
    """Boosts a value by a defined percentage."""

    @staticmethod
    def invoke(data: dict[str, Any], value: float = None, percent: float = None) -> str:
        if value is None or percent is None:
            payload = {"error": "value and percent are required parameters."}
            out = json.dumps(payload)
            return out

        new_value = value * (100 + percent) / 100
        payload = {"new_value": new_value}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "IncreaseValueWithPercent",
                "description": "Increases a value by a specified percentage.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "value": {
                            "type": "number",
                            "description": "The original value.",
                        },
                        "percent": {
                            "type": "number",
                            "description": "The percentage to increase by.",
                        },
                    },
                    "required": ["value", "percent"],
                },
            },
        }
