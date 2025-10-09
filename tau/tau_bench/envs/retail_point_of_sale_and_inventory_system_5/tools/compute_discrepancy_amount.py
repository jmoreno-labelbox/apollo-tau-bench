from tau_bench.envs.tool import Tool
import hashlib
import json
from typing import Any

class ComputeDiscrepancyAmount(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], system_count: int, physical_count: int, unit_cost: float) -> str:
        discrepancy_amount = abs(system_count - physical_count) * unit_cost
        payload = {"discrepancy_amount": discrepancy_amount}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ComputeDiscrepancyAmount",
                "parameters": {
                    "system_count": {"type": "integer"},
                    "physical_count": {"type": "integer"},
                    "unit_cost": {"type": "number"},
                },
                "required": ["system_count", "physical_count", "unit_cost"],
            },
        }
