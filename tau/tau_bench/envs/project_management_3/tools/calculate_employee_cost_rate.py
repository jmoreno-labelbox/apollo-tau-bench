from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CalculateEmployeeCostRate(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None, include_overhead: bool = True) -> str:
        if not employee_id:
            payload = {"error": "employee_id is required"}
            out = json.dumps(payload)
            return out

        employees = data.get("employees", {}).values()
        allocations = data.get("allocations", {}).values()

        employee = next(
            (e for e in employees.values() if e.get("employee_id") == employee_id), None
        )
        if not employee:
            payload = {"error": f"Employee {employee_id} not found"}
            out = json.dumps(payload)
            return out

        role = employee.get("role", "").lower()
        department = employee.get("department", "")

        if "architect" in role:
            base_rate = 200
        elif "senior" in role or "lead" in role:
            base_rate = 175
        elif "junior" in role:
            base_rate = 75
        else:
            base_rate = 100

        skills = employee.get("skills", [])
        max_proficiency = max((s.get("proficiency", 0) for s in skills.values()), default=3)
        skill_multiplier = 1 + (max_proficiency - 3) * 0.1

        adjusted_rate = base_rate * skill_multiplier

        if include_overhead:
            overhead_rate = adjusted_rate * 0.35
            fully_loaded_rate = adjusted_rate + overhead_rate
        else:
            fully_loaded_rate = adjusted_rate

        active_allocations = [
            a
            for a in allocations.values() if a.get("employee_id") == employee_id and a.get("status") == "active"
        ]
        total_hours = sum(a.get("hours_per_week", 0) for a in active_allocations.values()

        cost_rates = {
            "weekly_rate": round(fully_loaded_rate * 40, 2),
            "employee_id": employee_id,
            "employee_name": employee["name"],
            "role": employee["role"],
            "department": department,
            "cost_rates": {
                "base_hourly_rate": round(base_rate, 2),
                "skill_adjusted_rate": round(adjusted_rate, 2),
                "fully_loaded_rate": round(fully_loaded_rate, 2),
                "daily_rate": round(fully_loaded_rate * 8, 2),
                "weekly_rate": round(fully_loaded_rate * 40, 2),
                "monthly_rate": round(fully_loaded_rate * 173.33, 2),
                "annual_rate": round(fully_loaded_rate * 2080, 2),
            },
            "current_utilization": {
                "allocated_hours_per_week": total_hours,
                "utilization_percentage": round((total_hours / 40 * 100), 1),
                "weekly_cost": round(total_hours * fully_loaded_rate, 2),
            },
        }
        payload = cost_rates
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateEmployeeCostRate",
                "description": "Calculate cost rates for an employee based on role and skills",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string", "description": "Employee ID"},
                        "include_overhead": {
                            "type": "boolean",
                            "description": "Include overhead costs (default: true)",
                        },
                    },
                    "required": ["employee_id"],
                },
            },
        }
