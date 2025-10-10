# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetEmployeeExpenseHistory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id, fiscal_year = datetime.now().year) -> str:

        if not employee_id:
            return json.dumps({"error": "employee_id is required"})

        employees = list(data.get("employees", {}).values())
        expenses = data.get("expenses", [])
        reimbursements = data.get("reimbursements", [])
        allocations = data.get("allocations", [])

        employee = next(
            (e for e in employees if e.get("employee_id") == employee_id), None
        )
        if not employee:
            return json.dumps({"error": f"Employee {employee_id} not found"})

        employee_expenses = [
            e
            for e in expenses
            if e.get("employee_id") == employee_id
            and e.get("fiscal_year") == fiscal_year
        ]

        employee_reimbursements = [
            r for r in reimbursements if r.get("employee_id") == employee_id
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
            for a in allocations
            if a.get("employee_id") == employee_id and a.get("status") == "active"
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
                "total_expenses": sum(e.get("amount", 0) for e in employee_expenses),
                "expense_count": len(employee_expenses),
                "approved_count": len(
                    [e for e in employee_expenses if e.get("status") == "approved"]
                ),
                "pending_count": len(
                    [
                        e
                        for e in employee_expenses
                        if e.get("status") == "pending_approval"
                    ]
                ),
                "rejected_count": len(
                    [e for e in employee_expenses if e.get("status") == "rejected"]
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
                    [e for e in employee_expenses if e.get("amount", 0) > monthly_limit]
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

        return json.dumps(history, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_employee_expense_history",
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
