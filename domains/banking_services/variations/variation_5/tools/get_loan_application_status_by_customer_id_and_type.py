from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timezone, date, timedelta
import calendar
from typing import Any, Dict
import random

class GetLoanApplicationStatusByCustomerIdAndType(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = "", loan_type: str = "") -> str:
        customer_id = customer_id.strip()
        loan_type = loan_type.strip().lower()

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

                # decision = app.get("decision") or {}

                # if status.lower() == "approved":
                #     response.update({
                #         "decision_date":   decision.get("decision_date"),
                #         "approved_amount": decision.get("approved_amount"),
                #         "interest_rate":   decision.get("interest_rate")
                #     })

                # elif status.lower() == "rejected":
                #     response["rejection_reason"] = decision.get("rejection_reason", "Not specified")

                # else:
                #     # Submitted, Under-Review, or other in-progress states
                # response["note"] = status

                return json.dumps(response, indent=2)

        return json.dumps({"message": "No matching loan application found."}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetLoanApplicationStatusByCustomerIdAndType",
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
