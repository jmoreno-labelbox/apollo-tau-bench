# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetTotalLoanApplicationsCount(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        count = len(data.get("loan_applications", []))
        return json.dumps({"total_loan_applications": count})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_total_loan_applications_count",
                        "description": "Returns the current total number of loan applications in the system.",
                        "parameters": {"type": "object", "properties": {}},
                },
        }
