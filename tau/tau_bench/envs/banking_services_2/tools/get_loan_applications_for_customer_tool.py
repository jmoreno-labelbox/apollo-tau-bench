# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetLoanApplicationsForCustomerTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id) -> str:
        loan_applications = data.get('loan_applications', [])
        result = []

        for application in loan_applications:
            if application.get('customer_id') == customer_id:
                result.append({
                    "application_id": application.get("application_id"),
                    "loan_type": application.get("loan_type"),
                    "requested_amount": application.get("requested_amount"),
                    "purpose": application.get("purpose"),
                    "annual_income": application.get("annual_income"),
                    "credit_score": application.get("credit_score"),
                    "status": application.get("status"),
                    "application_date": application.get("application_date"),
                    "decision": application.get("decision"),
                    "approved_amount": application.get("approved_amount"),
                    "notes": application.get("notes"),
                })

        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_loan_applications_for_customer",
                "description": "Get all loan applications for a specific customer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Customer identifier"}
                    },
                    "required": ["customer_id"]
                }
            }
        }
