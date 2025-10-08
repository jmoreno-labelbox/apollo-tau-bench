from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class CompareValue(Tool):
    """Evaluates a value against a threshold with a defined operator."""

    @staticmethod
    def invoke(data: dict[str, Any], value: Any = None, threshold: Any = None, operator: str = None) -> str:
        if value is None or threshold is None or operator is None:
            payload = {"error": "value, threshold, and operator are required parameters."}
            out = json.dumps(payload)
            return out

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
            payload = {"error": f"Unknown operator: {operator}"}
            out = json.dumps(payload)
            return out
        payload = {"result": result}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CompareValue",
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
                        },
                    },
                    "required": ["value", "threshold", "operator"],
                },
            },
        }
