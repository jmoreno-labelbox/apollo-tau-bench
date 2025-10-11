from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any, Dict, List
import os
from . import load_json

class GetLoanDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], loan_id: str = None) -> str:
        if not loan_id:
            return json.dumps({"error": "loan_id is required"})

        loans = load_json("loans.json")

        loan = next((l for l in loans.values() if l["loan_id"] == loan_id), None)
        if not loan:
            return json.dumps({"error": f"Loan with ID '{loan_id}' not found"})

        return json.dumps({"loan_details": loan})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetLoanDetails",
                "description": "Fetches detailed information for a specific loan using its loan_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "loan_id": {
                            "type": "string",
                            "description": "The unique identifier of the loan."
                        }
                    },
                    "required": ["loan_id"]
                }
            }
        }
