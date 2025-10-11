# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchEmployees(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], clearance, department, min_available_hours, name, role, role_contains, role_disregard, skills, utilization_above, utilization_below, disregard_employee_ids = [], min_proficiency = 0, min_skill_matches = 1) -> str:
        required_skills = skills
        disregard_employees = disregard_employee_ids


        employees = list(data.get("employees", {}).values())
        results = []

        for employee in employees:

            if name and name.lower() not in employee.get("name", "").lower():
                continue

            if department and employee.get("department") != department:
                continue

            if role and employee.get("role") != role:
                continue

            if employee.get("employee_id") in disregard_employees:
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

            if required_skills:
                employee_skills = employee.get("skills", [])
                skills_matches = {
                    info["skill"] for info in employee_skills
                    if info["skill"] in required_skills and info.get("proficiency", 0) >= min_proficiency
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
                available_hours = (employee.get("max_hours_per_week", 0) *
                                   (100 - employee.get("current_utilization", 0)) / 100)
                if available_hours < min_available_hours:
                    continue

            results.append(employee)

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_employees",
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
