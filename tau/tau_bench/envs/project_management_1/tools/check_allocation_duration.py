# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CheckAllocationDuration(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        employee_id = kwargs.get("employee_id")
        project_id = kwargs.get("project_id")

        if not all([employee_id, project_id]):
            return json.dumps({"error": "employee_id and project_id are required"})

        allocations = data.get("allocations", [])

        for allocation in allocations:
            if (
                allocation.get("employee_id") == employee_id
                and allocation.get("project_id") == project_id
            ):
                start_date = datetime.fromisoformat(allocation.get("start_date"))
                duration_days = (datetime.now() - start_date).days
                duration_months = duration_days / 30

                return json.dumps(
                    {
                        "employee_id": employee_id,
                        "project_id": project_id,
                        "start_date": allocation.get("start_date"),
                        "duration_days": duration_days,
                        "duration_months": round(duration_months, 1),
                    }
                )

        return json.dumps({"error": "Allocation not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "check_allocation_duration",
                "description": "Check how long an employee has been allocated to a project",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The employee ID",
                        },
                        "project_id": {
                            "type": "string",
                            "description": "The project ID",
                        },
                    },
                    "required": ["employee_id", "project_id"],
                },
            },
        }
