# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SummarizeOptimizationResults(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employees_optimized = [], optimization_actions = []) -> str:

        utilization_optimized = (
            len(optimization_actions) > 0 or len(employees_optimized) > 0
        )
        resources_balanced = utilization_optimized

        return json.dumps(
            {
                "utilization_optimized": utilization_optimized,
                "resources_balanced": resources_balanced,
                "optimization_summary": {
                    "actions_performed": optimization_actions,
                    "employees_affected": employees_optimized,
                    "status": "completed"
                    if utilization_optimized
                    else "no_optimization_needed",
                },
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "summarize_optimization_results",
                "description": "Generate a summary of resource utilization optimization results",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "optimization_actions": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of optimization actions performed",
                        },
                        "employees_optimized": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of employee IDs that were optimized",
                        },
                    },
                },
            },
        }
