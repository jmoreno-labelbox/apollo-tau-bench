from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class SummarizeOptimizationResults(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], optimization_actions: list = None, employees_optimized: list = None) -> str:
        if optimization_actions is None:
            optimization_actions = []
        if employees_optimized is None:
            employees_optimized = []

        utilization_optimized = (
            len(optimization_actions) > 0 or len(employees_optimized) > 0
        )
        resources_balanced = utilization_optimized
        payload = {
                "utilization_optimized": utilization_optimized,
                "resources_balanced": resources_balanced,
                "optimization_summary": {
                    "actions_performed": optimization_actions,
                    "employees_affected": employees_optimized,
                    "status": (
                        "completed"
                        if utilization_optimized
                        else "no_optimization_needed"
                    ),
                },
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "summarizeOptimizationResults",
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
