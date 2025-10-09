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

class SearchEmployees(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        name: str = None,
        skills: list[str] = None,
        min_skill_matches: int = 1,
        department: str = None,
        role: str = None,
        role_contains: str = None,
        role_disregard: str = None,
        clearance: str = None,
        utilization_below: float = None,
        utilization_above: float = None,
        min_proficiency: int = 0,
        min_available_hours: float = None,
        disregard_employee_ids: list[int] = []
    ) -> str:
        employees = data.get("employees", {}).values()
        results = []

        for employee in employees.values():

            if name and name.lower() not in employee.get("name", "").lower():
                continue

            if department and employee.get("department") != department:
                continue

            if role and employee.get("role") != role:
                continue

            if employee.get("employee_id") in disregard_employee_ids:
                continue

            if (
                role_contains
                and role_contains.lower() not in employee.get("role", "").lower()
            ):
                continue

            if (
                role_disregard
                and role_disregard.lower() in employee.get("role", "").lower()
            ):
                continue

            if clearance and employee.get("clearance") != clearance:
                continue

            if skills:
                employee_skills = employee.get("skills", [])
                skills_matches = {
                    info["skill"]
                    for info in employee_skills
                    if info["skill"] in skills
                    and info.get("proficiency", 0) >= min_proficiency
                }
                if len(skills_matches) < min_skill_matches:
                    continue

            if utilization_below:
                current_util = employee.get("current_utilization", 0)
                if current_util > utilization_below:
                    continue

            if utilization_above is not None:
                current_util = employee.get("current_utilization", 0)
                if current_util <= utilization_above:
                    continue

            if min_available_hours:
                available_hours = (
                    employee.get("max_hours_per_week", 0)
                    * (100 - employee.get("current_utilization", 0))
                    / 100
                )
                if available_hours < min_available_hours:
                    continue

            results.append(employee)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchEmployees",
                "description": "Search for employees by name, skill, department, role, security clearance, or utilization levels",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Employee name to search for",
                        },
                        "skill": {
                            "type": "string",
                            "description": "Skill name to filter by",
                        },
                        "department": {
                            "type": "string",
                            "description": "Department to filter by",
                        },
                        "role": {
                            "type": "string",
                            "description": "Exact role to filter by",
                        },
                        "role_contains": {
                            "type": "string",
                            "description": "Partial role match",
                        },
                        "clearance": {
                            "type": "string",
                            "description": "Security clearance level",
                        },
                        "utilization_below": {
                            "type": "number",
                            "description": "Find employees with utilization below this value",
                        },
                        "utilization_above": {
                            "type": "number",
                            "description": "Find employees with utilization above this value",
                        },
                        "min_proficiency": {
                            "type": "number",
                            "description": "Minimum skill proficiency level",
                        },
                    },
                },
            },
        }
