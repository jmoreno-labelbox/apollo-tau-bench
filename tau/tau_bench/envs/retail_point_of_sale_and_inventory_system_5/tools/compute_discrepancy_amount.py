# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ComputeDiscrepancyAmount(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], physical_count, system_count, unit_cost) -> str:
        system_count = int(system_count)
        physical_count = int(physical_count)
        unit_cost = float(unit_cost)
        discrepancy_amount = abs(system_count - physical_count) * unit_cost
        return json.dumps({"discrepancy_amount": discrepancy_amount}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "compute_discrepancy_amount",
                "description": "Compute discrepancy amount based on counts and unit cost",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "system_count": {"type": "integer"},
                        "physical_count": {"type": "integer"},
                        "unit_cost": {"type": "number"}
                    },
                    "required": ["system_count", "physical_count", "unit_cost"]
                }
            }
        }