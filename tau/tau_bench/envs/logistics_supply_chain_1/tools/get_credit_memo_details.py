# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCreditMemoDetails(Tool):
    """Retrieves details of a specific credit memo."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        credit_memo_id = kwargs.get('credit_memo_id')
        if not credit_memo_id:
            return json.dumps({"error": "credit_memo_id is required."}, indent=2)

        memo = next((m for m in data.get('credit_memos', []) if m.get('credit_memo_id') == credit_memo_id), None)
        if not memo:
            return json.dumps({"error": f"Credit Memo '{credit_memo_id}' not found."}, indent=2)

        return json.dumps(memo, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_credit_memo_details",
                "description": "Retrieves the details of a specific credit memo by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"credit_memo_id": {"type": "string", "description": "The Credit Memo ID to search for."}},
                    "required": ["credit_memo_id"]
                }
            }
        }
