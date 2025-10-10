# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DecreaseValueWithPercent(Tool):
    """Decreases a value by a specified percentage."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        value = kwargs.get("value")
        percent = kwargs.get("percent")
        
        if value is None or percent is None:
            return json.dumps({"error": "value and percent are required parameters."})
        
        new_value = value * (100 - percent) / 100
        return json.dumps({"new_value": new_value})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "decrease_value_with_percent",
                "description": "Decreases a value by a specified percentage.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "value": {
                            "type": "number",
                            "description": "The original value.",
                        },
                        "percent": {
                            "type": "number",
                            "description": "The percentage to decrease by.",
                        }
                    },
                    "required": ["value", "percent"],
                },
            },
        }
