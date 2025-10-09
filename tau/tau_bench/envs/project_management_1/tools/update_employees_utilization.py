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

class UpdateEmployeesUtilization(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_ids: list[str] = None) -> str:
        if not employee_ids:
            payload = {"error": "employee_ids is required"}
            out = json.dumps(payload)
            return out

        employees = data.get("employees", {}).values()
        employee_info = {
            info["employee_id"]: {
                "index": i,
                "max_hours_per_week": info["max_hours_per_week"],
            }
            for i, info in enumerate(employees.values())
        }

        allocations = data.get("allocations", {}).values()

        utilization_per_employee = {}
        for allocation in allocations.values():
            employee_id = allocation.get("employee_id")
            if employee_id not in employee_ids:
                continue
            project_id = allocation.get("project_id")
            hours = allocation.get("hours_per_week")
            if employee_id in utilization_per_employee:
                utilization_per_employee[employee_id]["project_allocations"] += [
                    {"project_id": project_id, "hours": hours},
                ]
                utilization_per_employee[employee_id]["total_hours"] += hours
                utilization_per_employee[employee_id]["utilization_percentage"] = int(
                    utilization_per_employee[employee_id]["total_hours"]
                    * 100
                    / employee_info[employee_id]["max_hours_per_week"]
                )
            else:
                utilization_per_employee[employee_id] = {
                    "log_id": f"log_{uuid.uuid4().hex[:8]}",
                    "employee_id": employee_id,
                    "week": "current",
                    "project_allocations": [
                        {"project_id": project_id, "hours": hours},
                    ],
                    "total_hours": hours,
                    "utilization_percentage": int(
                        hours * 100 / employee_info[employee_id]["max_hours_per_week"]
                    ),
                }

        new_utilization_logs = []
        for employee_id, utilization_info in utilization_per_employee.items():
            if employee_id not in employee_ids:
                continue
            new_utilization_logs.append(utilization_info)
            employees[employee_info[employee_id]["index"]]["current_utilization"] = (
                utilization_info
            )["utilization_percentage"]

        data["utilization_logs"] = new_utilization_logs
        payload = {"success": True, "utilization_logs": new_utilization_logs}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateEmployeesUtilization",
                "description": "Update utilization log and employees current utilization with information "
                "from allocations",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of employee IDs",
                        }
                    },
                    "required": ["employee_ids"],
                },
            },
        }
