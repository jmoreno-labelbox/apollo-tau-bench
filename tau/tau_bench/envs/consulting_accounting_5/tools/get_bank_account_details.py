# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetBankAccountDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_type) -> str:
        """
        Returns bank_account_id(s). Optionally filter by account_type (chequing/savings).
        """
        if account_type:
            ids = [b["account_id"] for b in data["bank_accounts"] if b["account_type"] == account_type]
        else:
            ids = [b["account_id"] for b in data["bank_accounts"]]
        return json.dumps(ids)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetBankAccountDetails",
                "description": "Retrieve bank_account_id(s), optionally filtered by account_type.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_type": {"type": "string", "description": "Optional filter (chequing, savings, etc.)"}
                    },
                    "required": [],
                },
            },
        }
