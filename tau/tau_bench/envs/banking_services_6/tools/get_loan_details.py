# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetLoanDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], loan_id) -> str:
        loan = next((l for l in data['loans'] if l['loan_id'] == loan_id), None)
        if loan:
            return json.dumps(loan)
        return json.dumps({"error": "Loan not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_loan_details",
                        "description": "Retrieves full details for a specific loan.",
                        "parameters": {
                                "type": "object",
                                "properties": {"loan_id": {"type": "string"}},
                                "required": ["loan_id"]
                        }
                }
        }
