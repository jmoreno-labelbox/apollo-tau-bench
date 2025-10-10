# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FreezeAccountOnFraudAlertTool(Tool):
    """
    Tool to freeze a customer account in response to a fraud alert.

    This tool locates the target account and changes its status to 'Frozen',
    while also storing the reason and timestamp of the freeze action.

    Methods:
        invoke(data: Dict[str, Any], **kwargs) -> str:
            Freezes the account with the given reason.

        get_info() -> Dict[str, Any]:
            Provides a schema of expected inputs for invoking the freeze operation.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        account_id = kwargs.get("account_id")
        alert_reason = kwargs.get("alert_reason")

        if not account_id or not alert_reason:
            return json.dumps(
                {"error": "account_id and alert_reason are required"}, indent=2
            )

        accounts = list(data.get("accounts", {}).values())
        account = next((a for a in accounts if a["account_id"] == account_id), None)
        if not account:
            return json.dumps({"error": "Account not found"}, indent=2)

        account["status"] = "Frozen"
        account["freeze_reason"] = alert_reason
        account["frozen_date"] = get_current_timestamp()

        return json.dumps(
            {
                "account_id": account_id,
                "new_status": "Frozen",
                "freeze_reason": alert_reason,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "freeze_account_on_fraud_alert",
                "description": "Freeze an account if fraud indicators are detected.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string", "description": "Account id"},
                        "alert_reason": {
                            "type": "string",
                            "description": "Alert reason",
                        },
                    },
                    "required": ["account_id", "alert_reason"],
                },
            },
        }
