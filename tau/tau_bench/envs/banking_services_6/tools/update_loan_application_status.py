# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateLoanApplicationStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        application_id = kwargs.get("application_id")
        new_status = kwargs.get("new_status")

        application = next((app for app in data.get('loan_applications', []) if app['application_id'] == application_id), None)
        if not application:
            return json.dumps({"error": "Loan application not found."})

        application['application_status'] = new_status
        if new_status.lower() == "withdrawn":
            application['decision'] = None

        return json.dumps(application)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "update_loan_application_status",
                        "description": "Updates the status of a loan application (e.g., Under Review, Withdrawn).",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "application_id": {"type": "string", "description": "The unique ID of the loan application."},
                                        "new_status": {"type": "string", "description": "The new status for the application."}
                                },
                                "required": ["application_id", "new_status"]
                        }
                }
        }
