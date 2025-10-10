# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import get_current_timestamp


class UpdateLoanApplicationStatusTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], application_id, approved_amount, status, notes = '') -> str:

        loan_applications = data.get('loan_applications', [])

        for application in loan_applications:
            if application['application_id'] == application_id:
                application['status'] = status
                application['decision'] = status
                application['decision_date'] = get_current_timestamp()
                application['notes'] = notes

                if approved_amount:
                    application['approved_amount'] = approved_amount

                return json.dumps({
                    "application_id": application_id,
                    "new_status": status,
                    "approved_amount": approved_amount,
                    "decision_date": application['decision_date'],
                    "notes": notes
                }, indent=2)

        return json.dumps({"error": f"Application {application_id} not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_loan_application_status",
                "description": "Update the status of a loan application",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "application_id": {"type": "string", "description": "Loan application identifier"},
                        "status": {"type": "string", "description": "New status", "enum": ["Approved", "Denied", "Under Review"]},
                        "approved_amount": {"type": "number", "description": "Approved loan amount"},
                        "notes": {"type": "string", "description": "Decision notes"}
                    },
                    "required": ["application_id", "status"]
                }
            }
        }
