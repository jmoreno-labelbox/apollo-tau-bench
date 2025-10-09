from tau_bench.envs.tool import Tool
import json
import os
from datetime import datetime, timedelta
from typing import Any, Dict

class DetectSuspiciousActivityAndAlertTool(Tool):
    """
    Tool to detect suspicious account activity and trigger an alert if necessary.

    This tool reviews transaction history for a given account and flags activity
    based on thresholds like unusually large amounts or unusual timing. If a match
    is found, it marks the account and issues a simulated alert.

    Methods:
        invoke(data: Dict[str, Any], **kwargs) -> str:
            Analyzes transactions and returns alert status.

        get_info() -> Dict[str, Any]:
            Describes the tool’s fraud detection criteria and input fields.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None) -> str:
        if not account_id:
            return json.dumps({"error": "account_id is required"}, indent=2)

        transactions = load_json("transactions.json")
        recent = [
            t
            for t in transactions
            if t["account_id"] == account_id and t.get("amount", 0) > 10000
        ]
        flagged = bool(recent)
        return json.dumps(
            {
                "flagged": flagged,
                "alert_id": f"alert_{generate_unique_id()}" if flagged else None,
            },
            indent=2,
        )
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DetectSuspiciousActivityAndAlert",
                "description": "Analyze recent transactions and flag suspicious patterns, triggering an alert.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {
                            "type": "string",
                            "description": "Account ID to monitor",
                        }
                    },
                    "required": ["account_id"],
                },
            },
        }
