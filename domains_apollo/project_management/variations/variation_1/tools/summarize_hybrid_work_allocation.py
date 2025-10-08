from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class SummarizeHybridWorkAllocation(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], project_id: str = None) -> str:
        if not project_id:
            payload = {"error": "project_id is required"}
            out = json.dumps(payload)
            return out

        allocations = data.get("allocations", [])
        employees = data.get("employees", [])

        project_allocations = [
            alloc
            for alloc in allocations
            if alloc.get("project_id") == project_id and alloc.get("status") == "active"
        ]

        total_hours = 0
        onsite_hours = 0
        remote_work_maintained = True

        for allocation in project_allocations:
            employee_id = allocation.get("employee_id")
            hours = allocation.get("hours_per_week", 0)
            role = allocation.get("role", "").lower()

            total_hours += hours

            employee = next(
                (emp for emp in employees if emp.get("employee_id") == employee_id),
                None,
            )

            if employee:
                work_location_preference = employee.get(
                    "work_location_preference", "remote"
                )
                can_work_onsite = employee.get("can_work_onsite", True)

                is_onsite_allocation = False

                if "onsite" in role:
                    is_onsite_allocation = True

                    if work_location_preference == "remote" and not can_work_onsite:
                        remote_work_maintained = False
                elif work_location_preference == "onsite":
                    is_onsite_allocation = True
                elif work_location_preference == "hybrid":

                    is_onsite_allocation = True
                    onsite_hours += hours * 0.5
                    continue

                if is_onsite_allocation:
                    onsite_hours += hours

        onsite_percentage = (
            round(onsite_hours / total_hours * 100) if total_hours > 0 else 0
        )
        payload = {
                "project_id": project_id,
                "onsite_percentage": onsite_percentage,
                "remote_work_maintained": remote_work_maintained,
                "total_hours": total_hours,
                "onsite_hours": onsite_hours,
                "hybrid_work_summary": {
                    "total_project_hours": total_hours,
                    "onsite_hours": onsite_hours,
                    "onsite_percentage": onsite_percentage,
                    "remote_agreements_respected": remote_work_maintained,
                    "status": "calculated",
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
                "name": "summarizeHybridWorkAllocation",
                "description": "Calculate and summarize onsite vs remote work allocation percentages for a project",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {
                            "type": "string",
                            "description": "The project ID to analyze",
                        }
                    },
                    "required": ["project_id"],
                },
            },
        }
