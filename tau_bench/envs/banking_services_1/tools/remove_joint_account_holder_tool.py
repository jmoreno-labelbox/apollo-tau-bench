from tau_bench.envs.tool import Tool
import json
import os
from datetime import datetime, timedelta
from typing import Any, Dict

class RemoveJointAccountHolderTool(Tool):
    """
    Tool to remove a joint account holder from a shared account.

    This tool ensures the account and holder both exist, and then proceeds to
    disassociate the specified joint holder from the account.

    Methods:
        invoke(data: Dict[str, Any], **kwargs) -> str:
            Removes the joint account holder from the specified account.

        get_info() -> Dict[str, Any]:
            Supplies schema information and execution purpose.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None, holder_id: str = None) -> str:
        if not account_id or not holder_id:
            return json.dumps({"error": "Missing required parameters"}, indent=2)
        accounts = load_json("accounts_joint_holders.json")
        updated = False
        for acc in accounts:
            if acc["account_id"] == account_id and "joint_holders" in acc:
                if holder_id in acc["joint_holders"]:
                    acc["joint_holders"].remove(holder_id)
                    updated = True
        if updated:
            return json.dumps(
                {"status": "success", "removed_at": get_current_timestamp()},
                indent=2,
            )
        return json.dumps({"error": "Holder not found or account invalid"}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RemoveJointAccountHolder",
                "description": "Remove a joint account holder if no pending operations are linked.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {
                            "type": "string",
                            "description": "Account identifier",
                        },
                        "holder_id": {
                            "type": "string",
                            "description": "Holder identifier",
                        },
                    },
                    "required": ["account_id", "holder_id"],
                },
            },
        }
