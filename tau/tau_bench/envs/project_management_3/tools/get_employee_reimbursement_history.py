# Copyright Sierra

import datetime
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetEmployeeReimbursementHistory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id, fiscal_year = datetime.now().year) -> str:

        if not employee_id:
            return json.dumps({"error": "employee_id is required"})

        employees = list(data.get("employees", {}).values())
        reimbursements = data.get("reimbursements", [])

        employee = next(
            (e for e in employees if e.get("employee_id") == employee_id), None
        )
        if not employee:
            return json.dumps({"error": f"Employee {employee_id} not found"})

        employee_reimbursements = [
            r for r in reimbursements if r.get("employee_id") == employee_id
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

        return json.dumps(history, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_employee_reimbursement_history",
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
