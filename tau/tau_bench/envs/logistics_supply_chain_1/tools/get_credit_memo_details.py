from tau_bench.envs.tool import Tool
import json
import random
from typing import Any

class GetCreditMemoDetails(Tool):
    """Obtains details for a specific credit memo."""

    @staticmethod
    def invoke(data: dict[str, Any], credit_memo_id: str = None) -> str:
        if not credit_memo_id:
            payload = {"error": "credit_memo_id is required."}
            out = json.dumps(payload, indent=2)
            return out

        memo = next(
            (
                m
                for m in data.get("credit_memos", [])
                if m.get("credit_memo_id") == credit_memo_id
            ),
            None,
        )
        if not memo:
            payload = {"error": f"Credit Memo '{credit_memo_id}' not found."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        payload = memo
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCreditMemoDetails",
                "description": "Retrieves the details of a specific credit memo by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "credit_memo_id": {
                            "type": "string",
                            "description": "The Credit Memo ID to search for.",
                        }
                    },
                    "required": ["credit_memo_id"],
                },
            },
        }
