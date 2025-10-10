# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CompareValue(Tool):
    """Compares a value with a threshold using a specified operator."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        value = kwargs.get("value")
        threshold = kwargs.get("threshold")
        operator = kwargs.get("operator")
        
        if value is None or threshold is None or operator is None:
            return json.dumps({"error": "value, threshold, and operator are required parameters."})
        
        result = False
        if operator == "greater":
            result = value > threshold
        elif operator == "greater_equal":
            result = value >= threshold
        elif operator == "less":
            result = value < threshold
        elif operator == "less_equal":
            result = value <= threshold
        elif operator == "equal":
            result = value == threshold
        else:
            return json.dumps({"error": f"Unknown operator: {operator}"})
        
        return json.dumps({"result": result})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "compare_value",
                "description": "Compares a value with a threshold using a specified operator.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "value": {
                            "type": "number",
                            "description": "The value to compare.",
                        },
                        "threshold": {
                            "type": "number",
                            "description": "The threshold value.",
                        },
                        "operator": {
                            "type": "string",
                            "description": "The comparison operator (greater, greater_equal, less, less_equal, equal).",
                        }
                    },
                    "required": ["value", "threshold", "operator"],
                },
            },
        }
