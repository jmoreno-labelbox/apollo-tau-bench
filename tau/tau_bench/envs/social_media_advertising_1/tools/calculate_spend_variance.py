# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CalculateSpendVariance(Tool):
    """Calculates the variance percentage between planned and actual spend."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        planned_spend = kwargs.get("planned_spend")
        actual_spend = kwargs.get("actual_spend")
        
        if planned_spend is None or actual_spend is None:
            return json.dumps({"error": "planned_spend and actual_spend are required parameters."})
        
        if planned_spend == 0:
            return json.dumps({"error": "planned_spend cannot be zero."})
        
        variance_percent = ((actual_spend - planned_spend) / planned_spend) * 100
        return json.dumps({"variance_percent": variance_percent})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_spend_variance",
                "description": "Calculates the variance percentage between planned and actual spend.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "planned_spend": {
                            "type": "number",
                            "description": "The planned spend amount.",
                        },
                        "actual_spend": {
                            "type": "number",
                            "description": "The actual spend amount.",
                        }
                    },
                    "required": ["planned_spend", "actual_spend"],
                },
            },
        }
