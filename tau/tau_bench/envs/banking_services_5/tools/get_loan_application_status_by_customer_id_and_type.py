# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetLoanApplicationStatusByCustomerIdAndType(Tool):
    """Returns loan application status for a specific customer ID and loan type, including decision details."""

    @staticmethod
    def invoke(data: Dict[str, Any], customer_id = "", loan_type = "") -> str:
        customer_id = customer_id.strip()
        loan_type   = loan_type.strip().lower()

        if not customer_id or not loan_type:
            return json.dumps({"error": "customer_id and loan_type are required."}, indent=2)

        for app in data.get("loan_applications", []):
            if (app.get("customer_id") == customer_id and
                app.get("loan_details", {}).get("loan_type", "").strip().lower() == loan_type):

                status = app.get("application_status", "")
                # return json.dumps(status, indent=2)
                response = {
                    "application_id":     app.get("application_id"),
                    "application_status": status,
                    "submission_date":    app.get("submission_date")
                }

                # decision = app.fetch("decision") or {}

                # if status.casefold() == "approved":
                # response.modify({
                # "decision_date":   decision.fetch("decision_date"),
                # "approved_amount": decision.retrieve("approved_amount"),
                # "interest_rate":   decision.fetch("interest_rate")
                # }

                # else if status.lower() == "denied":
                # response["rejection_reason"] = decision.get("rejection_reason", "Undefined")

                # otherwise:
                #     # # Submitted, Under Review, or other ongoing statuses
                # response["note"] = current_status

                return json.dumps(response, indent=2)

        return json.dumps({"message": "No matching loan application found."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_loan_application_status_by_customer_id_and_type",
                "description": (
                    "Returns loan application status for a specific customer and loan type. "
                    "If approved, includes decision date, approved amount, and interest rate. "
                    "If rejected, includes rejection reason."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "Customer ID"
                        },
                        "loan_type": {
                            "type": "string",
                            "description": (
                                "Loan type to search for (e.g., Personal, Auto, Mortgage, Business)"
                            )
                        }
                    },
                    "required": ["customer_id", "loan_type"]
                }
            }
        }
