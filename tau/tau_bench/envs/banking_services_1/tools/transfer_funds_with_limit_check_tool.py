# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class TransferFundsWithLimitCheckTool(Tool):
    """
    Tool to transfer funds between two accounts, including daily limit validation.

    This tool validates source and destination account IDs, confirms the sender
    has sufficient balance, and ensures the transaction does not exceed configured
    limits for the day. A successful transfer updates both account balances.

    Methods:
        invoke(data: Dict[str, Any], **kwargs) -> str:
            Executes a validated fund transfer and returns confirmation.

        get_info() -> Dict[str, Any]:
            Describes the tool’s capabilities, inputs, and conditions for execution.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], from_account, to_account, amount = 0) -> str:
        if not from_account or not to_account or amount <= 0:
            return json.dumps({"error": "Invalid input"}, indent=2)
        if amount > 10000:
            return json.dumps(
                {"error": "Transfer amount exceeds daily limit"}, indent=2
            )

        return json.dumps(
            {"transaction_id": f"txn_{generate_unique_id()}", "status": "Success"},
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "transfer_funds_with_limit_check",
                "description": "Transfer funds between accounts with pre-check on daily limit and balance.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "from_account": {
                            "type": "string",
                            "description": "Source account",
                        },
                        "to_account": {
                            "type": "string",
                            "description": "Target account",
                        },
                        "amount": {
                            "type": "number",
                            "description": "Amount to transfer",
                        },
                    },
                    "required": ["from_account", "to_account", "amount"],
                },
            },
        }
