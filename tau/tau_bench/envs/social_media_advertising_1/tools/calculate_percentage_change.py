# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CalculatePercentageChange(Tool):
    """Calculates the percentage change in revenue between two values."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        current_value = kwargs.get("current_value")
        previous_value = kwargs.get("previous_value")
        
        if current_value is None or previous_value is None:
            return json.dumps({"error": "current_value and previous_value are required parameters."})
        
        if previous_value == 0:
            return json.dumps({"error": "previous_value cannot be zero."})
        
        change_percent = ((current_value - previous_value) / previous_value) * 100
        return json.dumps({"change_percent": change_percent})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_percentage_change",
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
                        }
                    },
                    "required": ["current_value", "previous_value"],
                },
            },
        }
