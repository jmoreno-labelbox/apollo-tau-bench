# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GenerateDepartmentFinancialReport(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        department_name = kwargs.get("department_name")
        fiscal_year = kwargs.get("fiscal_year", datetime.now().year)
        include_employee_costs = kwargs.get("include_employee_costs", True)

        if not department_name:
            return json.dumps({"error": "department_name is required"})

        departments = list(data.get("departments", {}).values())
        projects = list(data.get("projects", {}).values())
        budgets = data.get("budgets", [])
        employees = list(data.get("employees", {}).values())
        allocations = data.get("allocations", [])
        expenses = data.get("expenses", [])

        department = next(
            (d for d in departments if d.get("department_name") == department_name),
            None,
        )
        if not department:
            return json.dumps({"error": f"Department {department_name} not found"})

        dept_projects = [p for p in projects if p.get("department") == department_name]

        total_budget = 0
        total_spent = 0
        total_committed = 0
        project_summaries = []

        for project in dept_projects:
            project_budget = next(
                (
                    b
                    for b in budgets
                    if b.get("project_id") == project["project_id"]
                    and b.get("fiscal_year") == fiscal_year
                ),
                None,
            )
            if project_budget:
                total_budget += project_budget["total_budget"]
                total_spent += project_budget.get("spent_amount", 0)
                total_committed += project_budget.get("committed_amount", 0)

                project_summaries.append(
                    {
                        "project_id": project["project_id"],
                        "project_name": project["name"],
                        "priority": project["priority"],
                        "budget": project_budget["total_budget"],
                        "spent": project_budget.get("spent_amount", 0),
                        "utilization": round(
                            (
                                project_budget.get("spent_amount", 0)
                                / project_budget["total_budget"]
                                * 100
                            ),
                            2,
                        ),
                    }
                )

        employee_costs = {}
        if include_employee_costs:
            dept_employees = [
                e for e in employees if e.get("department") == department_name
            ]

            for employee in dept_employees:

                emp_allocations = [
                    a
                    for a in allocations
                    if a.get("employee_id") == employee["employee_id"]
                    and a.get("status") == "active"
                ]

                total_hours = sum(a.get("hours_per_week", 0) for a in emp_allocations)
                hourly_rate = (
                    150 if "senior" in employee.get("role", "").lower() else 100
                )

                employee_costs[employee["employee_id"]] = {
                    "name": employee["name"],
                    "role": employee["role"],
                    "utilization": employee.get("current_utilization", 0),
                    "allocated_hours": total_hours,
                    "weekly_cost": total_hours * hourly_rate,
                    "annual_cost": total_hours * hourly_rate * 52,
                }

        avg_utilization = department.get("avg_utilization", 0)
        capacity_efficiency = (
            department.get("allocated_hours", 0)
            / department.get("total_capacity_hours", 1)
            * 100
        )

        report = {
            "department": department_name,
            "fiscal_year": fiscal_year,
            "financial_summary": {
                "total_budget": total_budget,
                "total_spent": total_spent,
                "total_committed": total_committed,
                "available": total_budget - total_spent - total_committed,
                "budget_utilization": round((total_spent / total_budget * 100), 2)
                if total_budget > 0
                else 0,
            },
            "project_count": len(dept_projects),
            "project_breakdown": project_summaries,
            "department_metrics": {
                "employee_count": department.get("employee_count", 0),
                "average_utilization": avg_utilization,
                "capacity_efficiency": round(capacity_efficiency, 2),
                "total_capacity_hours": department.get("total_capacity_hours", 0),
                "allocated_hours": department.get("allocated_hours", 0),
            },
            "high_priority_projects": len(
                [p for p in dept_projects if p.get("priority") == "critical"]
            ),
            "projects_over_budget": len(
                [p for p in project_summaries if p["utilization"] > 90]
            ),
            "report_generated": datetime.now().isoformat(),
        }

        if include_employee_costs:
            report["employee_costs"] = employee_costs
            report["total_employee_cost"] = sum(
                e["annual_cost"] for e in employee_costs.values()
            )

        return json.dumps(report, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generate_department_financial_report",
                "description": "Generate comprehensive financial report for a department",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "department_name": {
                            "type": "string",
                            "description": "Department name",
                        },
                        "fiscal_year": {
                            "type": "integer",
                            "description": "Fiscal year",
                        },
                        "include_employee_costs": {
                            "type": "boolean",
                            "description": "Include employee cost breakdown",
                        },
                    },
                    "required": ["department_name"],
                },
            },
        }
