# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SummarizeDepartmentMerger(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        merged_departments = kwargs.get("merged_departments", [])
        new_department_name = kwargs.get("new_department_name")
        teams_consolidated = kwargs.get("teams_consolidated", [])
        final_utilization = kwargs.get("final_utilization")
        employees_affected = kwargs.get("employees_affected", [])

        if not all([merged_departments, new_department_name]):
            return json.dumps(
                {"error": "merged_departments and new_department_name are required"}
            )

        if final_utilization is None and employees_affected:
            employees = list(data.get("employees", {}).values())
            total_hours = 0
            total_capacity = 0

            for emp_id in employees_affected:
                for employee in employees:
                    if employee.get("employee_id") == emp_id:
                        total_capacity += 40
                        total_hours += (
                            employee.get("current_utilization", 0) / 100
                        ) * 40
                        break

            if total_capacity > 0:
                final_utilization = round((total_hours / total_capacity) * 100, 1)

        return json.dumps(
            {
                "merged_department_utilization": final_utilization,
                "teams_consolidated": len(teams_consolidated),
                "merger_summary": {
                    "departments_merged": merged_departments,
                    "new_department": new_department_name,
                    "teams_affected": teams_consolidated,
                    "employees_in_new_dept": len(employees_affected),
                    "status": "completed",
                },
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "summarize_department_merger",
                "description": "Generate a summary of department merger operations",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "merged_departments": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of department names that were merged",
                        },
                        "new_department_name": {
                            "type": "string",
                            "description": "Name of the new merged department",
                        },
                        "teams_consolidated": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of team IDs that were consolidated",
                        },
                        "final_utilization": {
                            "type": "number",
                            "description": "Final utilization percentage of merged department",
                        },
                        "employees_affected": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of employee IDs in the merged department",
                        },
                    },
                    "required": ["merged_departments", "new_department_name"],
                },
            },
        }
