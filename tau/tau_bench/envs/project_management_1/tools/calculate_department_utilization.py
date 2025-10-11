# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CalculateDepartmentUtilization(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], department) -> str:
        if not department:
            return json.dumps({"error": "department is required"})

        result = GetDepartmentCapacity.invoke(data, department=department)
        dept_data = json.loads(result)

        return json.dumps(
            {
                "department": department,
                "dept_utilization": dept_data.get("utilization_percentage", 0),
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_department_utilization",
                "description": "Calculate overall department utilization",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "department": {
                            "type": "string",
                            "description": "Department name",
                        }
                    },
                    "required": ["department"],
                },
            },
        }
