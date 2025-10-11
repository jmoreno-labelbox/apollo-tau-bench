# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CalculateROAS(Tool):
    """Calculates Return on Ad Spend (ROAS) from revenue and spend."""

    @staticmethod
    def invoke(data: Dict[str, Any], revenue, spend) -> str:
        
        if revenue is None or spend is None:
            return json.dumps({"error": "revenue and spend are required parameters."})
        
        if spend == 0:
            return json.dumps({"error": "spend cannot be zero."})
        
        roas = revenue / spend
        return json.dumps({"roas": roas})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_roas",
                "description": "Calculates Return on Ad Spend (ROAS) from revenue and spend.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "revenue": {
                            "type": "number",
                            "description": "The revenue generated.",
                        },
                        "spend": {
                            "type": "number",
                            "description": "The amount spent.",
                        }
                    },
                    "required": ["revenue", "spend"],
                },
            },
        }
