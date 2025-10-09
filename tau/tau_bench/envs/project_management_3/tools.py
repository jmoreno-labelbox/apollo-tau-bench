import json
import uuid
from datetime import datetime, timezone
from typing import Any

from tau_bench.envs.tool import Tool




def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db


class CreateProjectBudget(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        project_id: str = None,
        fiscal_year: int = None,
        total_budget: float = None,
        budget_categories: dict = None,
        budget_id: str = None
    ) -> str:
        if budget_categories is None:
            budget_categories = {}

        if not all([project_id, fiscal_year, total_budget]):
            payload = {"error": "project_id, fiscal_year, and total_budget are required"}
            out = json.dumps(payload)
            return out

        budgets = data.get("budgets", {}).values()
        projects = data.get("projects", {}).values()
        allocations = data.get("allocations", {}).values()
        employees = data.get("employees", {}).values()

        project = next((p for p in projects.values() if p.get("project_id") == project_id), None)
        if not project:
            payload = {"error": f"Project {project_id} not found"}
            out = json.dumps(payload)
            return out

        if project.get("status") not in ["active", "planning"]:
            payload = {
                "error": f"Cannot create budget for project with status: {project.get('status')}"
            }
            out = json.dumps(payload)
            return out

        project_allocations = [
            a
            for a in allocations.values() if a.get("project_id") == project_id and a.get("status") == "active"
        ]

        total_personnel_cost = 0
        for allocation in project_allocations:
            employee = next(
                (
                    e
                    for e in employees.values() if e.get("employee_id") == allocation.get("employee_id")
                ),
                None,
            )
            if employee:
                hourly_rate = (
                    150 if "senior" in employee.get("role", "").lower() else 100
                )
                weekly_cost = allocation.get("hours_per_week", 0) * hourly_rate

                duration_weeks = 26
                total_personnel_cost += weekly_cost * duration_weeks

        if total_personnel_cost > total_budget * 0.8:
            payload = {
                "error": f"Personnel costs (${total_personnel_cost}) exceed 80% of total budget. Increase budget or reduce allocations.",
                "suggested_budget": int(total_personnel_cost / 0.8),
            }
            out = json.dumps(payload)
            return out

        if budget_id is None:
            budget_id = f"budget_{uuid.uuid4().hex[:8]}"

        new_budget = {
            "budget_id": budget_id,
            "project_id": project_id,
            "fiscal_year": fiscal_year,
            "total_budget": total_budget,
            "personnel_budget": total_budget * 0.8,
            "non_personnel_budget": total_budget * 0.2,
            "allocated_personnel_cost": total_personnel_cost,
            "spent_amount": 0,
            "committed_amount": 0,
            "budget_categories": budget_categories,
            "status": "active",
            "created_date": datetime.now().isoformat(),
            "last_modified": datetime.now().isoformat(),
            "project_priority": project.get("priority"),
            "department": project.get("department"),
        }

        data["budgets"][budget_id] = new_budget
        payload = {"success": True, "budget": new_budget}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateProjectBudget",
                "description": "Create a new budget for a project based on team allocations",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "Project ID"},
                        "budget_id": {"type": "string", "description": "Budget ID"},
                        "fiscal_year": {
                            "type": "integer",
                            "description": "Fiscal year",
                        },
                        "total_budget": {
                            "type": "number",
                            "description": "Total budget amount",
                        },
                        "budget_categories": {
                            "type": "object",
                            "description": "Budget breakdown by category",
                        },
                    },
                    "required": ["project_id", "fiscal_year", "total_budget"],
                },
            },
        }


class CalculateProjectCost(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], project_id: str, include_planned: bool = True, as_of_date: str = None) -> str:
        if not project_id:
            payload = {"error": "project_id is required"}
            out = json.dumps(payload)
            return out

        allocations = data.get("allocations", {}).values()
        employees = data.get("employees", {}).values()
        tasks = data.get("tasks", {}).values()
        task_logs = data.get("task_logs", {}).values()
        expenses = data.get("expenses", {}).values()

        project_allocations = [
            a for a in allocations.values() if a.get("project_id") == project_id
        ]

        actual_personnel_cost = 0
        planned_personnel_cost = 0

        for allocation in project_allocations:
            employee = next(
                (
                    e
                    for e in employees.values() if e.get("employee_id") == allocation.get("employee_id")
                ),
                None,
            )
            if employee:

                hourly_rate = (
                    150 if "senior" in employee.get("role", "").lower() else 100
                )
                if "architect" in employee.get("role", "").lower():
                    hourly_rate = 200
                elif "junior" in employee.get("role", "").lower():
                    hourly_rate = 75

                employee_tasks = [
                    t
                    for t in tasks.values() if t.get("assignee_id") == employee["employee_id"]
                    and t.get("sprint_id")
                    and any(a.get("project_id") == project_id for a in allocations.values())
                ]

                actual_hours = 0
                for task in employee_tasks:
                    task_hours = sum(
                        log.get("hours", 0)
                        for log in task_logs.values() if log.get("task_id") == task["task_id"]
                    )
                    actual_hours += task_hours

                actual_personnel_cost += actual_hours * hourly_rate

                if include_planned:
                    weeks = 26
                    planned_personnel_cost += (
                        allocation.get("hours_per_week", 0) * hourly_rate * weeks
                    )

        project_expenses = [
            e
            for e in expenses.values() if e.get("project_id") == project_id and e.get("status") == "approved"
        ]
        non_personnel_cost = sum(e.get("amount", 0) for e in project_expenses.values())

        teams = data.get("teams", {}).values()
        project_teams = [t for t in teams.values() if t.get("project_id") == project_id]

        cost_breakdown = {
            "project_id": project_id,
            "actual_costs": {
                "personnel": actual_personnel_cost,
                "non_personnel": non_personnel_cost,
                "total": actual_personnel_cost + non_personnel_cost,
            },
            "planned_costs": (
                {
                    "personnel": planned_personnel_cost,
                    "total": planned_personnel_cost + (planned_personnel_cost * 0.25),
                }
                if include_planned
                else None
            ),
            "cost_per_story_point": 0,
            "team_count": len(project_teams),
            "allocation_count": len(project_allocations),
            "burn_rate_weekly": (
                actual_personnel_cost / 26 if actual_personnel_cost > 0 else 0
            ),
        }

        completed_story_points = sum(
            t.get("story_points", 0)
            for t in tasks.values() if t.get("status") == "done"
            and any(
                a.get("project_id") == project_id
                for a in allocations.values() if a.get("employee_id") == t.get("assignee_id")
            )
        )

        if completed_story_points > 0:
            cost_breakdown["cost_per_story_point"] = round(
                actual_personnel_cost / completed_story_points, 2
            )
        payload = cost_breakdown
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateProjectCost",
                "description": "Calculate actual and planned costs for a project based on team allocations and logged hours",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "Project ID"},
                        "include_planned": {
                            "type": "boolean",
                            "description": "Include planned costs",
                        },
                        "as_of_date": {
                            "type": "string",
                            "description": "Calculate as of specific date",
                        },
                    },
                    "required": ["project_id"],
                },
            },
        }


class ValidateExpenseSubmission(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        employee_id: str = None,
        project_id: str = None,
        amount: float = None,
        expense_date: str = None,
        category: str = None,
        sprint_id: str = None,
        task_id: str = None
    ) -> str:
        if not all([employee_id, project_id, amount, category]):
            payload = {"error": "employee_id, project_id, amount, and category are required"}
            out = json.dumps(payload)
            return out

        allocations = data.get("allocations", {}).values()
        projects = data.get("projects", {}).values()
        sprints = data.get("sprints", {}).values()
        tasks = data.get("tasks", {}).values()

        project = next((p for p in projects.values() if p.get("project_id") == project_id), None)
        if not project:
            payload = {"error": f"Project {project_id} not found"}
            out = json.dumps(payload)
            return out

        if project.get("status") in ["cancelled", "completed"]:
            payload = {"error": f"Cannot submit expense for {project.get('status')} project"}
            out = json.dumps(payload)
            return out

        employee_allocation = next(
            (
                a
                for a in allocations.values() if a.get("employee_id") == employee_id
                and a.get("project_id") == project_id
                and a.get("status") == "active"
            ),
            None,
        )

        if not employee_allocation:
            payload = {
                "error": f"Employee {employee_id} is not allocated to project {project_id}"
            }
            out = json.dumps(payload)
            return out

        allocation_percentage = employee_allocation.get("hours_per_week", 0) / 40
        base_limit = 1000
        adjusted_limit = base_limit * allocation_percentage

        validation_result = {
            "valid": True,
            "employee_id": employee_id,
            "project_id": project_id,
            "allocation_percentage": round(allocation_percentage * 100, 1),
            "reimbursement_limit": adjusted_limit,
            "warnings": [],
        }

        if sprint_id:
            sprint = next((s for s in sprints.values() if s.get("sprint_id") == sprint_id), None)
            if sprint:
                if sprint.get("status") != "active":
                    validation_result["warnings"].append(
                        f"Sprint {sprint_id} is not active"
                    )

                if expense_date:
                    expense_dt = datetime.fromisoformat(
                        expense_date.replace("Z", "+00:00")
                    )
                    sprint_start = datetime.fromisoformat(
                        sprint["start_date"].replace("Z", "+00:00")
                    )
                    sprint_end = datetime.fromisoformat(
                        sprint["end_date"].replace("Z", "+00:00")
                    )

                    if not (
                        sprint_start.timestamp()
                        <= expense_dt.timestamp()
                        <= sprint_end.timestamp()
                    ):
                        validation_result["warnings"].append(
                            "Expense date is outside sprint duration"
                        )

        if task_id:
            task = next((t for t in tasks.values() if t.get("task_id") == task_id), None)
            if task:
                if task.get("assignee_id") != employee_id:
                    validation_result["valid"] = False
                    validation_result["error"] = (
                        f"Task {task_id} is not assigned to employee {employee_id}"
                    )
                elif task.get("status") == "todo":
                    validation_result["warnings"].append(
                        "Task has not been started yet"
                    )

        if amount > adjusted_limit:
            validation_result["warnings"].append(
                f"Amount exceeds adjusted limit of ${adjusted_limit}"
            )
        payload = validation_result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ValidateExpenseSubmission",
                "description": "Validate expense submission against employee allocation and project rules",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string", "description": "Employee ID"},
                        "project_id": {"type": "string", "description": "Project ID"},
                        "amount": {"type": "number", "description": "Expense amount"},
                        "expense_date": {
                            "type": "string",
                            "description": "Date of expense",
                        },
                        "category": {
                            "type": "string",
                            "description": "Expense category",
                        },
                        "sprint_id": {
                            "type": "string",
                            "description": "Associated sprint ID",
                        },
                        "task_id": {
                            "type": "string",
                            "description": "Associated task ID",
                        },
                    },
                    "required": ["employee_id", "project_id", "amount", "category"],
                },
            },
        }


class GetTeamBudgetStatus(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], 
        team_id: str, 
        include_member_breakdown: bool = False, 
        fiscal_year: int = datetime.now().year
    ) -> str:
        if not team_id:
            payload = {"error": "team_id is required"}
            out = json.dumps(payload)
            return out

        teams = data.get("teams", {}).values()
        budgets = data.get("budgets", {}).values()
        expenses = data.get("expenses", {}).values()
        employees = data.get("employees", {}).values()
        task_logs = data.get("task_logs", {}).values()

        team = next((t for t in teams.values() if t.get("team_id") == team_id), None)
        if not team:
            payload = {"error": f"Team {team_id} not found"}
            out = json.dumps(payload)
            return out

        project_id = team.get("project_id")
        budget = next(
            (
                b
                for b in budgets.values() if b.get("project_id") == project_id
                and b.get("fiscal_year") == fiscal_year
            ),
            None,
        )

        if not budget:
            payload = {"error": f"No budget found for team's project {project_id}"}
            out = json.dumps(payload)
            return out

        team_members = team.get("members", [])
        member_costs = {}
        total_team_cost = 0

        for member_id in team_members:
            employee = next(
                (e for e in employees.values() if e.get("employee_id") == member_id), None
            )
            if employee:
                hourly_rate = (
                    150 if "senior" in employee.get("role", "").lower() else 100
                )
                if "lead" in employee.get("role", "").lower():
                    hourly_rate = 175

                member_logs = [
                    log for log in task_logs.values() if log.get("employee_id") == member_id
                ]
                total_hours = sum(log.get("hours", 0) for log in member_logs.values())
                member_cost = total_hours * hourly_rate

                member_costs[member_id] = {
                    "name": employee.get("name"),
                    "role": employee.get("role"),
                    "hourly_rate": hourly_rate,
                    "logged_hours": total_hours,
                    "total_cost": member_cost,
                }
                total_team_cost += member_cost

        team_expenses = [
            e
            for e in expenses.values() if e.get("employee_id") in team_members
            and e.get("project_id") == project_id
            and e.get("status") == "approved"
        ]

        total_expenses = sum(e.get("amount", 0) for e in team_expenses.values())

        status = {
            "budget_utilization": (
                round((total_team_cost / budget["personnel_budget"] * 100), 2)
                if budget["personnel_budget"] > 0
                else 0
            ),
            "team_id": team_id,
            "team_name": team.get("team_name"),
            "project_id": project_id,
            "budget_info": {
                "total_budget": budget["total_budget"],
                "personnel_budget": budget["personnel_budget"],
                "spent_amount": budget.get("spent_amount", 0),
                "available_amount": budget["total_budget"]
                - budget.get("spent_amount", 0),
            },
            "team_costs": {
                "personnel_cost": total_team_cost,
                "expense_cost": total_expenses,
                "total_cost": total_team_cost + total_expenses,
            },
            "cost_efficiency": {
                "cost_per_member": (
                    total_team_cost / len(team_members) if team_members else 0
                ),
                "budget_utilization": (
                    round((total_team_cost / budget["personnel_budget"] * 100), 2)
                    if budget["personnel_budget"] > 0
                    else 0
                ),
            },
        }

        if include_member_breakdown:
            status["member_breakdown"] = member_costs

        if status["cost_efficiency"]["budget_utilization"] > 80:
            status["warning"] = "Team personnel costs approaching budget limit"
        payload = status
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTeamBudgetStatus",
                "description": "Get budget status and cost breakdown for a team",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {"type": "string", "description": "Team ID"},
                        "include_member_breakdown": {
                            "type": "boolean",
                            "description": "Include individual member costs",
                        },
                        "fiscal_year": {
                            "type": "integer",
                            "description": "Fiscal year (defaults to current)",
                        },
                    },
                    "required": ["team_id"],
                },
            },
        }


class ReconcileSprintExpenses(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], sprint_id: str = None) -> str:
        if not sprint_id:
            payload = {"error": "sprint_id is required"}
            out = json.dumps(payload)
            return out

        sprints = data.get("sprints", {}).values()
        tasks = data.get("tasks", {}).values()
        task_logs = data.get("task_logs", {}).values()
        expenses = data.get("expenses", {}).values()
        employees = data.get("employees", {}).values()

        sprint = next((s for s in sprints.values() if s.get("sprint_id") == sprint_id), None)
        if not sprint:
            payload = {"error": f"Sprint {sprint_id} not found"}
            out = json.dumps(payload)
            return out

        if sprint.get("status") != "completed":
            payload = {"error": "Can only reconcile completed sprints"}
            out = json.dumps(payload)
            return out

        sprint_tasks = [t for t in tasks.values() if t.get("sprint_id") == sprint_id]

        planned_story_points = sprint.get("planned_story_points", 0)
        completed_story_points = sprint.get("completed_story_points", 0)

        total_hours_logged = 0
        cost_by_employee = {}

        for task in sprint_tasks:
            task_time_logs = [
                log for log in task_logs.values() if log.get("task_id") == task["task_id"]
            ]
            for log in task_time_logs:
                employee_id = log.get("employee_id")
                hours = log.get("hours", 0)
                total_hours_logged += hours

                if employee_id not in cost_by_employee:
                    employee = next(
                        (e for e in employees.values() if e.get("employee_id") == employee_id),
                        None,
                    )
                    if employee:
                        hourly_rate = (
                            150 if "senior" in employee.get("role", "").lower() else 100
                        )
                        cost_by_employee[employee_id] = {
                            "name": employee.get("name"),
                            "hours": 0,
                            "rate": hourly_rate,
                            "cost": 0,
                        }

                cost_by_employee[employee_id]["hours"] += hours
                cost_by_employee[employee_id]["cost"] += (
                    hours * cost_by_employee[employee_id]["rate"]
                )

        from datetime import timezone

        sprint_start = datetime.fromisoformat(
            sprint["start_date"].replace("Z", "+00:00")
        )
        sprint_end = datetime.fromisoformat(sprint["end_date"].replace("Z", "+00:00"))

        sprint_expenses = []
        for expense in expenses.values():
            if expense.get("sprint_id") == sprint_id:
                sprint_data["expenses"][expense_id] = expense
            elif expense.get("submitted_date"):

                try:
                    submitted_date = datetime.fromisoformat(
                        expense["submitted_date"].replace("Z", "+00:00")
                    )
                    if sprint_start <= submitted_date <= sprint_end:
                        sprint_data["expenses"][expense_id] = expense
                except:

                    pass

        total_expense_amount = sum(
            e.get("amount", 0) for e in sprint_expenses if e.get("status") == "approved"
        )

        estimated_hours = planned_story_points * 6
        hour_variance = (
            ((total_hours_logged - estimated_hours) / estimated_hours * 100)
            if estimated_hours > 0
            else 0
        )

        total_personnel_cost = sum(emp["cost"] for emp in cost_by_employee.values())

        reconciliation = {
            "sprint_id": sprint_id,
            "sprint_name": sprint.get("sprint_name"),
            "team_id": sprint.get("team_id"),
            "performance_metrics": {
                "planned_story_points": planned_story_points,
                "completed_story_points": completed_story_points,
                "completion_rate": (
                    round((completed_story_points / planned_story_points * 100), 2)
                    if planned_story_points > 0
                    else 0
                ),
            },
            "cost_metrics": {
                "total_hours_logged": total_hours_logged,
                "estimated_hours": estimated_hours,
                "hour_variance_percentage": round(hour_variance, 2),
                "personnel_cost": total_personnel_cost,
                "expense_cost": total_expense_amount,
                "total_cost": total_personnel_cost + total_expense_amount,
                "cost_per_story_point": (
                    round(
                        (total_personnel_cost + total_expense_amount)
                        / completed_story_points,
                        2,
                    )
                    if completed_story_points > 0
                    else 0
                ),
            },
            "employee_breakdown": list(cost_by_employee.values()),
            "expense_count": len(sprint_expenses),
            "reconciliation_date": datetime.now(timezone.utc).isoformat(),
        }

        if hour_variance > 20:
            reconciliation["recommendations"] = [
                "Review estimation practices - significant overrun detected"
            ]
        elif hour_variance < -20:
            reconciliation["recommendations"] = [
                "Team may be over-estimating - consider adjusting story point values"
            ]
        payload = reconciliation
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ReconcileSprintExpenses",
                "description": "Reconcile sprint expenses with actual hours logged and story points completed",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sprint_id": {
                            "type": "string",
                            "description": "Sprint ID to reconcile",
                        }
                    },
                    "required": ["sprint_id"],
                },
            },
        }


class CreateVendorFromRetrospective(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        vendor_name: str,
        vendor_type: str,
        payment_terms: str = "Net 30",
        team_feedback: dict = {},
        retrospective_id: str = None
    ) -> str:
        if not all([vendor_name, vendor_type]):
            payload = {"error": "vendor_name and vendor_type are required"}
            out = json.dumps(payload)
            return out

        vendors = data.get("vendors", {}).values()
        retrospectives = data.get("retrospectives", {}).values()
        teams = data.get("teams", {}).values()

        existing = next(
            (
                v
                for v in vendors.values() if v.get("vendor_name", "").lower() == vendor_name.lower()
            ),
            None,
        )
        if existing:
            payload = {"error": f"Vendor {vendor_name} already exists"}
            out = json.dumps(payload)
            return out

        team_skills = []
        if retrospective_id:
            retro = next(
                (
                    r
                    for r in retrospectives.values() if r.get("retrospective_id") == retrospective_id
                ),
                None,
            )
            if retro:
                team_id = retro.get("team_id")
                team = next((t for t in teams.values() if t.get("team_id") == team_id), None)
                if team:
                    action_items = retro.get("action_items", [])
                    for item in action_items:
                        if "vendor" in item.lower() or "contractor" in item.lower():
                            skills = [
                                "development",
                                "testing",
                                "design",
                                "security",
                                "devops",
                            ]
                            for skill in skills:
                                if skill in item.lower():
                                    team_skills.append(skill)

        vendor_id = f"vendor_{uuid.uuid4().hex[:8]}"

        new_vendor = {
            "vendor_id": vendor_id,
            "vendor_name": vendor_name,
            "vendor_type": vendor_type,
            "payment_terms": payment_terms,
            "status": "pending_review",
            "late_payments": 0,
            "capability_match": team_skills,
            "team_feedback": team_feedback,
            "created_from_retrospective": (
                retrospective_id if retrospective_id else None
            ),
            "created_date": datetime.now().isoformat(),
            "requires_assessment": True,
            "preferred_for_skills": team_skills,
        }

        data["vendors"][vendor_id] = new_vendor
        payload = {"success": True, "vendor": new_vendor}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateVendorFromRetrospective",
                "description": "Create a vendor record based on team retrospective feedback",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "vendor_name": {"type": "string", "description": "Vendor name"},
                        "vendor_type": {
                            "type": "string",
                            "description": "Type of vendor services",
                        },
                        "payment_terms": {
                            "type": "string",
                            "description": "Payment terms (default Net 30)",
                        },
                        "team_feedback": {
                            "type": "object",
                            "description": "Team feedback from retrospective",
                        },
                        "retrospective_id": {
                            "type": "string",
                            "description": "Related retrospective ID",
                        },
                    },
                    "required": ["vendor_name", "vendor_type"],
                },
            },
        }


class GenerateDepartmentFinancialReport(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        department_name: str,
        fiscal_year: int = datetime.now().year,
        include_employee_costs: bool = True
    ) -> str:
        if not department_name:
            payload = {"error": "department_name is required"}
            out = json.dumps(payload)
            return out

        departments = data.get("departments", {}).values()
        projects = data.get("projects", {}).values()
        budgets = data.get("budgets", {}).values()
        employees = data.get("employees", {}).values()
        allocations = data.get("allocations", {}).values()
        data.get("expenses", {}).values()

        department = next(
            (d for d in departments.values() if d.get("department_name") == department_name),
            None,
        )
        if not department:
            payload = {"error": f"Department {department_name} not found"}
            out = json.dumps(payload)
            return out

        dept_projects = [p for p in projects.values() if p.get("department") == department_name]

        total_budget = 0
        total_spent = 0
        total_committed = 0
        project_summaries = []

        for project in dept_projects:
            project_budget = next(
                (
                    b
                    for b in budgets.values() if b.get("project_id") == project["project_id"]
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
                e for e in employees.values() if e.get("department") == department_name
            ]

            for employee in dept_employees:

                emp_allocations = [
                    a
                    for a in allocations.values() if a.get("employee_id") == employee["employee_id"]
                    and a.get("status") == "active"
                ]

                total_hours = sum(a.get("hours_per_week", 0) for a in emp_allocations.values())
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
                "budget_utilization": (
                    round((total_spent / total_budget * 100), 2)
                    if total_budget > 0
                    else 0
                ),
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
                [p for p in dept_projects.values() if p.get("priority") == "critical"]
            ),
            "projects_over_budget": len(
                [p for p in project_summaries.values() if p["utilization"] > 90]
            ),
            "report_generated": datetime.now().isoformat(),
        }

        if include_employee_costs:
            report["employee_costs"] = employee_costs
            report["total_employee_cost"] = sum(
                e["annual_cost"] for e in employee_costs.values()
            )
        payload = report
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GenerateDepartmentFinancialReport",
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


class AllocateTaskExpenses(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        task_id: str = None,
        expense_amount: float = None,
        expense_category: str = None,
        description: str = None
    ) -> str:
        if not all([task_id, expense_amount, expense_category, description]):
            payload = {"error": "All fields are required"}
            out = json.dumps(payload)
            return out

        tasks = data.get("tasks", {}).values()
        expenses = data.get("expenses", {}).values()
        allocations = data.get("allocations", {}).values()
        budgets = data.get("budgets", {}).values()

        task = next((t for t in tasks.values() if t.get("task_id") == task_id), None)
        if not task:
            payload = {"error": f"Task {task_id} not found"}
            out = json.dumps(payload)
            return out

        employee_id = task.get("assignee_id")
        employee_allocation = next(
            (
                a
                for a in allocations.values() if a.get("employee_id") == employee_id and a.get("status") == "active"
            ),
            None,
        )

        if not employee_allocation:
            payload = {"error": "Cannot determine project for task expense"}
            out = json.dumps(payload)
            return out

        project_id = employee_allocation.get("project_id")

        if task.get("status") not in ["in_progress", "done"]:
            payload = {"error": "Expenses can only be allocated to active or completed tasks"}
            out = json.dumps(payload)
            return out

        expense_id = f"exp_{uuid.uuid4().hex[:8]}"

        from datetime import timezone

        current_time = datetime.now(timezone.utc)

        new_expense = {
            "expense_id": expense_id,
            "project_id": project_id,
            "task_id": task_id,
            "sprint_id": task.get("sprint_id"),
            "amount": expense_amount,
            "category": expense_category,
            "description": description,
            "employee_id": employee_id,
            "status": "approved",
            "submitted_date": current_time.isoformat(),
            "fiscal_year": current_time.year,
            "task_details": {
                "task_title": task.get("title"),
                "task_status": task.get("status"),
                "story_points": task.get("story_points"),
                "time_logged": task.get("time_logged", 0),
            },
        }

        data["expenses"][expense_id] = new_expense

        budget = next(
            (
                b
                for b in budgets.values() if b.get("project_id") == project_id
                and b.get("fiscal_year") == current_time.year
            ),
            None,
        )

        if budget:
            budget["spent_amount"] = budget.get("spent_amount", 0) + expense_amount
            budget["last_modified"] = current_time.isoformat()

        cost_per_point = expense_amount / task.get("story_points", 1)
        payload = {
            "success": True,
            "expense": new_expense,
            "cost_per_story_point": round(cost_per_point, 2),
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AllocateTaskExpenses",
                "description": "Allocate expenses directly to specific tasks",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task_id": {"type": "string", "description": "Task ID"},
                        "expense_amount": {
                            "type": "number",
                            "description": "Expense amount",
                        },
                        "expense_category": {
                            "type": "string",
                            "description": "Expense category",
                        },
                        "description": {
                            "type": "string",
                            "description": "Expense description",
                        },
                    },
                    "required": [
                        "task_id",
                        "expense_amount",
                        "expense_category",
                        "description",
                    ],
                },
            },
        }


class CalculateVelocityBudgetRatio(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], 
        team_id: str, 
        lookback_sprints: int = 3, 
        fiscal_year: int = datetime.now().year
    ) -> str:
        if not team_id:
            payload = {"error": "team_id is required"}
            out = json.dumps(payload)
            return out

        teams = data.get("teams", {}).values()
        sprints = data.get("sprints", {}).values()
        budgets = data.get("budgets", {}).values()
        expenses = data.get("expenses", {}).values()
        data.get("task_logs", {}).values()
        employees = data.get("employees", {}).values()

        team = next((t for t in teams.values() if t.get("team_id") == team_id), None)
        if not team:
            payload = {"error": f"Team {team_id} not found"}
            out = json.dumps(payload)
            return out

        team_sprints = [
            s
            for s in sprints.values() if s.get("team_id") == team_id and s.get("status") == "completed"
        ]

        team_sprints.sort(key=lambda x: x.get("end_date", ""), reverse=True)
        recent_sprints = team_sprints[:lookback_sprints]

        if not recent_sprints:
            payload = {"error": "No completed sprints found for team"}
            out = json.dumps(payload)
            return out

        sprint_metrics = []
        total_velocity = 0
        total_cost = 0

        for sprint in recent_sprints:
            sprint_velocity = sprint.get("velocity", 0)
            total_velocity += sprint_velocity

            sprint_cost = 0

            start_date = datetime.fromisoformat(
                sprint["start_date"].replace("Z", "+00:00")
            )
            end_date = datetime.fromisoformat(sprint["end_date"].replace("Z", "+00:00"))
            duration_weeks = (end_date - start_date).days / 7

            for member_id in team.get("members", []):
                employee = next(
                    (e for e in employees.values() if e.get("employee_id") == member_id), None
                )
                if employee:
                    hourly_rate = (
                        150 if "senior" in employee.get("role", "").lower() else 100
                    )

                    member_cost = hourly_rate * 40 * duration_weeks
                    sprint_cost += member_cost

            sprint_expenses = [
                e
                for e in expenses.values() if e.get("sprint_id") == sprint["sprint_id"]
                and e.get("status") == "approved"
            ]
            sprint_expense_total = sum(e.get("amount", 0) for e in sprint_expenses.values())
            sprint_cost += sprint_expense_total

            total_cost += sprint_cost

            sprint_metrics.append(
                {
                    "sprint_id": sprint["sprint_id"],
                    "sprint_name": sprint["sprint_name"],
                    "velocity": sprint_velocity,
                    "cost": sprint_cost,
                    "cost_per_point": (
                        round(sprint_cost / sprint_velocity, 2)
                        if sprint_velocity > 0
                        else 0
                    ),
                    "duration_weeks": round(duration_weeks, 1),
                }
            )

        project_id = team.get("project_id")
        budget = next(
            (
                b
                for b in budgets.values() if b.get("project_id") == project_id
                and b.get("fiscal_year") == fiscal_year
            ),
            None,
        )

        avg_velocity = total_velocity / len(recent_sprints)
        avg_cost_per_sprint = total_cost / len(recent_sprints)
        avg_cost_per_point = total_cost / total_velocity if total_velocity > 0 else 0

        remaining_budget = 0
        if budget:
            remaining_budget = budget["total_budget"] - budget.get("spent_amount", 0)

        projected_sprints_remaining = (
            remaining_budget / avg_cost_per_sprint if avg_cost_per_sprint > 0 else 0
        )
        projected_story_points = projected_sprints_remaining * avg_velocity

        analysis = {
            "projected_sprints_remaining": round(projected_sprints_remaining, 1),
            "team_id": team_id,
            "team_name": team["team_name"],
            "analysis_period": {
                "sprints_analyzed": len(recent_sprints),
                "total_story_points": total_velocity,
                "total_cost": total_cost,
            },
            "velocity_metrics": {
                "average_velocity": round(avg_velocity, 2),
                "velocity_trend": (
                    "improving"
                    if len(sprint_metrics) > 1
                    and sprint_metrics[0]["velocity"] > sprint_metrics[-1]["velocity"]
                    else "stable"
                ),
            },
            "cost_metrics": {
                "average_cost_per_sprint": round(avg_cost_per_sprint, 2),
                "average_cost_per_story_point": round(avg_cost_per_point, 2),
                "cost_efficiency_trend": (
                    "improving"
                    if len(sprint_metrics) > 1
                    and sprint_metrics[0]["cost_per_point"]
                    < sprint_metrics[-1]["cost_per_point"]
                    else "stable"
                ),
            },
            "budget_projection": {
                "remaining_budget": remaining_budget,
                "projected_sprints_remaining": round(projected_sprints_remaining, 1),
                "projected_story_points_deliverable": round(projected_story_points, 0),
            },
            "sprint_breakdown": sprint_metrics,
            "recommendations": [],
        }

        if avg_cost_per_point > 1000:
            analysis["recommendations"].append(
                "High cost per story point - consider efficiency improvements"
            )
        if projected_sprints_remaining < 2:
            analysis["recommendations"].append(
                "Budget running low - consider requesting budget modification"
            )
        payload = analysis
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateVelocityBudgetRatio",
                "description": "Calculate team velocity to budget ratio and project future capacity",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {"type": "string", "description": "Team ID"},
                        "lookback_sprints": {
                            "type": "integer",
                            "description": "Number of sprints to analyze",
                        },
                        "fiscal_year": {
                            "type": "integer",
                            "description": "Fiscal year (defaults to current)",
                        },
                    },
                    "required": ["team_id"],
                },
            },
        }


class TransferBudgetBetweenTeams(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        source_team_id: str = None,
        target_team_id: str = None,
        transfer_amount: float = None,
        fiscal_year: int = datetime.now().year
    ) -> str:
        if not all([source_team_id, target_team_id, transfer_amount]):
            payload = {"error": "All fields are required"}
            out = json.dumps(payload)
            return out

        teams = data.get("teams", {}).values()
        budgets = data.get("budgets", {}).values()
        budget_transfers = data.get("budget_transfers", {}).values()

        source_team = next(
            (t for t in teams.values() if t.get("team_id") == source_team_id), None
        )
        target_team = next(
            (t for t in teams.values() if t.get("team_id") == target_team_id), None
        )

        if not source_team or not target_team:
            payload = {"error": "Source or target team not found"}
            out = json.dumps(payload)
            return out

        source_project_id = source_team.get("project_id")
        target_project_id = target_team.get("project_id")

        source_budget = next(
            (
                b
                for b in budgets.values() if b.get("project_id") == source_project_id
                and b.get("fiscal_year") == fiscal_year
            ),
            None,
        )

        if not source_budget:
            payload = {"error": "No budget found for source team's project"}
            out = json.dumps(payload)
            return out

        available = (
            source_budget["total_budget"]
            - source_budget.get("spent_amount", 0)
            - source_budget.get("committed_amount", 0)
        )

        if transfer_amount > available * 0.25:
            payload = {
                    "error": f"Transfer amount exceeds 25% of available budget. Maximum allowed: ${available * 0.25}"
                }
            out = json.dumps(
                payload)
            return out

        source_dept = source_budget.get("department")
        target_budget = next(
            (
                b
                for b in budgets.values() if b.get("project_id") == target_project_id
                and b.get("fiscal_year") == fiscal_year
            ),
            None,
        )

        cross_department = False
        if target_budget:
            cross_department = source_dept != target_budget.get("department")

        transfer_id = f"xfer_{uuid.uuid4().hex[:8]}"

        new_transfer = {
            "transfer_id": transfer_id,
            "source_team_id": source_team_id,
            "target_team_id": target_team_id,
            "source_project_id": source_project_id,
            "target_project_id": target_project_id,
            "transfer_amount": transfer_amount,
            "cross_department": cross_department,
            "status": "approved" if not cross_department else "pending_finance_review",
            "created_date": datetime.now().isoformat(),
            "fiscal_year": fiscal_year,
        }

        data["budget_transfers"][new_transfer["budget_transfer_id"]] = new_transfer

        if new_transfer["status"] == "approved":
            source_budget["total_budget"] -= transfer_amount
            if target_budget:
                target_budget["total_budget"] += transfer_amount
        payload = {"success": True, "transfer": new_transfer}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "TransferBudgetBetweenTeams",
                "description": "Transfer budget between teams based on their projects",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "source_team_id": {
                            "type": "string",
                            "description": "Source team ID",
                        },
                        "target_team_id": {
                            "type": "string",
                            "description": "Target team ID",
                        },
                        "transfer_amount": {
                            "type": "number",
                            "description": "Amount to transfer",
                        },
                        "fiscal_year": {
                            "type": "integer",
                            "description": "Fiscal year (defaults to current)",
                        },
                    },
                    "required": [
                        "source_team_id",
                        "target_team_id",
                        "transfer_amount",
                    ],
                },
            },
        }


class GetEmployeeExpenseHistory(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str, fiscal_year: int = datetime.now().year) -> str:
        if not employee_id:
            payload = {"error": "employee_id is required"}
            out = json.dumps(payload)
            return out

        employees = data.get("employees", {}).values()
        expenses = data.get("expenses", {}).values()
        reimbursements = data.get("reimbursements", {}).values()
        allocations = data.get("allocations", {}).values()

        employee = next(
            (e for e in employees.values() if e.get("employee_id") == employee_id), None
        )
        if not employee:
            payload = {"error": f"Employee {employee_id} not found"}
            out = json.dumps(payload)
            return out

        employee_expenses = [
            e
            for e in expenses.values() if e.get("employee_id") == employee_id
            and e.get("fiscal_year") == fiscal_year
        ]

        employee_reimbursements = [
            r for r in reimbursements.values() if r.get("employee_id") == employee_id
        ]

        expenses_by_project = {}
        for expense in employee_expenses:
            project_id = expense.get("project_id")
            if project_id not in expenses_by_project:
                expenses_by_project[project_id] = {
                    "expenses": [],
                    "total_amount": 0,
                    "categories": {},
                }

            expenses_by_project[project_id]["expenses"].append(expense)
            expenses_by_project[project_id]["total_amount"] += expense.get("amount", 0)

            category = expense.get("category")
            if category not in expenses_by_project[project_id]["categories"]:
                expenses_by_project[project_id]["categories"][category] = 0
            expenses_by_project[project_id]["categories"][category] += expense.get(
                "amount", 0
            )

        total_allocation_percentage = 0
        active_allocations = [
            a
            for a in allocations.values() if a.get("employee_id") == employee_id and a.get("status") == "active"
        ]

        for allocation in active_allocations:
            allocation_percentage = allocation.get("hours_per_week", 0) / 40
            total_allocation_percentage += allocation_percentage

        monthly_limit = 1000 * total_allocation_percentage

        history = {
            "employee_id": employee_id,
            "employee_name": employee.get("name"),
            "fiscal_year": fiscal_year,
            "expense_summary": {
                "total_expenses": sum(e.get("amount", 0) for e in employee_expenses.values()),
                "expense_count": len(employee_expenses),
                "approved_count": len(
                    [e for e in employee_expenses.values() if e.get("status") == "approved"]
                ),
                "pending_count": len(
                    [
                        e
                        for e in employee_expenses
                        if e.get("status") == "pending_approval"
                    ]
                ),
                "rejected_count": len(
                    [e for e in employee_expenses.values() if e.get("status") == "rejected"]
                ),
            },
            "reimbursement_summary": {
                "total_reimbursements": sum(
                    r.get("amount", 0) for r in employee_reimbursements
                ),
                "reimbursement_count": len(employee_reimbursements),
                "average_submission_delay": 0,
            },
            "allocation_based_limits": {
                "total_allocation_percentage": round(
                    total_allocation_percentage * 100, 1
                ),
                "monthly_expense_limit": monthly_limit,
                "annual_expense_limit": monthly_limit * 12,
            },
            "expenses_by_project": expenses_by_project,
            "compliance_metrics": {
                "late_submissions": 0,
                "missing_receipts": len(
                    [
                        e
                        for e in employee_expenses
                        if not e.get("receipt_provided", True)
                    ]
                ),
                "over_limit_expenses": len(
                    [e for e in employee_expenses.values() if e.get("amount", 0) > monthly_limit]
                ),
            },
        }

        delays = []
        for reimb in employee_reimbursements:
            if reimb.get("expense_date") and reimb.get("submission_date"):
                expense_date = datetime.fromisoformat(
                    reimb["expense_date"].replace("Z", "+00:00")
                )
                submission_date = datetime.fromisoformat(
                    reimb["submission_date"].replace("Z", "+00:00")
                )
                delay_days = (submission_date - expense_date).days
                delays.append(delay_days)
                if delay_days > 30:
                    history["compliance_metrics"]["late_submissions"] += 1

        if delays:
            history["reimbursement_summary"]["average_submission_delay"] = round(
                sum(delays) / len(delays), 1
            )
        payload = history
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetEmployeeExpenseHistory",
                "description": "Get comprehensive expense history for an employee",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string", "description": "Employee ID"},
                        "fiscal_year": {
                            "type": "integer",
                            "description": "Fiscal year",
                        },
                    },
                    "required": ["employee_id"],
                },
            },
        }


class GetEmployeeReimbursementHistory(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str, fiscal_year: int = datetime.now().year) -> str:
        if not employee_id:
            payload = {"error": "employee_id is required"}
            out = json.dumps(payload)
            return out

        employees = data.get("employees", {}).values()
        reimbursements = data.get("reimbursements", {}).values()

        employee = next(
            (e for e in employees.values() if e.get("employee_id") == employee_id), None
        )
        if not employee:
            payload = {"error": f"Employee {employee_id} not found"}
            out = json.dumps(payload)
            return out

        employee_reimbursements = [
            r for r in reimbursements.values() if r.get("employee_id") == employee_id
        ]

        history = {
            "employee_id": employee_id,
            "employee_name": employee.get("name"),
            "fiscal_year": fiscal_year,
            "reimbursement_summary": {
                "total_reimbursements": sum(
                    r.get("amount", 0) for r in employee_reimbursements
                ),
                "reimbursement_count": len(employee_reimbursements),
            },
        }

        delays = []
        for reimb in employee_reimbursements:
            if reimb.get("expense_date") and reimb.get("submission_date"):
                expense_date = datetime.fromisoformat(
                    reimb["expense_date"].replace("Z", "+00:00")
                )
                submission_date = datetime.fromisoformat(
                    reimb["submission_date"].replace("Z", "+00:00")
                )
                delay_days = (submission_date - expense_date).days
                delays.append(delay_days)
        payload = history
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetEmployeeReimbursementHistory",
                "description": "Get comprehensive reimbursement history for an employee",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string", "description": "Employee ID"},
                        "fiscal_year": {
                            "type": "integer",
                            "description": "Fiscal year",
                        },
                    },
                    "required": ["employee_id"],
                },
            },
        }


class CreateBudgetFromVelocity(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], project_id: str, target_story_points: int, buffer_percentage: int = 20) -> str:
        if not all([project_id, target_story_points]):
            payload = {"error": "project_id and target_story_points are required"}
            out = json.dumps(payload)
            return out

        projects = data.get("projects", {}).values()
        teams = data.get("teams", {}).values()
        sprints = data.get("sprints", {}).values()
        budgets = data.get("budgets", {}).values()
        employees = data.get("employees", {}).values()

        project = next((p for p in projects.values() if p.get("project_id") == project_id), None)
        if not project:
            payload = {"error": f"Project {project_id} not found"}
            out = json.dumps(payload)
            return out

        project_team = next(
            (t for t in teams.values() if t.get("project_id") == project_id), None
        )
        if not project_team:
            payload = {"error": "No team assigned to project"}
            out = json.dumps(payload)
            return out

        team_sprints = [
            s
            for s in sprints.values() if s.get("team_id") == project_team["team_id"]
            and s.get("status") == "completed"
        ]

        if not team_sprints:
            avg_velocity = 40
            avg_cost_per_point = 500
        else:
            total_velocity = sum(s.get("velocity", 0) for s in team_sprints.values())
            total_sprints = len(team_sprints)
            avg_velocity = total_velocity / total_sprints if total_sprints > 0 else 40

            total_cost = 0
            for member_id in project_team.get("members", []):
                employee = next(
                    (e for e in employees.values() if e.get("employee_id") == member_id), None
                )
                if employee:
                    hourly_rate = (
                        150 if "senior" in employee.get("role", "").lower() else 100
                    )

                    total_cost += hourly_rate * 80 * total_sprints

            avg_cost_per_point = (
                total_cost / total_velocity if total_velocity > 0 else 500
            )

        required_sprints = target_story_points / avg_velocity if avg_velocity > 0 else 1
        base_budget = target_story_points * avg_cost_per_point

        total_budget = base_budget * (1 + buffer_percentage / 100)

        budget_id = f"budget_{uuid.uuid4().hex[:8]}"

        new_budget = {
            "budget_id": budget_id,
            "project_id": project_id,
            "fiscal_year": datetime.now().year,
            "total_budget": round(total_budget, 2),
            "personnel_budget": round(total_budget * 0.8, 2),
            "non_personnel_budget": round(total_budget * 0.2, 2),
            "calculation_basis": {
                "target_story_points": target_story_points,
                "average_velocity": round(avg_velocity, 2),
                "required_sprints": round(required_sprints, 1),
                "cost_per_story_point": round(avg_cost_per_point, 2),
                "buffer_percentage": buffer_percentage,
            },
            "spent_amount": 0,
            "committed_amount": 0,
            "status": "active",
            "created_date": datetime.now().isoformat(),
            "department": project.get("department"),
        }

        data["budgets"][budget_id] = new_budget
        payload = {"success": True, "budget": new_budget}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateBudgetFromVelocity",
                "description": "Create project budget based on team velocity and story point targets",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "Project ID"},
                        "target_story_points": {
                            "type": "integer",
                            "description": "Total story points to deliver",
                        },
                        "buffer_percentage": {
                            "type": "integer",
                            "description": "Budget buffer percentage (default 20%)",
                        },
                    },
                    "required": ["project_id", "target_story_points"],
                },
            },
        }


class GetBudgetStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], project_id: str, fiscal_year: int = datetime.now().year) -> str:
        if not project_id:
            payload = {"error": "project_id is required"}
            out = json.dumps(payload)
            return out

        budgets = data.get("budgets", {}).values()
        expenses = data.get("expenses", {}).values()
        purchase_orders = data.get("purchase_orders", {}).values()

        budget = next(
            (
                b
                for b in budgets.values() if b.get("project_id") == project_id
                and b.get("fiscal_year") == fiscal_year
            ),
            None,
        )

        if not budget:
            payload = {
                    "error": f"No budget found for project {project_id} in fiscal year {fiscal_year}"
                }
            out = json.dumps(
                payload)
            return out

        pending_expenses = sum(
            e.get("amount", 0)
            for e in expenses.values() if e.get("project_id") == project_id
            and e.get("status") == "pending_approval"
            and e.get("fiscal_year") == fiscal_year
        )

        pending_pos = sum(
            po.get("total_amount", 0)
            for po in purchase_orders.values() if po.get("project_id") == project_id
            and po.get("status") == "pending_approval"
        )

        total_budget = budget["total_budget"]
        spent = budget.get("spent_amount", 0)
        committed = budget.get("committed_amount", 0)
        available = total_budget - spent - committed

        utilization_rate = (spent / total_budget * 100) if total_budget > 0 else 0
        burn_rate = (
            ((spent + committed) / total_budget * 100) if total_budget > 0 else 0
        )

        status = {
            "project_id": project_id,
            "fiscal_year": fiscal_year,
            "total_budget": total_budget,
            "spent_amount": spent,
            "committed_amount": committed,
            "available_amount": available,
            "pending_expenses": pending_expenses,
            "pending_purchase_orders": pending_pos,
            "utilization_rate": round(utilization_rate, 2),
            "burn_rate": round(burn_rate, 2),
            "budget_health": (
                "critical"
                if burn_rate > 90
                else "warning" if burn_rate > 80 else "healthy"
            ),
            "requires_modification": burn_rate > 110,
        }
        payload = status
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetBudgetStatus",
                "description": "Get current budget status and utilization for a project",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "Project ID"},
                        "fiscal_year": {
                            "type": "integer",
                            "description": "Fiscal year (defaults to current)",
                        },
                    },
                    "required": ["project_id"],
                },
            },
        }


class ProcessVendorPayment(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], invoice_id: str = None, payment_amount: float = None, payment_method: str = None, processor_id: str = None) -> str:
        if not all([invoice_id, payment_amount, payment_method, processor_id]):
            payload = {"error": "All fields are required"}
            out = json.dumps(payload)
            return out

        invoices = data.get("invoices", {}).values()
        payments = data.get("payments", {}).values()
        vendors = data.get("vendors", {}).values()

        invoice = next((i for i in invoices.values() if i.get("invoice_id") == invoice_id), None)
        if not invoice:
            payload = {"error": f"Invoice {invoice_id} not found"}
            out = json.dumps(payload)
            return out

        if invoice.get("status") == "paid":
            payload = {"error": "Invoice is already paid"}
            out = json.dumps(payload)
            return out

        if payment_amount != invoice["amount"]:
            payload = {
                    "error": f"Payment amount ${payment_amount} does not match invoice amount ${invoice['amount']}"
                }
            out = json.dumps(
                payload)
            return out

        due_date = datetime.fromisoformat(invoice["due_date"].replace("Z", "+00:00"))

        from datetime import timezone

        is_late = datetime.now(timezone.utc) > due_date
        late_fee = 0
        days_late = 0

        if is_late:
            days_late = (datetime.now(timezone.utc) - due_date).days
            months_late = days_late // 30
            late_fee = invoice["amount"] * 0.02 * months_late

        payment_id = f"pay_{uuid.uuid4().hex[:8]}"

        new_payment = {
            "payment_id": payment_id,
            "invoice_id": invoice_id,
            "vendor_id": invoice["vendor_id"],
            "amount": payment_amount,
            "late_fee": late_fee,
            "total_paid": payment_amount + late_fee,
            "payment_method": payment_method,
            "payment_date": datetime.now(timezone.utc).isoformat(),
            "processed_by": processor_id,
            "is_late": is_late,
            "days_late": days_late,
        }

        data["payments"][payment_id] = new_payment

        invoice["status"] = "paid"
        invoice["payment_id"] = payment_id
        invoice["paid_date"] = datetime.now(timezone.utc).isoformat()

        vendor = next(
            (v for v in vendors.values() if v.get("vendor_id") == invoice["vendor_id"]), None
        )
        if vendor:
            if "late_payments" not in vendor:
                vendor["late_payments"] = 0
            if is_late:
                vendor["late_payments"] += 1

            vendor["last_payment_date"] = datetime.now(timezone.utc).isoformat()

        result = {"success": True, "payment": new_payment}

        if vendor and vendor.get("late_payments", 0) >= 3:
            result["warning"] = (
                f"Vendor has {vendor['late_payments']} late payments - review required"
            )
        payload = result
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ProcessVendorPayment",
                "description": "Process payment for a vendor invoice",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoice_id": {"type": "string", "description": "Invoice ID"},
                        "payment_amount": {
                            "type": "number",
                            "description": "Payment amount",
                        },
                        "payment_method": {
                            "type": "string",
                            "description": "Payment method (check, wire, ach)",
                        },
                        "processor_id": {
                            "type": "string",
                            "description": "Employee processing payment",
                        },
                    },
                    "required": [
                        "invoice_id",
                        "payment_amount",
                        "payment_method",
                        "processor_id",
                    ],
                },
            },
        }


class RequestBudgetModification(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        project_id: str,
        modification_amount: float,
        modification_type: str,
        justification: str,
        requestor_id: str,
        fiscal_year: int = datetime.now().year
    ) -> str:
        if not all(
            [
                project_id,
                modification_amount,
                modification_type,
                justification,
                requestor_id,
            ]
        ):
            payload = {"error": "All fields are required"}
            out = json.dumps(payload)
            return out

        budget_modifications = data.get("budget_modifications", {}).values()
        budgets = data.get("budgets", {}).values()

        current_budget = next(
            (
                b
                for b in budgets.values() if b.get("project_id") == project_id
                and b.get("fiscal_year") == fiscal_year
            ),
            None,
        )

        if not current_budget:
            payload = {"error": f"No active budget found for project {project_id}"}
            out = json.dumps(payload)
            return out

        current_overrun = (
            current_budget.get("spent_amount", 0) / current_budget["total_budget"] - 1
        ) * 100
        is_emergency = (
            current_overrun > 10
            and current_overrun <= 15
            and modification_type == "increase"
        )

        modification_id = f"mod_{uuid.uuid4().hex[:8]}"

        new_modification = {
            "modification_id": modification_id,
            "project_id": project_id,
            "current_budget": current_budget["total_budget"],
            "modification_amount": modification_amount,
            "modification_type": modification_type,
            "new_budget": (
                current_budget["total_budget"] + modification_amount
                if modification_type == "increase"
                else current_budget["total_budget"] - modification_amount
            ),
            "justification": justification,
            "requestor_id": requestor_id,
            "status": "pending_approval",
            "requires_approval": ["project_sponsor", "finance_director"],
            "is_emergency": is_emergency,
            "created_date": datetime.now().isoformat(),
            "fiscal_year": fiscal_year,
        }

        data["budget_modifications"][new_modification["budget_modification_id"]] = new_modification

        result = {"success": True, "modification_request": new_modification}

        if is_emergency:
            result["info"] = (
                "Emergency modification - can be approved retroactively within 48 hours"
            )
        payload = result
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RequestBudgetModification",
                "description": "Request a budget increase or decrease",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "Project ID"},
                        "modification_amount": {
                            "type": "number",
                            "description": "Amount to modify",
                        },
                        "modification_type": {
                            "type": "string",
                            "description": "increase or decrease",
                        },
                        "justification": {
                            "type": "string",
                            "description": "Justification for modification",
                        },
                        "requestor_id": {
                            "type": "string",
                            "description": "Employee requesting modification",
                        },
                        "fiscal_year": {
                            "type": "integer",
                            "description": "Fiscal year (defaults to current)",
                        },
                    },
                    "required": [
                        "project_id",
                        "modification_amount",
                        "modification_type",
                        "justification",
                        "requestor_id",
                    ],
                },
            },
        }


class GetVendorStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], vendor_id: str = None) -> str:
        if not vendor_id:
            payload = {"error": "vendor_id is required"}
            out = json.dumps(payload)
            return out

        vendors = data.get("vendors", {}).values()
        invoices = data.get("invoices", {}).values()
        data.get("payments", {}).values()
        purchase_orders = data.get("purchase_orders", {}).values()

        vendor = next((v for v in vendors.values() if v.get("vendor_id") == vendor_id), None)
        if not vendor:
            payload = {"error": f"Vendor {vendor_id} not found"}
            out = json.dumps(payload)
            return out

        vendor_invoices = [i for i in invoices.values() if i.get("vendor_id") == vendor_id]

        outstanding_amount = sum(
            i.get("amount", 0) for i in vendor_invoices if i.get("status") != "paid"
        )

        pending_pos = [
            po
            for po in purchase_orders.values() if po.get("vendor_id") == vendor_id
            and po.get("status") == "pending_approval"
        ]
        approved_pos = [
            po
            for po in purchase_orders.values() if po.get("vendor_id") == vendor_id and po.get("status") == "approved"
        ]

        late_invoices = []
        for invoice in vendor_invoices:
            if invoice.get("status") != "paid":
                due_date = datetime.fromisoformat(
                    invoice["due_date"].replace("Z", "+00:00")
                )

                current_time = datetime.now(timezone.utc)
                if current_time > due_date:
                    days_late = (current_time - due_date).days
                    late_invoices.append(
                        {
                            "invoice_id": invoice["invoice_id"],
                            "amount": invoice["amount"],
                            "days_late": days_late,
                            "late_fee": invoice["amount"] * 0.02 * (days_late // 30),
                        }
                    )

        status = {
            "vendor_id": vendor_id,
            "vendor_name": vendor.get("vendor_name"),
            "payment_terms": vendor.get("payment_terms", "Net 30"),
            "status": vendor.get("status", "active"),
            "late_payments_count": vendor.get("late_payments", 0),
            "requires_prepayment": vendor.get("late_payments", 0) >= 3,
            "outstanding_amount": outstanding_amount,
            "pending_pos_count": len(pending_pos),
            "pending_pos_value": sum(po.get("total_amount", 0) for po in pending_pos.values()),
            "approved_pos_count": len(approved_pos),
            "approved_pos_value": sum(po.get("total_amount", 0) for po in approved_pos.values()),
            "late_invoices": late_invoices,
            "total_late_fees": sum(inv["late_fee"] for inv in late_invoices.values()),
            "last_payment_date": vendor.get("last_payment_date"),
        }
        payload = status
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetVendorStatus",
                "description": "Get vendor payment status and history",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "vendor_id": {"type": "string", "description": "Vendor ID"}
                    },
                    "required": ["vendor_id"],
                },
            },
        }


class AllocateCosts(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], expense_id: str, allocation_splits: list = [], allocator_id: str = None, fiscal_year: int = datetime.now().year) -> str:
        if not all([expense_id, allocation_splits, allocator_id]):
            payload = {
                    "error": "expense_id, allocation_splits, and allocator_id are required"
                }
            out = json.dumps(
                payload)
            return out

        expenses = data.get("expenses", {}).values()
        cost_allocations = data.get("cost_allocations", {}).values()
        budgets = data.get("budgets", {}).values()

        expense = next((e for e in expenses.values() if e.get("expense_id") == expense_id), None)
        if not expense:
            payload = {"error": f"Expense {expense_id} not found"}
            out = json.dumps(payload)
            return out

        total_percentage = sum(
            split.get("percentage", 0) for split in allocation_splits
        )
        if abs(total_percentage - 100) > 0.01:
            payload = {
                    "error": f"Allocations must sum to 100%, currently {total_percentage}%"
                }
            out = json.dumps(
                payload)
            return out

        total_allocated = sum(split.get("amount", 0) for split in allocation_splits.values())
        if abs(total_allocated - expense["amount"]) > 0.01:
            payload = {
                    "error": f"Allocated amounts must match expense total ${expense['amount']}"
                }
            out = json.dumps(
                payload)
            return out

        allocation_id = f"alloc_{uuid.uuid4().hex[:8]}"

        new_allocation = {
            "allocation_id": allocation_id,
            "expense_id": expense_id,
            "original_amount": expense["amount"],
            "allocation_splits": allocation_splits,
            "allocated_by": allocator_id,
            "allocation_date": datetime.now().isoformat(),
            "status": "completed",
        }

        cost_data["allocations"][allocation_id] = new_allocation

        for split in allocation_splits:
            budget = next(
                (
                    b
                    for b in budgets.values() if b.get("project_id") == split["project_id"]
                    and b.get("fiscal_year") == fiscal_year
                ),
                None,
            )
            if budget:
                budget["spent_amount"] = budget.get("spent_amount", 0) + split["amount"]
                budget["last_modified"] = datetime.now().isoformat()

        unallocated = [
            e
            for e in expenses.values() if e.get("expense_id")
            not in [a.get("expense_id") for a in cost_allocations.values()]
            and e.get("amount", 0) > 10000
        ]

        result = {"success": True, "allocation": new_allocation}

        if unallocated:
            result["warning"] = (
                f"{len(unallocated)} expenses over $10,000 remain unallocated"
            )
        payload = result
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AllocateCosts",
                "description": "Allocate costs across multiple projects",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "expense_id": {
                            "type": "string",
                            "description": "Expense ID to allocate",
                        },
                        "allocation_splits": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "project_id": {"type": "string"},
                                    "percentage": {"type": "number"},
                                    "amount": {"type": "number"},
                                },
                            },
                            "description": "List of allocation splits",
                        },
                        "allocator_id": {
                            "type": "string",
                            "description": "Employee performing allocation",
                        },
                        "fiscal_year": {
                            "type": "integer",
                            "description": "Fiscal year (defaults to current)",
                        },
                    },
                    "required": ["expense_id", "allocation_splits", "allocator_id"],
                },
            },
        }


class SubmitReimbursement(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        employee_id: str,
        submission_date: str = None,
        expense_date: str = None,
        amount: float = None,
        description: str = None,
        category: str = None,
        receipt_provided: bool = True,
        project_id: str = None,
        reimbursement_id: str = None
    ) -> str:
        from datetime import timezone

        if submission_date is None:
            submission_date = datetime.now(timezone.utc).isoformat()

        if not all([employee_id, expense_date, amount, description, category]):
            payload = {"error": "Missing required fields"}
            out = json.dumps(payload)
            return out

        reimbursements = data.get("reimbursements", {}).values()

        expense_dt = datetime.fromisoformat(expense_date.replace("Z", "+00:00"))

        submission_dt = datetime.fromisoformat(submission_date.replace("Z", "+00:00"))

        days_elapsed = (submission_dt - expense_dt).days

        if not receipt_provided and amount > 75:
            payload = {"error": "Receipts are required for expenses over $75 without receipt"}
            out = json.dumps(payload)
            return out

        if reimbursement_id is None:
            reimbursement_id = f"reimb_{uuid.uuid4().hex[:8]}"

        new_reimbursement = {
            "reimbursement_id": reimbursement_id,
            "employee_id": employee_id,
            "expense_date": expense_date,
            "submission_date": submission_date,
            "amount": amount,
            "description": description,
            "category": category,
            "receipt_provided": receipt_provided,
            "project_id": project_id,
            "status": "pending_approval" if amount > 500 else "approved",
            "days_to_submit": days_elapsed,
        }

        data["reimbursements"][reimbursement_id] = new_reimbursement
        payload = {"success": True, "reimbursement": new_reimbursement}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SubmitReimbursement",
                "description": "Submit an expense reimbursement request",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string", "description": "Employee ID"},
                        "reimbursement_id": {
                            "type": "string",
                            "description": "Reimbursement ID",
                        },
                        "expense_date": {
                            "type": "string",
                            "description": "Date of expense (ISO format)",
                        },
                        "submission_date": {
                            "type": "string",
                            "description": "Date of the submission (ISO format)",
                        },
                        "amount": {
                            "type": "number",
                            "description": "Reimbursement amount",
                        },
                        "description": {
                            "type": "string",
                            "description": "Expense description",
                        },
                        "category": {
                            "type": "string",
                            "description": "Expense category",
                        },
                        "receipt_provided": {
                            "type": "boolean",
                            "description": "Whether receipt is provided",
                        },
                        "project_id": {
                            "type": "string",
                            "description": "Related project ID (optional)",
                        },
                    },
                    "required": [
                        "employee_id",
                        "expense_date",
                        "amount",
                        "description",
                        "category",
                    ],
                },
            },
        }


class GetFinancialReport(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], report_type: str, entity_id: str, fiscal_year: int = datetime.now().year) -> str:
        if not all([report_type, entity_id]):
            payload = {"error": "report_type and entity_id are required"}
            out = json.dumps(payload)
            return out

        budgets = data.get("budgets", {}).values()
        expenses = data.get("expenses", {}).values()
        purchase_orders = data.get("purchase_orders", {}).values()

        if report_type == "project":
            budget = next(
                (
                    b
                    for b in budgets.values() if b.get("project_id") == entity_id
                    and b.get("fiscal_year") == fiscal_year
                ),
                None,
            )

            if not budget:
                payload = {"error": f"No budget found for project {entity_id}"}
                out = json.dumps(payload)
                return out

            project_expenses = [
                e
                for e in expenses.values() if e.get("project_id") == entity_id
                and e.get("fiscal_year") == fiscal_year
                and e.get("status") == "approved"
            ]

            expenses_by_category = {}
            for exp in project_expenses:
                cat = exp.get("category", "Other")
                expenses_by_category[cat] = (
                    expenses_by_category.get(cat, 0) + exp["amount"]
                )

            report = {
                "report_type": "project_financial",
                "project_id": entity_id,
                "fiscal_year": fiscal_year,
                "budget_summary": {
                    "total_budget": budget["total_budget"],
                    "spent": budget.get("spent_amount", 0),
                    "committed": budget.get("committed_amount", 0),
                    "available": budget["total_budget"]
                    - budget.get("spent_amount", 0)
                    - budget.get("committed_amount", 0),
                    "utilization_rate": round(
                        (budget.get("spent_amount", 0) / budget["total_budget"] * 100),
                        2,
                    ),
                },
                "expenses_by_category": expenses_by_category,
                "total_expenses": sum(expenses_by_category.values()),
                "purchase_orders": {
                    "pending": len(
                        [
                            po
                            for po in purchase_orders.values() if po.get("project_id") == entity_id
                            and po.get("status") == "pending_approval"
                        ]
                    ),
                    "approved": len(
                        [
                            po
                            for po in purchase_orders.values() if po.get("project_id") == entity_id
                            and po.get("status") == "approved"
                        ]
                    ),
                },
                "compliance": {
                    "budget_health": (
                        "critical"
                        if budget.get("spent_amount", 0) > budget["total_budget"] * 0.9
                        else (
                            "warning"
                            if budget.get("spent_amount", 0)
                            > budget["total_budget"] * 0.8
                            else "healthy"
                        )
                    ),
                    "requires_review": budget.get("spent_amount", 0)
                    < budget["total_budget"] * 0.3,
                },
            }
            payload = report
            out = json.dumps(payload, indent=2)
            return out
        payload = {"error": f"Report type '{report_type}' not implemented"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetFinancialReport",
                "description": "Generate financial reports for projects, departments, or vendors",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "report_type": {
                            "type": "string",
                            "description": "Type of report: project, department, vendor",
                        },
                        "entity_id": {
                            "type": "string",
                            "description": "ID of the entity to report on",
                        },
                        "fiscal_year": {
                            "type": "integer",
                            "description": "Fiscal year",
                        },
                        "quarter": {
                            "type": "integer",
                            "description": "Quarter (1-4, optional)",
                        },
                    },
                    "required": ["report_type", "entity_id"],
                },
            },
        }


class CreateFinancialAlert(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        alert_type: str,
        entity_type: str,
        entity_id: str,
        threshold_value: Any = None,
        notify_list: list = None,
        alert_id: str = None
    ) -> str:
        if notify_list is None:
            notify_list = []
        if alert_id is None:
            alert_id = f"alert_{uuid.uuid4().hex[:8]}"

        if not all([alert_type, entity_type, entity_id, notify_list]):
            payload = {
                "error": "alert_type, entity_type, entity_id, and notify_list are required"
            }
            out = json.dumps(payload)
            return out

        financial_alerts = data.get("financial_alerts", {}).values()

        new_alert = {
            "alert_id": alert_id,
            "alert_type": alert_type,
            "entity_type": entity_type,
            "entity_id": entity_id,
            "threshold_value": threshold_value,
            "notify_list": notify_list,
            "status": "active",
            "created_date": datetime.now().isoformat(),
            "triggered_count": 0,
            "last_triggered": None,
        }

        data["financial_alerts"][new_alert["financial_alert_id"]] = new_alert
        payload = {"success": True, "alert": new_alert}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateFinancialAlert",
                "description": "Create automated financial alerts",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "alert_type": {
                            "type": "string",
                            "description": "Type of alert",
                        },
                        "entity_type": {
                            "type": "string",
                            "description": "Entity type to monitor",
                        },
                        "entity_id": {"type": "string", "description": "Entity ID"},
                        "alert_id": {"type": "string", "description": "Alert ID"},
                        "threshold_value": {
                            "type": "number",
                            "description": "Threshold value (optional)",
                        },
                        "notify_list": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of employee IDs to notify",
                        },
                    },
                    "required": [
                        "alert_type",
                        "entity_type",
                        "entity_id",
                        "notify_list",
                    ],
                },
            },
        }


class ProcessBudgetTransfer(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        transfer_id: str = None,
        approval_action: str = None,
        approver_id: str = None,
        approver_role: str = None
    ) -> str:
        if not all([transfer_id, approval_action, approver_id, approver_role]):
            payload = {"error": "All fields are required"}
            out = json.dumps(payload)
            return out

        budget_transfers = data.get("budget_transfers", {}).values()
        budgets = data.get("budgets", {}).values()

        transfer = next(
            (t for t in budget_transfers.values() if t.get("transfer_id") == transfer_id), None
        )
        if not transfer:
            payload = {"error": f"Transfer {transfer_id} not found"}
            out = json.dumps(payload)
            return out

        if transfer.get("status") != "pending_approval":
            payload = {"error": "Transfer is not pending approval"}
            out = json.dumps(payload)
            return out

        if "approvals" not in transfer:
            transfer["approvals"] = {}

        transfer["approvals"][approver_role] = {
            "action": approval_action,
            "approver_id": approver_id,
            "approval_date": datetime.now().isoformat(),
        }

        all_approved = all(
            transfer["approvals"].get(role, {}).values().get("action") == "approve"
            for role in transfer["approvals_required"]
        )

        any_rejected = any(
            transfer["approvals"].get(role, {}).values().get("action") == "reject"
            for role in transfer["approvals_required"]
        )

        if any_rejected:
            transfer["status"] = "rejected"
        elif all_approved:
            transfer["status"] = "approved"

            source_budget = next(
                (
                    b
                    for b in budgets.values() if b.get("project_id") == transfer["source_project_id"]
                    and b.get("fiscal_year") == transfer["fiscal_year"]
                ),
                None,
            )
            target_budget = next(
                (
                    b
                    for b in budgets.values() if b.get("project_id") == transfer["target_project_id"]
                    and b.get("fiscal_year") == transfer["fiscal_year"]
                ),
                None,
            )

            if source_budget and target_budget:
                source_budget["total_budget"] -= transfer["transfer_amount"]
                target_budget["total_budget"] += transfer["transfer_amount"]
                source_budget["last_modified"] = datetime.now().isoformat()
                target_budget["last_modified"] = datetime.now().isoformat()

        transfer["last_updated"] = datetime.now().isoformat()
        payload = {
            "success": True,
            "transfer": transfer,
            "all_approvals_complete": transfer["status"] in ["approved", "rejected"],
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "processBudgetTransfer",
                "description": "Approve or reject a budget transfer request",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "transfer_id": {"type": "string", "description": "Transfer ID"},
                        "approval_action": {
                            "type": "string",
                            "description": "approve or reject",
                        },
                        "approver_id": {
                            "type": "string",
                            "description": "Approver's employee ID",
                        },
                        "approver_role": {
                            "type": "string",
                            "description": "Approver's role in this transfer",
                        },
                    },
                    "required": [
                        "transfer_id",
                        "approval_action",
                        "approver_id",
                        "approver_role",
                    ],
                },
            },
        }


class RecordInvoice(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        vendor_id: str,
        po_number: str = None,
        invoice_number: str = None,
        amount: float = None,
        invoice_date: str = None,
        due_date: str = None,
        invoice_id: str = None
    ) -> str:
        if not all([vendor_id, invoice_number, amount, invoice_date, due_date]):
            payload = {"error": "All fields except po_number are required"}
            out = json.dumps(payload)
            return out

        invoices = data.get("invoices", {}).values()
        purchase_orders = data.get("purchase_orders", {}).values()
        vendors = data.get("vendors", {}).values()

        vendor = next((v for v in vendors.values() if v.get("vendor_id") == vendor_id), None)
        if not vendor:
            payload = {"error": f"Vendor {vendor_id} not found"}
            out = json.dumps(payload)
            return out

        if po_number:
            po = next(
                (p for p in purchase_orders.values() if p.get("po_number") == po_number), None
            )
            if po:
                if po.get("vendor_id") != vendor_id:
                    payload = {"error": "PO vendor does not match invoice vendor"}
                    out = json.dumps(payload)
                    return out
                if abs(po.get("total_amount", 0) - amount) > 0.01:
                    payload = {
                        "error": f"Invoice amount ${amount} does not match PO amount ${po.get('total_amount', 0)}"
                    }
                    out = json.dumps(payload)
                    return out

        if invoice_id is None:
            invoice_id = f"inv_{uuid.uuid4().hex[:8]}"

        new_invoice = {
            "invoice_id": invoice_id,
            "vendor_id": vendor_id,
            "po_number": po_number,
            "invoice_number": invoice_number,
            "amount": amount,
            "invoice_date": invoice_date,
            "due_date": due_date,
            "status": "pending",
            "recorded_date": datetime.now().isoformat(),
            "payment_terms": vendor.get("payment_terms", "Net 30"),
        }

        data["invoices"][invoice_id] = new_invoice

        due_dt = datetime.fromisoformat(due_date.replace("Z", "+00:00"))

        from datetime import timezone

        if datetime.now(timezone.utc) > due_dt:
            days_late = (datetime.now(timezone.utc) - due_dt).days
            payload = {
                "success": True,
                "invoice": new_invoice,
                "warning": f"Invoice is already {days_late} days past due",
            }
            out = json.dumps(payload)
            return out
        payload = {"success": True, "invoice": new_invoice}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RecordInvoice",
                "description": "Record a vendor invoice for payment",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "vendor_id": {"type": "string", "description": "Vendor ID"},
                        "invoice_id": {"type": "string", "description": "Invoice ID"},
                        "po_number": {
                            "type": "string",
                            "description": "Related PO number (optional)",
                        },
                        "invoice_number": {
                            "type": "string",
                            "description": "Vendor's invoice number",
                        },
                        "amount": {"type": "number", "description": "Invoice amount"},
                        "invoice_date": {
                            "type": "string",
                            "description": "Invoice date",
                        },
                        "due_date": {
                            "type": "string",
                            "description": "Payment due date",
                        },
                    },
                    "required": [
                        "vendor_id",
                        "invoice_number",
                        "amount",
                        "invoice_date",
                        "due_date",
                    ],
                },
            },
        }


class GetProjectFinancialSummary(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], project_id: str, fiscal_year: int = datetime.now().year) -> str:
        if not project_id:
            payload = {"error": "project_id is required"}
            out = json.dumps(payload)
            return out

        projects = data.get("projects", {}).values()
        budgets = data.get("budgets", {}).values()
        expenses = data.get("expenses", {}).values()
        allocations = data.get("allocations", {}).values()
        employees = data.get("employees", {}).values()

        project = next((p for p in projects.values() if p.get("project_id") == project_id), None)
        if not project:
            payload = {"error": f"Project {project_id} not found"}
            out = json.dumps(payload)
            return out

        current_budget = next(
            (
                b
                for b in budgets.values() if b.get("project_id") == project_id
                and b.get("fiscal_year") == fiscal_year
            ),
            None,
        )

        project_allocations = [
            a
            for a in allocations.values() if a.get("project_id") == project_id and a.get("status") == "active"
        ]

        weekly_resource_cost = 0
        for alloc in project_allocations:
            employee = next(
                (e for e in employees.values() if e.get("employee_id") == alloc["employee_id"]),
                None,
            )
            if employee:
                hourly_rate = (
                    150 if "senior" in employee.get("role", "").lower() else 100
                )
                weekly_resource_cost += alloc.get("hours_per_week", 0) * hourly_rate

        approved_expenses = sum(
            e.get("amount", 0)
            for e in expenses.values() if e.get("project_id") == project_id and e.get("status") == "approved"
        )

        summary = {
            "project_id": project_id,
            "project_name": project["name"],
            "project_status": project["status"],
            "financial_summary": {
                "budget_allocated": (
                    current_budget["total_budget"] if current_budget else 0
                ),
                "budget_spent": (
                    current_budget.get("spent_amount", 0) if current_budget else 0
                ),
                "weekly_burn_rate": weekly_resource_cost,
                "monthly_burn_rate": weekly_resource_cost * 4.33,
                "total_expenses": approved_expenses,
                "remaining_budget": (
                    (
                        current_budget["total_budget"]
                        - current_budget.get("spent_amount", 0)
                    )
                    if current_budget
                    else 0
                ),
            },
            "resource_allocation": {
                "active_allocations": len(project_allocations),
                "weekly_resource_hours": sum(
                    a.get("hours_per_week", 0) for a in project_allocations
                ),
                "weekly_resource_cost": weekly_resource_cost,
            },
        }
        payload = summary
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProjectFinancialSummary",
                "description": "Get comprehensive financial summary for a project",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "Project ID"},
                        "fiscal_year": {
                            "type": "integer",
                            "description": "Fiscal year (defaults to current)",
                        },
                    },
                    "required": ["project_id"],
                },
            },
        }


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
        total_hours = sum(a.get("hours_per_week", 0) for a in active_allocations.values())

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


class GetDepartmentBudgetOverview(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], department_name: str, fiscal_year: int = datetime.now().year) -> str:
        if not department_name:
            payload = {"error": "department_name is required"}
            out = json.dumps(payload)
            return out

        departments = data.get("departments", {}).values()
        projects = data.get("projects", {}).values()
        budgets = data.get("budgets", {}).values()

        department = next(
            (d for d in departments.values() if d.get("department_name") == department_name),
            None,
        )
        if not department:
            payload = {"error": f"Department {department_name} not found"}
            out = json.dumps(payload)
            return out

        dept_projects = [p for p in projects.values() if p.get("department") == department_name]

        total_budget = 0
        total_spent = 0
        project_budgets = []

        for project in dept_projects:
            project_budget = next(
                (
                    b
                    for b in budgets.values() if b.get("project_id") == project["project_id"]
                    and b.get("fiscal_year") == fiscal_year
                ),
                None,
            )
            if project_budget:
                total_budget += project_budget["total_budget"]
                total_spent += project_budget.get("spent_amount", 0)

                project_budgets.append(
                    {
                        "project_id": project["project_id"],
                        "project_name": project["name"],
                        "priority": project["priority"],
                        "budget": project_budget["total_budget"],
                        "spent": project_budget.get("spent_amount", 0),
                        "remaining": project_budget["total_budget"]
                        - project_budget.get("spent_amount", 0),
                    }
                )

        project_budgets.sort(key=lambda x: x["budget"], reverse=True)

        overview = {
            "department": department_name,
            "budget_overview": {
                "total_department_budget": total_budget,
                "total_spent": total_spent,
                "total_remaining": total_budget - total_spent,
                "utilization_percentage": (
                    round((total_spent / total_budget * 100), 2)
                    if total_budget > 0
                    else 0
                ),
                "project_count": len(dept_projects),
                "projects_with_budget": len(project_budgets),
            },
            "top_projects_by_budget": project_budgets[:5],
            "capacity_metrics": {
                "total_employees": department.get("employee_count", 0),
                "total_capacity_hours": department.get("total_capacity_hours", 0),
                "allocated_hours": department.get("allocated_hours", 0),
                "available_hours": department.get("available_hours", 0),
            },
        }
        payload = overview
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetDepartmentBudgetOverview",
                "description": "Get budget overview for all projects in a department",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "department_name": {
                            "type": "string",
                            "description": "Department name",
                        },
                        "fiscal_year": {
                            "type": "integer",
                            "description": "Fiscal year (defaults to current)",
                        },
                    },
                    "required": ["department_name"],
                },
            },
        }


class CreateCostForecast(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        project_id: str,
        forecast_months: int = 3,
        include_contingency: bool = True,
        fiscal_year: int = datetime.now().year,
    ) -> str:
        if not project_id:
            payload = {"error": "project_id is required"}
            out = json.dumps(payload)
            return out

        projects = data.get("projects", {}).values()
        allocations = data.get("allocations", {}).values()
        employees = data.get("employees", {}).values()
        budgets = data.get("budgets", {}).values()
        cost_forecasts = data.get("cost_forecasts", {}).values()

        project = next((p for p in projects.values() if p.get("project_id") == project_id), None)
        if not project:
            payload = {"error": f"Project {project_id} not found"}
            out = json.dumps(payload)
            return out

        project_allocations = [
            a
            for a in allocations.values() if a.get("project_id") == project_id and a.get("status") == "active"
        ]

        monthly_personnel_cost = 0
        for alloc in project_allocations:
            employee = next(
                (e for e in employees.values() if e.get("employee_id") == alloc["employee_id"]),
                None,
            )
            if employee:
                hourly_rate = (
                    150 if "senior" in employee.get("role", "").lower() else 100
                )
                monthly_personnel_cost += (
                    alloc.get("hours_per_week", 0) * hourly_rate * 4.33
                )

        monthly_non_personnel = monthly_personnel_cost * 0.2
        monthly_total = monthly_personnel_cost + monthly_non_personnel

        forecast_data = []
        cumulative_cost = 0

        for month in range(1, forecast_months + 1):
            if include_contingency:
                month_cost = monthly_total * (1 + 0.1 * month / forecast_months)
            else:
                month_cost = monthly_total

            cumulative_cost += month_cost

            forecast_data.append(
                {
                    "month": month,
                    "personnel_cost": (
                        monthly_personnel_cost * (1 + 0.1 * month / forecast_months)
                        if include_contingency
                        else monthly_personnel_cost
                    ),
                    "non_personnel_cost": (
                        monthly_non_personnel * (1 + 0.1 * month / forecast_months)
                        if include_contingency
                        else monthly_non_personnel
                    ),
                    "total_cost": month_cost,
                    "cumulative_cost": cumulative_cost,
                }
            )

        current_budget = next(
            (
                b
                for b in budgets.values() if b.get("project_id") == project_id
                and b.get("fiscal_year") == fiscal_year
            ),
            None,
        )

        budget_exhaustion_month = None
        if current_budget:
            remaining_budget = current_budget["total_budget"] - current_budget.get(
                "spent_amount", 0
            )
            for i, month_data in enumerate(forecast_data):
                if month_data["cumulative_cost"] > remaining_budget:
                    budget_exhaustion_month = i + 1
                    break

        forecast_id = f"forecast_{uuid.uuid4().hex[:8]}"

        new_forecast = {
            "budget_exhaustion_month": budget_exhaustion_month,
            "forecast_id": forecast_id,
            "project_id": project_id,
            "forecast_months": forecast_months,
            "monthly_burn_rate": monthly_total,
            "forecast_data": forecast_data,
            "total_forecasted_cost": cumulative_cost,
            "includes_contingency": include_contingency,
            "created_date": datetime.now().isoformat(),
        }

        data["cost_forecasts"][new_forecast["cost_forecast_id"]] = new_forecast
        payload = {"success": True, "forecast": new_forecast}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateCostForecast",
                "description": "Create a cost forecast for a project",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "Project ID"},
                        "forecast_months": {
                            "type": "integer",
                            "description": "Number of months to forecast",
                        },
                        "include_contingency": {
                            "type": "boolean",
                            "description": "Include contingency in forecast",
                        },
                        "fiscal_year": {
                            "type": "integer",
                            "description": "Fiscal year (defaults to current)",
                        },
                    },
                    "required": ["project_id"],
                },
            },
        }


class GetTaskCostBreakdown(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], task_id: str = None) -> str:
        if not task_id:
            payload = {"error": "task_id is required"}
            out = json.dumps(payload)
            return out

        tasks = data.get("tasks", {}).values()
        task_logs = data.get("task_logs", {}).values()
        employees = data.get("employees", {}).values()
        expenses = data.get("expenses", {}).values()

        task = next((t for t in tasks.values() if t.get("task_id") == task_id), None)
        if not task:
            payload = {"error": f"Task {task_id} not found"}
            out = json.dumps(payload)
            return out

        task_time_logs = [log for log in task_logs.values() if log.get("task_id") == task_id]

        personnel_costs = []
        total_hours = 0
        total_personnel_cost = 0

        for log in task_time_logs:
            employee_id = log.get("employee_id")
            hours = log.get("hours", 0)

            employee = next(
                (e for e in employees.values() if e.get("employee_id") == employee_id), None
            )
            if employee:
                hourly_rate = (
                    150 if "senior" in employee.get("role", "").lower() else 100
                )
                cost = hours * hourly_rate

                personnel_costs.append(
                    {
                        "employee_id": employee_id,
                        "employee_name": employee["name"],
                        "hours_logged": hours,
                        "hourly_rate": hourly_rate,
                        "cost": cost,
                        "log_date": log.get("logged_date"),
                    }
                )

                total_hours += hours
                total_personnel_cost += cost

        task_expenses = [
            e
            for e in expenses.values() if e.get("task_id") == task_id and e.get("status") == "approved"
        ]

        total_expense_cost = sum(e.get("amount", 0) for e in task_expenses.values())

        story_points = task.get("story_points", 1)
        total_cost = total_personnel_cost + total_expense_cost
        cost_per_point = total_cost / story_points if story_points > 0 else 0

        breakdown = {
            "task_id": task_id,
            "task_title": task["title"],
            "task_status": task["status"],
            "story_points": story_points,
            "cost_breakdown": {
                "personnel_cost": total_personnel_cost,
                "expense_cost": total_expense_cost,
                "total_cost": total_cost,
                "cost_per_story_point": round(cost_per_point, 2),
            },
            "time_metrics": {
                "total_hours_logged": total_hours,
                "average_hourly_cost": (
                    round(total_personnel_cost / total_hours, 2)
                    if total_hours > 0
                    else 0
                ),
                "hours_per_story_point": (
                    round(total_hours / story_points, 2) if story_points > 0 else 0
                ),
            },
            "personnel_details": personnel_costs,
            "expense_count": len(task_expenses),
        }
        payload = breakdown
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTaskCostBreakdown",
                "description": "Get detailed cost breakdown for a specific task",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task_id": {"type": "string", "description": "Task ID"}
                    },
                    "required": ["task_id"],
                },
            },
        }


class ValidatePurchaseOrder(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], po_number: str = None, vendor_id: str = None, project_id: str = None, amount: float = None, description: str = None, fiscal_year: int = datetime.now().year) -> str:
        if not all([po_number, vendor_id, project_id, amount]):
            payload = {"error": "po_number, vendor_id, project_id, and amount are required"}
            out = json.dumps(payload)
            return out

        budgets = data.get("budgets", {}).values()
        vendors = data.get("vendors", {}).values()
        data.get("purchase_orders", {}).values()
        projects = data.get("projects", {}).values()

        vendor = next((v for v in vendors.values() if v.get("vendor_id") == vendor_id), None)
        if not vendor:
            payload = {"error": f"Vendor {vendor_id} not found"}
            out = json.dumps(payload)
            return out

        if vendor.get("status") != "active":
            payload = {
                "error": f"Vendor status is {vendor.get('status')}. Only active vendors allowed"
            }
            out = json.dumps(payload)
            return out

        budget = next(
            (
                b
                for b in budgets.values() if b.get("project_id") == project_id
                and b.get("fiscal_year") == fiscal_year
            ),
            None,
        )

        if not budget:
            payload = {"error": "No budget found for project"}
            out = json.dumps(payload)
            return out

        available_budget = (
            budget["total_budget"]
            - budget.get("spent_amount", 0)
            - budget.get("committed_amount", 0)
        )

        project = next((p for p in projects.values() if p.get("project_id") == project_id), None)
        approval_required = []

        if project:
            if project["priority"] == "low" and amount > 10000:
                approval_required.append("finance_manager")
            if amount > 50000:
                approval_required.append("department_head")
            if amount > 100000:
                approval_required.append("cfo")

        validation_result = {
            "po_number": po_number,
            "validation_status": "valid",
            "vendor_check": {
                "vendor_name": vendor.get("vendor_name"),
                "vendor_status": vendor.get("status"),
                "late_payments": vendor.get("late_payments", 0),
                "requires_prepayment": vendor.get("late_payments", 0) >= 3,
            },
            "budget_check": {
                "available_budget": available_budget,
                "po_amount": amount,
                "sufficient_funds": amount <= available_budget,
                "budget_utilization_after": round(
                    (
                        (budget.get("spent_amount", 0) + amount)
                        / budget["total_budget"]
                        * 100
                    ),
                    2,
                ),
            },
            "approval_requirements": approval_required,
            "warnings": [],
        }

        if amount > available_budget:
            validation_result["validation_status"] = "insufficient_funds"
            validation_result["warnings"].append("Insufficient budget available")

        if vendor.get("late_payments", 0) >= 3:
            validation_result["warnings"].append(
                "Vendor has history of late payments - prepayment recommended"
            )

        if validation_result["budget_check"]["budget_utilization_after"] > 90:
            validation_result["warnings"].append(
                "PO will push budget utilization over 90%"
            )
        payload = validation_result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ValidatePurchaseOrder",
                "description": "Validate a purchase order against budget and vendor status",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "po_number": {
                            "type": "string",
                            "description": "Purchase order number",
                        },
                        "vendor_id": {"type": "string", "description": "Vendor ID"},
                        "project_id": {"type": "string", "description": "Project ID"},
                        "amount": {"type": "number", "description": "PO amount"},
                        "description": {
                            "type": "string",
                            "description": "PO description",
                        },
                        "fiscal_year": {
                            "type": "integer",
                            "description": "Fiscal year (defaults to current)",
                        },
                    },
                    "required": ["po_number", "vendor_id", "project_id", "amount"],
                },
            },
        }


class GetEmployeeCostByProject(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], 
        employee_id: str = None, 
        project_id: str = None, 
        include_expenses: bool = True
    ) -> str:
        if not all([employee_id, project_id]):
            payload = {"error": "employee_id and project_id are required"}
            out = json.dumps(payload)
            return out

        employees = data.get("employees", {}).values()
        allocations = data.get("allocations", {}).values()
        task_logs = data.get("task_logs", {}).values()
        tasks = data.get("tasks", {}).values()
        expenses = data.get("expenses", {}).values()

        employee = next(
            (e for e in employees.values() if e.get("employee_id") == employee_id), None
        )
        if not employee:
            payload = {"error": f"Employee {employee_id} not found"}
            out = json.dumps(payload)
            return out

        project_allocation = next(
            (
                a
                for a in allocations.values() if a.get("employee_id") == employee_id
                and a.get("project_id") == project_id
            ),
            None,
        )

        hourly_rate = 150 if "senior" in employee.get("role", "").lower() else 100

        employee_project_tasks = [
            t
            for t in tasks.values() if t.get("assignee_id") == employee_id
            and any(
                a.get("project_id") == project_id
                for a in allocations.values() if a.get("employee_id") == employee_id
            )
        ]

        total_hours = 0
        task_details = []

        for task in employee_project_tasks:
            task_time_logs = [
                log
                for log in task_logs.values() if log.get("task_id") == task["task_id"]
                and log.get("employee_id") == employee_id
            ]

            task_hours = sum(log.get("hours", 0) for log in task_time_logs.values())
            total_hours += task_hours

            if task_hours > 0:
                task_details.append(
                    {
                        "task_id": task["task_id"],
                        "task_title": task["title"],
                        "hours_logged": task_hours,
                        "cost": task_hours * hourly_rate,
                    }
                )

        total_time_cost = total_hours * hourly_rate

        employee_expenses = []
        total_expense_amount = 0

        if include_expenses:
            employee_expenses = [
                e
                for e in expenses.values() if e.get("employee_id") == employee_id
                and e.get("project_id") == project_id
                and e.get("status") == "approved"
            ]
            total_expense_amount = sum(e.get("amount", 0) for e in employee_expenses.values())

        employee_cost = {
            "employee_id": employee_id,
            "employee_name": employee["name"],
            "project_id": project_id,
            "allocation_status": "active" if project_allocation else "inactive",
            "cost_summary": {
                "total_hours_logged": total_hours,
                "hourly_rate": hourly_rate,
                "time_based_cost": total_time_cost,
                "expense_cost": total_expense_amount,
                "total_cost": total_time_cost + total_expense_amount,
            },
            "tasks_worked": len(task_details),
            "task_details": task_details[:10],
            "expense_count": len(employee_expenses) if include_expenses else None,
        }

        if project_allocation:
            employee_cost["allocation_details"] = {
                "hours_per_week": project_allocation.get("hours_per_week", 0),
                "role": project_allocation.get("role"),
                "start_date": project_allocation.get("start_date"),
                "end_date": project_allocation.get("end_date"),
            }
        payload = employee_cost
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetEmployeeCostByProject",
                "description": "Get total cost incurred by an employee on a specific project",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string", "description": "Employee ID"},
                        "project_id": {"type": "string", "description": "Project ID"},
                        "include_expenses": {
                            "type": "boolean",
                            "description": "Include expense data",
                        },
                    },
                    "required": ["employee_id", "project_id"],
                },
            },
        }


class CreateBudgetThresholdAlert(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        project_id: str,
        threshold_percentage: int = 80,
        alert_recipients: list = [],
        alert_name: str = None
    ) -> str:
        if not all([project_id, alert_recipients]):
            payload = {"error": "project_id and alert_recipients are required"}
            out = json.dumps(payload)
            return out

        if threshold_percentage < 50 or threshold_percentage > 100:
            payload = {"error": "threshold_percentage must be between 50 and 100"}
            out = json.dumps(payload)
            return out

        budgets = data.get("budgets", {}).values()
        budget_alerts = data.get("budget_alerts", {}).values()
        projects = data.get("projects", {}).values()

        project = next((p for p in projects.values() if p.get("project_id") == project_id), None)
        if not project:
            payload = {"error": f"Project {project_id} not found"}
            out = json.dumps(payload)
            return out

        existing_alert = next(
            (
                a
                for a in budget_alerts.values() if a.get("project_id") == project_id
                and a.get("threshold_percentage") == threshold_percentage
                and a.get("active")
            ),
            None,
        )

        if existing_alert:
            payload = {"error": "Similar active alert already exists for this project"}
            out = json.dumps(payload)
            return out

        alert_id = f"alert_{uuid.uuid4().hex[:8]}"

        new_alert = {
            "alert_id": alert_id,
            "alert_name": alert_name
            or f"{project['name']} - {threshold_percentage}% Budget Alert",
            "project_id": project_id,
            "threshold_percentage": threshold_percentage,
            "alert_recipients": alert_recipients,
            "active": True,
            "triggered": False,
            "last_triggered": None,
            "created_date": datetime.now().isoformat(),
            "alert_type": "budget_threshold",
        }

        data["budget_alerts"][new_alert["budget_alert_id"]] = new_alert

        current_budget = next(
            (
                b
                for b in budgets.values() if b.get("project_id") == project_id
                and b.get("fiscal_year") == datetime.now().year
            ),
            None,
        )

        current_utilization = 0
        if current_budget:
            current_utilization = round(
                (
                    current_budget.get("spent_amount", 0)
                    / current_budget["total_budget"]
                    * 100
                ),
                2,
            )
        payload = {
            "success": True,
            "budget_alert": new_alert,
            "current_utilization": current_utilization,
            "will_trigger_immediately": current_utilization >= threshold_percentage,
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateBudgetThresholdAlert",
                "description": "Create budget threshold alert for a project",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "Project ID"},
                        "threshold_percentage": {
                            "type": "integer",
                            "description": "Budget threshold percentage (50-100)",
                        },
                        "alert_recipients": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of employee IDs to alert",
                        },
                        "alert_name": {
                            "type": "string",
                            "description": "Custom alert name",
                        },
                    },
                    "required": ["project_id", "alert_recipients"],
                },
            },
        }


class GetSprintFinancialAnalysis(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], sprint_id: str = None) -> str:
        if not sprint_id:
            payload = {"error": "sprint_id is required"}
            out = json.dumps(payload)
            return out

        sprints = data.get("sprints", {}).values()
        tasks = data.get("tasks", {}).values()
        task_logs = data.get("task_logs", {}).values()
        employees = data.get("employees", {}).values()
        expenses = data.get("expenses", {}).values()

        sprint = next((s for s in sprints.values() if s.get("sprint_id") == sprint_id), None)
        if not sprint:
            payload = {"error": f"Sprint {sprint_id} not found"}
            out = json.dumps(payload)
            return out

        sprint_tasks = [t for t in tasks.values() if t.get("sprint_id") == sprint_id]

        employee_costs = {}
        total_hours = 0
        total_cost = 0

        for task in sprint_tasks:
            task_time_logs = [
                log for log in task_logs.values() if log.get("task_id") == task["task_id"]
            ]

            for log in task_time_logs:
                employee_id = log.get("employee_id")
                hours = log.get("hours", 0)

                if employee_id not in employee_costs:
                    employee = next(
                        (e for e in employees.values() if e.get("employee_id") == employee_id),
                        None,
                    )
                    if employee:
                        hourly_rate = (
                            150 if "senior" in employee.get("role", "").lower() else 100
                        )
                        employee_costs[employee_id] = {
                            "name": employee["name"],
                            "role": employee["role"],
                            "hours": 0,
                            "hourly_rate": hourly_rate,
                            "cost": 0,
                        }

                if employee_id in employee_costs:
                    employee_costs[employee_id]["hours"] += hours
                    employee_costs[employee_id]["cost"] += (
                        hours * employee_costs[employee_id]["hourly_rate"]
                    )
                    total_hours += hours
                    total_cost += hours * employee_costs[employee_id]["hourly_rate"]

        from datetime import timezone

        sprint_start = datetime.fromisoformat(
            sprint["start_date"].replace("Z", "+00:00")
        )
        sprint_end = datetime.fromisoformat(sprint["end_date"].replace("Z", "+00:00"))

        sprint_expenses = []
        for expense in expenses.values():
            if expense.get("sprint_id") == sprint_id:
                sprint_data["expenses"][expense_id] = expense
            elif expense.get("submitted_date"):

                try:
                    submitted_date_str = expense["submitted_date"]

                    if submitted_date_str.endswith("Z"):
                        submitted_date = datetime.fromisoformat(
                            submitted_date_str.replace("Z", "+00:00")
                        )
                    elif "+" in submitted_date_str or submitted_date_str.endswith(
                        "+00:00"
                    ):
                        submitted_date = datetime.fromisoformat(submitted_date_str)
                    else:

                        submitted_date = datetime.fromisoformat(
                            submitted_date_str
                        ).replace(tzinfo=timezone.utc)

                    if sprint_start <= submitted_date <= sprint_end:
                        sprint_data["expenses"][expense_id] = expense
                except Exception:

                    pass

        total_expenses = sum(
            e.get("amount", 0) for e in sprint_expenses if e.get("status") == "approved"
        )

        planned_points = sprint.get("planned_story_points", 0)
        completed_points = sprint.get("completed_story_points", 0)

        analysis = {
            "sprint_id": sprint_id,
            "sprint_name": sprint["sprint_name"],
            "sprint_status": sprint["status"],
            "financial_summary": {
                "total_personnel_cost": total_cost,
                "total_expense_cost": total_expenses,
                "total_cost": total_cost + total_expenses,
                "total_hours": total_hours,
                "average_hourly_cost": (
                    round(total_cost / total_hours, 2) if total_hours > 0 else 0
                ),
            },
            "productivity_metrics": {
                "planned_story_points": planned_points,
                "completed_story_points": completed_points,
                "cost_per_planned_point": (
                    round((total_cost + total_expenses) / planned_points, 2)
                    if planned_points > 0
                    else 0
                ),
                "cost_per_completed_point": (
                    round((total_cost + total_expenses) / completed_points, 2)
                    if completed_points > 0
                    else 0
                ),
                "velocity": sprint.get("velocity", 0),
            },
            "team_costs": {
                "team_members": len(employee_costs),
                "member_breakdown": list(employee_costs.values()),
            },
            "expense_summary": {
                "expense_count": len(sprint_expenses),
                "total_amount": total_expenses,
                "categories": {},
            },
        }

        for expense in sprint_expenses:
            category = expense.get("category", "Other")
            if category not in analysis["expense_summary"]["categories"]:
                analysis["expense_summary"]["categories"][category] = 0
            analysis["expense_summary"]["categories"][category] += expense.get(
                "amount", 0
            )
        payload = analysis
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSprintFinancialAnalysis",
                "description": "Get comprehensive financial analysis for a sprint",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sprint_id": {"type": "string", "description": "Sprint ID"}
                    },
                    "required": ["sprint_id"],
                },
            },
        }


class CalculateProjectROI(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        project_id: str,
        revenue_generated: float = 0,
        cost_savings: float = 0,
        fiscal_year: int = datetime.now().year
    ) -> str:
        if not project_id:
            payload = {"error": "project_id is required"}
            out = json.dumps(payload)
            return out

        projects = data.get("projects", {}).values()
        budgets = data.get("budgets", {}).values()
        expenses = data.get("expenses", {}).values()
        allocations = data.get("allocations", {}).values()
        employees = data.get("employees", {}).values()
        task_logs = data.get("task_logs", {}).values()
        tasks = data.get("tasks", {}).values()

        project = next((p for p in projects.values() if p.get("project_id") == project_id), None)
        if not project:
            payload = {"error": f"Project {project_id} not found"}
            out = json.dumps(payload)
            return out

        project_budget = next(
            (
                b
                for b in budgets.values() if b.get("project_id") == project_id
                and b.get("fiscal_year") == fiscal_year
            ),
            None,
        )

        budgeted_amount = project_budget["total_budget"] if project_budget else 0
        project_budget.get("spent_amount", 0) if project_budget else 0

        project_tasks = [
            t
            for t in tasks.values() if any(
                a.get("project_id") == project_id
                for a in allocations.values() if a.get("employee_id") == t.get("assignee_id")
            )
        ]

        actual_personnel_cost = 0
        for task in project_tasks:
            task_time_logs = [
                log for log in task_logs.values() if log.get("task_id") == task["task_id"]
            ]

            for log in task_time_logs:
                employee_id = log.get("employee_id")
                hours = log.get("hours", 0)

                employee = next(
                    (e for e in employees.values() if e.get("employee_id") == employee_id), None
                )
                if employee:
                    hourly_rate = (
                        150 if "senior" in employee.get("role", "").lower() else 100
                    )
                    actual_personnel_cost += hours * hourly_rate

        project_expenses = [
            e
            for e in expenses.values() if e.get("project_id") == project_id and e.get("status") == "approved"
        ]

        total_expense_cost = sum(e.get("amount", 0) for e in project_expenses.values())

        total_actual_cost = actual_personnel_cost + total_expense_cost

        total_benefit = revenue_generated + cost_savings
        roi_percentage = (
            ((total_benefit - total_actual_cost) / total_actual_cost * 100)
            if total_actual_cost > 0
            else 0
        )

        monthly_benefit = total_benefit / 12
        payback_months = (
            total_actual_cost / monthly_benefit if monthly_benefit > 0 else float("inf")
        )

        roi_analysis = {
            "roi_percentage": round(roi_percentage, 2),
            "project_id": project_id,
            "project_name": project["name"],
            "project_status": project["status"],
            "financial_metrics": {
                "budgeted_cost": budgeted_amount,
                "actual_cost": total_actual_cost,
                "personnel_cost": actual_personnel_cost,
                "expense_cost": total_expense_cost,
                "budget_variance": budgeted_amount - total_actual_cost,
            },
            "benefit_metrics": {
                "revenue_generated": revenue_generated,
                "cost_savings": cost_savings,
                "total_benefit": total_benefit,
            },
            "roi_calculations": {
                "roi_percentage": round(roi_percentage, 2),
                "net_benefit": total_benefit - total_actual_cost,
                "benefit_cost_ratio": (
                    round(total_benefit / total_actual_cost, 2)
                    if total_actual_cost > 0
                    else 0
                ),
                "payback_period_months": (
                    round(payback_months, 1)
                    if payback_months != float("inf")
                    else "N/A"
                ),
            },
            "roi_status": "positive" if roi_percentage > 0 else "negative",
            "meets_target": roi_percentage >= 15,
        }
        payload = roi_analysis
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateProjectRoi",
                "description": "Calculate return on investment (ROI) for a project",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "Project ID"},
                        "revenue_generated": {
                            "type": "number",
                            "description": "Revenue generated by project",
                        },
                        "cost_savings": {
                            "type": "number",
                            "description": "Cost savings achieved",
                        },
                        "fiscal_year": {
                            "type": "integer",
                            "description": "Fiscal year (defaults to current)",
                        },
                    },
                    "required": ["project_id"],
                },
            },
        }


TOOLS = [
    CreateProjectBudget(),
    CalculateProjectCost(),
    ValidateExpenseSubmission(),
    GetTeamBudgetStatus(),
    ReconcileSprintExpenses(),
    CreateVendorFromRetrospective(),
    GenerateDepartmentFinancialReport(),
    AllocateTaskExpenses(),
    CalculateVelocityBudgetRatio(),
    TransferBudgetBetweenTeams(),
    GetEmployeeExpenseHistory(),
    GetEmployeeReimbursementHistory(),
    CreateBudgetFromVelocity(),
    GetBudgetStatus(),
    ProcessVendorPayment(),
    RequestBudgetModification(),
    GetVendorStatus(),
    AllocateCosts(),
    SubmitReimbursement(),
    GetFinancialReport(),
    CreateFinancialAlert(),
    ProcessBudgetTransfer(),
    RecordInvoice(),
    GetProjectFinancialSummary(),
    CalculateEmployeeCostRate(),
    GetDepartmentBudgetOverview(),
    CreateCostForecast(),
    GetTaskCostBreakdown(),
    ValidatePurchaseOrder(),
    GetEmployeeCostByProject(),
    CreateBudgetThresholdAlert(),
    GetSprintFinancialAnalysis(),
    CalculateProjectROI(),
]
