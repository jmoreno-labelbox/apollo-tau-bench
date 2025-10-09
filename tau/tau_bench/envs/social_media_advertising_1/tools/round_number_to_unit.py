from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class RoundNumberToUnit(Tool):
    """Rounds a number to the closest multiple of a defined unit."""

    @staticmethod
    def invoke(data: dict[str, Any], number: float = None, unit: float = None) -> str:
        if number is None or unit is None:
            payload = {"error": "number and unit are required parameters."}
            out = json.dumps(payload)
            return out

        if unit <= 0:
            payload = {"error": "unit must be a positive number."}
            out = json.dumps(payload)
            return out

        rounded_number = round(number / unit) * unit
        payload = {"rounded_number": rounded_number}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RoundNumberToUnit",
                "description": "Rounds a number to the nearest multiple of a specified unit.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "number": {
                            "type": "number",
                            "description": "The number to round.",
                        },
                        "unit": {
                            "type": "number",
                            "description": "The unit to round to (e.g., 10 for rounding to nearest 10).",
                        },
                    },
                    "required": ["number", "unit"],
                },
            },
        }
