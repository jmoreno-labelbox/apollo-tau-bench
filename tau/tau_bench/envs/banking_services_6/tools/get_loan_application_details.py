# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetLoanApplicationDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], application_id) -> str:
        application = next((app for app in data.get('loan_applications', []) if app['application_id'] == application_id), None)
        if application:
            return json.dumps(application)
        return json.dumps({"error": "Loan application not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_loan_application_details",
                        "description": "Retrieves the full details of a single loan application.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "application_id": {"type": "string", "description": "The unique ID of the loan application."}
                                },
                                "required": ["application_id"]
                        }
                }
        }
