# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateCapacityPlan(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], warehouse_id: str, optimization_strategy: str) -> str:
        plan_id = f"CAP-{warehouse_id}"

        capacity_plan = {
            "plan_id": plan_id,
            "warehouse_id": warehouse_id,
            "optimization_strategy": optimization_strategy,
            "created_date": get_current_timestamp(),
            "recommendations": [
                "Redistribute slow-moving inventory",
                "Optimize storage layout",
                "Consider seasonal adjustments"
            ],
            "expected_efficiency_gain": "15%",
            "implementation_timeline": "30_days"
        }

        if "capacity_plans" not in data:
            data["capacity_plans"] = []
        data["capacity_plans"].append(capacity_plan)

        return json.dumps({
            "plan_id": plan_id,
            "status": "Created",
            "optimization_strategy": optimization_strategy
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_capacity_plan",
                "description": "Create warehouse capacity optimization plan",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "warehouse_id": {"type": "string", "description": "Warehouse identifier"},
                        "optimization_strategy": {"type": "string", "description": "Optimization strategy to apply"}
                    },
                    "required": ["warehouse_id", "optimization_strategy"]
                }
            }
        }
