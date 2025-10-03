from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any, Dict
from datetime import timedelta

class ComputeNetCashFlow(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], inflows: float, outflows: float) -> str:
        """
        Compute net cash flow from inflows and outflows.
        Returns inflows, outflows, and net result.
        """
        net = round(inflows - outflows, 2)

        return json.dumps({
            "inflows": inflows,
            "outflows": outflows,
            "net": net
        })
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ComputeNetCashFlow",
                "description": "Compute net cash flow from inflows and outflows.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "inflows": {"type": "number", "description": "Sum of expected inflows"},
                        "outflows": {"type": "number", "description": "Sum of expected outflows"}
                    },
                    "required": ["inflows", "outflows"],
                },
            },
        }
