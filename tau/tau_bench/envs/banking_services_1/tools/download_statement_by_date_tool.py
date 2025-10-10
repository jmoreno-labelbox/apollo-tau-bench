# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DownloadStatementByDateTool(Tool):
    """
    Tool to generate and download an account statement for a specific month and year.

    This tool compiles all relevant transactions for the period and formats them
    into a downloadable summary (simulated as a JSON string).

    Methods:
        invoke(data: Dict[str, Any], **kwargs) -> str:
            Generates the statement and returns a simulated file path.

        get_info() -> Dict[str, Any]:
            Provides metadata about input structure and time filters.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        account_id = kwargs.get("account_id")
        month = kwargs.get("month")
        if not account_id or not month:
            return json.dumps({"error": "account_id and month are required"}, indent=2)
        url = f"https://bank.example.com/statements/{account_id}/{month}.pdf"
        return json.dumps({"statement_url": url}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "download_statement_by_date",
                "description": "Download the account statement for a given month or date range.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {
                            "type": "string",
                            "description": "Account identifier",
                        },
                        "month": {
                            "type": "string",
                            "description": "Month string (e.g., 2024-05)",
                        },
                    },
                    "required": ["account_id", "month"],
                },
            },
        }
