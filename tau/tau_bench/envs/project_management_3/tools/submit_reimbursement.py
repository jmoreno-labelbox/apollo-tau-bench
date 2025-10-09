from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timezone
from typing import Any

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

        reimbursements = data.get("reimbursements", [])

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

        reimbursements.append(new_reimbursement)
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
