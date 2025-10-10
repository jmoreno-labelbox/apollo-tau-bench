# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class Calculate(Tool):
    """
    A tool to safely evaluate a basic mathematical expression.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], expression: str) -> str:
        allowed_chars = set("0123456789+-*/(). ")
        if not set(expression).issubset(allowed_chars):
            return json.dumps({"error": "Invalid characters in expression."})
        try:
            result = round(float(eval(expression, {"__builtins__": None}, {})), 2)
            return str(result)
        except Exception as e:
            return json.dumps({"error": str(e)})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate",
                "description": "Calculates the result of a simple mathematical expression.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "expression": {
                            "type": "string",
                            "description": "The mathematical expression to evaluate (e.g., '155 + 225 + 70')."
                        }
                    },
                    "required": ["expression"]
                }
            }
        }
