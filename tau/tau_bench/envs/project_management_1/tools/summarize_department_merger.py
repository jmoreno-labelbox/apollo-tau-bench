from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class SummarizeDepartmentMerger(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        merged_departments: list = None,
        new_department_name: str = None,
        teams_consolidated: list = None,
        final_utilization: float = None,
        employees_affected: list = None
    ) -> str:
        if merged_departments is None:
            merged_departments = []
        if teams_consolidated is None:
            teams_consolidated = []
        if employees_affected is None:
            employees_affected = []

        if not all([merged_departments, new_department_name]):
            payload = {"error": "merged_departments and new_department_name are required"}
            out = json.dumps(payload)
            return out

        if final_utilization is None and employees_affected:
            employees = data.get("employees", {}).values()
            total_hours = 0
            total_capacity = 0

            for emp_id in employees_affected.values():
                for employee in employees.values():
                    if employee.get("employee_id") == emp_id:
                        total_capacity += 40
                        total_hours += (
                            employee.get("current_utilization", 0) / 100
                        ) * 40
                        break

            if total_capacity > 0:
                final_utilization = round((total_hours / total_capacity) * 100, 1)

        payload = {
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
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "summarizeDepartmentMerger",
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
