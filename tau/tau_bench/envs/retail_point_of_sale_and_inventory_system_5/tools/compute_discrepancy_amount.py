# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ComputeDiscrepancyAmount(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        system_count = int(kwargs["system_count"])
        physical_count = int(kwargs["physical_count"])
        unit_cost = float(kwargs["unit_cost"])
        discrepancy_amount = abs(system_count - physical_count) * unit_cost
        return json.dumps({"discrepancy_amount": discrepancy_amount}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
                "name": "compute_discrepancy_amount",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "system_count": {"type": "integer"},
                        "physical_count": {"type": "integer"},
                        "unit_cost": {"type": "number"}
                    }
                }