# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CalculateSum(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        val = kwargs.get("values")
        total = 0
        if val:
            total = sum([float(v) for v in val])

        return json.dumps({"total": f"{total}"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "calculate_sum",
                        "description": "Calculate the total sum for a list of numerical values.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "values": {"type": "array", "description": "The values to sum up."}
                                },
                                "required": ["values"],
                        },
                },
        }
