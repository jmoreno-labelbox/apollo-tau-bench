# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SummarizeLoanApplicationsByStatusTool(Tool):
    """
    Tool to provide a summary of loan applications categorized by status.

    This tool scans all loan applications and returns a count of how many fall
    under each status (e.g., Approved, Rejected, Pending). Useful for dashboards
    or trend analysis.

    Methods:
        invoke(data: Dict[str, Any], **kwargs) -> str:
            Summarizes the loan applications grouped by their status.

        get_info() -> Dict[str, Any]:
            Provides information about the expected parameters and return type.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], customer_id) -> str:
        if not customer_id:
            return json.dumps({"error": "customer_id is required"}, indent=2)

        applications = load_json("loan_applications.json")
        filtered = [a for a in applications if a["customer_id"] == customer_id]
        summary = {"approved": 0, "pending": 0, "rejected": 0}
        for a in filtered:
            status = a.get("status", "pending").lower()
            if status in summary:
                summary[status] += 1

        return json.dumps(summary, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "summarize_loan_applications_by_status",
                "description": "Generate summary of loan applications grouped by status for a customer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Customer ID"}
                    },
                    "required": ["customer_id"],
                },
            },
        }
