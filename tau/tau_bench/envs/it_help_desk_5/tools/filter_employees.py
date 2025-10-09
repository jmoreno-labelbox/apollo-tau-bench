from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class FilterEmployees(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        first_name: str = None,
        last_name: str = None,
        department: str = None,
        job_title: str = None,
        manager_id: str = None,
        status: str = None
    ) -> str:
        employees = data.get("employees")

        if all(
            [
                attribute is None
                for attribute in [
                    first_name,
                    last_name,
                    department,
                    job_title,
                    manager_id,
                    status,
                ]
            ]
        ):
            payload = {"status": "error", "reason": "No criteria specified"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        temp_employees = employees.copy()

        if first_name is not None:
            temp_employees = [
                employee
                for employee in temp_employees
                if employee["first_name"] == first_name
            ]

        if last_name is not None:
            temp_employees = [
                employee
                for employee in temp_employees
                if employee["last_name"] == last_name
            ]

        if department is not None:
            temp_employees = [
                employee
                for employee in temp_employees
                if employee["department"] == department
            ]

        if job_title is not None:
            temp_employees = [
                employee
                for employee in temp_employees
                if employee["job_title"] == job_title
            ]

        if manager_id is not None and manager_id != "None":
            temp_employees = [
                employee
                for employee in temp_employees
                if employee["manager_id"] == manager_id
            ]

        if manager_id is not None and manager_id == "None":
            temp_employees = [
                employee
                for employee in temp_employees
                if employee["manager_id"] is None
            ]

        if status is not None:
            temp_employees = [
                employee for employee in temp_employees if employee["status"] == status
            ]
        payload = temp_employees
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "filterEmployees",
                "description": "Finds employees based on certain criteria.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "first_name": {
                            "type": "string",
                            "description": "The first name to search for.",
                        },
                        "last_name": {
                            "type": "string",
                            "description": "The last name to search for.",
                        },
                        "department": {
                            "type": "string",
                            "description": "The department to search for.",
                        },
                        "job_title": {
                            "type": "string",
                            "description": "The job title to search for.",
                        },
                        "manager_id": {
                            "type": "string",
                            "description": "The manager to search for.",
                        },
                        "status": {
                            "type": "string",
                            "description": "The status to search for.",
                        },
                    },
                },
            },
        }
