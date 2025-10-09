from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetEmployeeReimbursementHistory(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str, fiscal_year: int = datetime.now().year) -> str:
        if not employee_id:
            payload = {"error": "employee_id is required"}
            out = json.dumps(payload)
            return out

        employees = data.get("employees", [])
        reimbursements = data.get("reimbursements", [])

        employee = next(
            (e for e in employees if e.get("employee_id") == employee_id), None
        )
        if not employee:
            payload = {"error": f"Employee {employee_id} not found"}
            out = json.dumps(payload)
            return out

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
