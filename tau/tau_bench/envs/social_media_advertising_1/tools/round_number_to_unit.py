# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RoundNumberToUnit(Tool):
    """Rounds a number to the nearest multiple of a specified unit."""

    @staticmethod
    def invoke(data: Dict[str, Any], number, unit) -> str:
        
        if number is None or unit is None:
            return json.dumps({"error": "number and unit are required parameters."})
        
        if unit <= 0:
            return json.dumps({"error": "unit must be a positive number."})
        
        rounded_number = round(number / unit) * unit
        return json.dumps({"rounded_number": rounded_number})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "round_number_to_unit",
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
                        }
                    },
                    "required": ["number", "unit"],
                },
            },
        }
