from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timedelta
from typing import Any

class Calculate(Tool):

    @staticmethod
    def invoke(data: dict[str, Any], expression: str) -> str:
        allowed_chars = set("0123456789+-*/(). ")
        if not set(expression).issubset(allowed_chars):
            payload = {"error": "Invalid characters in expression."}
            out = json.dumps(payload)
            return out
        try:
            result = round(float(eval(expression, {"__builtins__": None}, {})), 2)
            return str(result)
        except Exception as e:
            payload = {"error": str(e)}
            out = json.dumps(payload)
            return out
    
    @staticmethod
    def get_info() -> dict[str, Any]:
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
                            "description": "The mathematical expression to evaluate (e.g., '155 + 225 + 70').",
                        }
                    },
                    "required": ["expression"],
                },
            },
        }
