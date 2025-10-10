# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CalculateCPA(Tool):
    """Calculates Cost Per Acquisition (CPA) from spend and purchases."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        spend = kwargs.get("spend")
        purchases = kwargs.get("purchases")
        
        if spend is None or purchases is None:
            return json.dumps({"error": "spend and purchases are required parameters."})
        
        if purchases == 0:
            return json.dumps({"error": "purchases cannot be zero."})
        
        cpa = spend / purchases
        return json.dumps({"cpa": cpa})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_cpa",
                "description": "Calculates Cost Per Acquisition (CPA) from spend and purchases.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "spend": {
                            "type": "number",
                            "description": "The amount spent.",
                        },
                        "purchases": {
                            "type": "number",
                            "description": "The number of purchases.",
                        }
                    },
                    "required": ["spend", "purchases"],
                },
            },
        }
