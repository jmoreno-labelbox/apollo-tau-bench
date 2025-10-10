# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CalculateInventoryVariance(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], instruction_count, physical_count, sku, system_count, instruction_system_count = 0) -> str:

        if instruction_count:
            physical_count = instruction_count

        if instruction_system_count:
            system_count = instruction_system_count

        if system_count == 0:
            variance_percentage = 0
        else:
            variance_percentage = abs((physical_count - system_count) / system_count) * 100

        variance = physical_count - system_count

        variance_analysis = {
            "sku": sku,
            "system_count": system_count,
            "physical_count": physical_count,
            "variance": variance,
            "variance_percentage": round(variance_percentage, 2),
            "variance_threshold_exceeded": variance_percentage > 2.0,
            "analysis_date": get_current_timestamp()
        }

        return json.dumps(variance_analysis)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_inventory_variance",
                "description": "Calculate variance between system and physical inventory counts",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {"type": "string", "description": "Product SKU"},
                        "system_count": {"type": "integer", "description": "System inventory count"},
                        "physical_count": {"type": "integer", "description": "Physical inventory count"},
                        "instruction_count": {"type": "integer", "description": "Instruction count"},
                        "instruction_system_count": {"type": "integer", "description": "Instruction system count"}
                    },
                    "required": ["sku"]
                }
            }
        }
