from tau_bench.envs.tool import Tool
import json
from datetime import date, datetime, time, timedelta, timezone
from typing import Any, Dict, List

class CalculateSum(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], values: list = None) -> str:
        total = 0
        if values:
            total = sum([float(v) for v in values])

        return json.dumps({"total": f"{total}"})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "CalculateSum",
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
