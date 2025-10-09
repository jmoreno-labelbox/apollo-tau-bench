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

class UpdateDepartmentsUtilization(Tool):
    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        departments = data.get("departments", {}).values()
        employees = data.get("employees", {}).values()
        allocations = data.get("allocations", {}).values()
        employee_info = {}
        department_info = {}
        for employee in employees.values():
            department = employee["department"]
            employee_info[employee["employee_id"]] = department
            if department in department_info:
                department_info[department]["total_capacity_hours"] += employee[
                    "max_hours_per_week"
                ]
                department_info[department]["employee_count"] += 1
            else:
                department_info[department] = {
                    "total_capacity_hours": employee["max_hours_per_week"],
                    "employee_count": 1,
                }

        for allocation in allocations.values():
            employee_id = allocation["employee_id"]
            department = employee_info.get(employee_id)
            if department in department_info:
                if "allocated_hours" in department_info[department]:
                    department_info[department]["allocated_hours"] += allocation[
                        "hours_per_week"
                    ]
                else:
                    department_info[department]["allocated_hours"] = allocation[
                        "hours_per_week"
                    ]
            else:
                department_info[department] = {
                    "allocated_hours": allocation["hours_per_week"]
                }

        for department in departments.values():
            department_name = department["department_name"]
            if department_name in department_info:
                department["total_capacity_hours"] = department_info.get(
                    department_name, {}
                ).get("total_capacity_hours", 0)
                department["allocated_hours"] = department_info.get(
                    department_name, {}
                ).get("allocated_hours", 0)
                department["employee_count"] = department_info.get(
                    department_name, {}
                ).get("employee_count", 0)
                department["available_hours"] = (
                    department["total_capacity_hours"] - department["allocated_hours"]
                )
                department["avg_utilization"] = (
                    department["allocated_hours"] / department["employee_count"]
                )
        payload = {
                "success": True,
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateDepartmentsUtilization",
                "description": "Update departments main metrics",
                "parameters": {},
            },
        }
