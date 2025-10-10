# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateDepartmentsUtilization(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:

        departments = list(data.get("departments", {}).values())
        employees = list(data.get("employees", {}).values())
        allocations = data.get("allocations", [])
        employee_info = {}
        department_info = {}
        for employee in employees:
            department = employee["department"]
            employee_info[employee["employee_id"]] = department
            if department in department_info:
                department_info[department]["total_capacity_hours"] += employee["max_hours_per_week"]
                department_info[department]["employee_count"] += 1
            else:
                department_info[department] = {
                    "total_capacity_hours": employee["max_hours_per_week"],
                    "employee_count": 1
                }

        for allocation in allocations:
            employee_id = allocation["employee_id"]
            department = employee_info.get(employee_id)
            if department in department_info:
                if "allocated_hours" in department_info[department]:
                    department_info[department]["allocated_hours"] += allocation["hours_per_week"]
                else:
                    department_info[department]["allocated_hours"] = allocation["hours_per_week"]
            else:
                department_info[department] = {"allocated_hours": allocation["hours_per_week"]}

        for department in departments:
            department_name = department["department_name"]
            if department_name in department_info:
                department["total_capacity_hours"] = department_info.get(department_name, {}).get("total_capacity_hours", 0)
                department["allocated_hours"] = department_info.get(department_name, {}).get("allocated_hours", 0)
                department["employee_count"] = department_info.get(department_name, {}).get("employee_count", 0)
                department["available_hours"] = department["total_capacity_hours"] - department["allocated_hours"]
                department["avg_utilization"] = department["allocated_hours"] / department["employee_count"]

        return json.dumps({"success": True, })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_departments_utilization",
                "description": "Update departments main metrics",
                "parameters": {},
            },
        }
