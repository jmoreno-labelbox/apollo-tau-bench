# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SubmitReimbursement(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:

        from datetime import timezone

        employee_id = kwargs.get("employee_id")
        submission_date = kwargs.get("submission_date", datetime.now(timezone.utc).isoformat())
        expense_date = kwargs.get("expense_date")
        amount = kwargs.get("amount")
        description = kwargs.get("description")
        category = kwargs.get("category")
        receipt_provided = kwargs.get("receipt_provided", True)
        project_id = kwargs.get("project_id")

        if not all([employee_id, expense_date, amount, description, category]):
            return json.dumps({"error": "Missing required fields"})

        reimbursements = data.get("reimbursements", [])

        expense_dt = datetime.fromisoformat(expense_date.replace("Z", "+00:00"))

        submission_dt = datetime.fromisoformat(submission_date.replace("Z", "+00:00"))

        days_elapsed = (submission_dt - expense_dt).days

        if not receipt_provided and amount > 75:
            return json.dumps(
                {"error": "Receipts are required for expenses over $75 without receipt"}
            )

        reimbursement_id = kwargs.get("reimbursement_id", f"reimb_{uuid.uuid4().hex[:8]}")

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

        return json.dumps({"success": True, "reimbursement": new_reimbursement})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "submit_reimbursement",
                "description": "Submit an expense reimbursement request",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string", "description": "Employee ID"},
                        "reimbursement_id": {"type": "string", "description": "Reimbursement ID"},
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
